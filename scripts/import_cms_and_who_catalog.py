"""
AegisMed Master Clinical Taxonomy Importer
Downloads and parses the complete official CMS ICD-10-CM (97,000+ codes)
and WHO ICD-11 MMS (36,000+ entities) master catalogs into a high-performance
SQLite database (clinical_taxonomy.db) with FTS5 sub-millisecond search.
"""

import os
import sys
import io
import re
import json
import sqlite3
import zipfile
import urllib.request
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("TaxonomyImporter")

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "api", "app", "data")
DB_PATH = os.path.join(DATA_DIR, "clinical_taxonomy.db")

CMS_ZIP_URL = "https://ftp.cdc.gov/pub/Health_Statistics/NCHS/Publications/ICD10CM/2025/ICD10-CM%20Code%20Descriptions%202025.zip"
WHO_ZIP_URL = "https://icdcdn.who.int/static/releasefiles/2024-01/SimpleTabulation-ICD-11-MMS-en.zip"

ICD10_CHAPTERS = {
    "A": "Certain infectious and parasitic diseases",
    "B": "Certain infectious and parasitic diseases",
    "C": "Neoplasms",
    "D": "Neoplasms and blood disorders",
    "E": "Endocrine, nutritional and metabolic diseases",
    "F": "Mental, Behavioral and Neurodevelopmental disorders",
    "G": "Diseases of the nervous system",
    "H": "Diseases of the eye, adnexa, ear and mastoid",
    "I": "Diseases of the circulatory system",
    "J": "Diseases of the respiratory system",
    "K": "Diseases of the digestive system",
    "L": "Diseases of the skin and subcutaneous tissue",
    "M": "Diseases of the musculoskeletal system and connective tissue",
    "N": "Diseases of the genitourinary system",
    "O": "Pregnancy, childbirth and the puerperium",
    "P": "Certain conditions originating in the perinatal period",
    "Q": "Congenital malformations, deformations and chromosomal abnormalities",
    "R": "Symptoms, signs and abnormal clinical and laboratory findings",
    "S": "Injury, poisoning and certain other consequences of external causes",
    "T": "Injury, poisoning and certain other consequences of external causes",
    "U": "Codes for special purposes (e.g. COVID-19, vaping)",
    "V": "External causes of morbidity",
    "W": "External causes of morbidity",
    "X": "External causes of morbidity",
    "Y": "External causes of morbidity",
    "Z": "Factors influencing health status and contact with health services"
}

def format_icd10_code(raw_code: str) -> str:
    raw = raw_code.strip()
    if len(raw) > 3 and "." not in raw:
        return f"{raw[:3]}.{raw[3:]}"
    return raw


def download_zip(url: str, label: str) -> zipfile.ZipFile:
    logger.info(f"Downloading {label} from {url}...")
    headers = {"User-Agent": "AegisMed/1.0 (Clinical Taxonomy Importer)"}
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=60) as resp:
        content = resp.read()
    logger.info(f"Downloaded {len(content) / (1024*1024):.2f} MB of {label} data.")
    return zipfile.ZipFile(io.BytesIO(content))


def init_database(db_path: str) -> sqlite3.Connection:
    os.makedirs(os.path.dirname(db_path), exist_ok=True)
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    cur.execute("DROP TABLE IF EXISTS clinical_catalog")
    cur.execute("DROP TABLE IF EXISTS clinical_catalog_fts")

    cur.execute("""
        CREATE TABLE clinical_catalog (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            source TEXT NOT NULL,
            code TEXT NOT NULL,
            raw_code TEXT,
            title TEXT NOT NULL,
            short_desc TEXT,
            category TEXT,
            chapter TEXT,
            is_billable INTEGER DEFAULT 1,
            foundation_uri TEXT,
            has_curated_monograph INTEGER DEFAULT 0
        )
    """)

    cur.execute("CREATE INDEX idx_catalog_code ON clinical_catalog (code)")
    cur.execute("CREATE INDEX idx_catalog_source ON clinical_catalog (source)")

    cur.execute("""
        CREATE VIRTUAL TABLE clinical_catalog_fts USING fts5(
            title,
            code,
            category,
            content=clinical_catalog,
            content_rowid=id
        )
    """)

    conn.commit()
    return conn


def load_curated_monograph_codes() -> set:
    curated_path = os.path.join(DATA_DIR, "medical_database.json")
    curated_codes = set()
    if os.path.exists(curated_path):
        try:
            with open(curated_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                for item in data:
                    c = item.get("icd10_code", "").strip().upper()
                    if c:
                        curated_codes.add(c)
                        curated_codes.add(c.replace(".", ""))
        except Exception as e:
            logger.warning(f"Could not load curated codes: {e}")
    logger.info(f"Loaded {len(curated_codes)} curated ICD-10 codes from existing rich monographs.")
    return curated_codes


def import_cms_icd10(conn: sqlite3.Connection, curated_codes: set) -> int:
    z = download_zip(CMS_ZIP_URL, "CMS 2025 ICD-10-CM Master Catalog")
    
    # Locate order file inside zip
    order_filename = None
    for name in z.namelist():
        if "order" in name.lower() and name.endswith(".txt") and "addenda" not in name.lower():
            order_filename = name
            break
    if not order_filename:
        for name in z.namelist():
            if name.endswith(".txt") and "codes" in name.lower() and "addenda" not in name.lower():
                order_filename = name
                break

    if not order_filename:
        raise ValueError(f"Could not find ICD-10 order text file in {z.namelist()}")

    logger.info(f"Parsing CMS file: {order_filename}...")
    lines = z.read(order_filename).decode("utf-8", errors="ignore").splitlines()

    cur = conn.cursor()
    batch = []
    count = 0

    for line in lines:
        if len(line) < 16:
            continue
        # Fixed width layout:
        # 0-5: order number
        # 6-13: raw code
        # 14: billable flag (0 = header/category, 1 = valid diagnosis)
        # 16-76: short description
        # 77+: long description
        raw_code = line[6:14].strip()
        billable_char = line[14:15].strip()
        is_billable = 1 if billable_char == "1" else 0
        
        short_desc = line[16:77].strip()
        long_desc = line[77:].strip() if len(line) > 77 else short_desc
        title = long_desc or short_desc

        if not raw_code:
            continue

        formatted_code = format_icd10_code(raw_code)
        first_char = raw_code[0].upper()
        chapter = ICD10_CHAPTERS.get(first_char, "Other Medical Conditions")
        has_monograph = 1 if (formatted_code.upper() in curated_codes or raw_code.upper() in curated_codes) else 0

        batch.append((
            "CMS_ICD10",
            formatted_code,
            raw_code,
            title,
            short_desc,
            chapter,
            f"Chapter {first_char}: {chapter}",
            is_billable,
            None,
            has_monograph
        ))
        count += 1

        if len(batch) >= 5000:
            cur.executemany("""
                INSERT INTO clinical_catalog (
                    source, code, raw_code, title, short_desc, category, chapter, is_billable, foundation_uri, has_curated_monograph
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, batch)
            conn.commit()
            batch = []

    if batch:
        cur.executemany("""
            INSERT INTO clinical_catalog (
                source, code, raw_code, title, short_desc, category, chapter, is_billable, foundation_uri, has_curated_monograph
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, batch)
        conn.commit()

    logger.info(f"[OK] Successfully imported {count:,} CMS ICD-10-CM diagnostic conditions.")
    return count


def import_who_icd11(conn: sqlite3.Connection) -> int:
    z = download_zip(WHO_ZIP_URL, "WHO ICD-11 MMS Master Catalog")
    
    tsv_filename = None
    for name in z.namelist():
        if "SimpleTabulation" in name and name.endswith(".txt"):
            tsv_filename = name
            break
    if not tsv_filename:
        for name in z.namelist():
            if name.endswith(".txt") and "readme" not in name.lower():
                tsv_filename = name
                break

    if not tsv_filename:
        raise ValueError(f"Could not find WHO tabulation file in {z.namelist()}")

    logger.info(f"Parsing WHO file: {tsv_filename}...")
    raw_content = z.read(tsv_filename).decode("utf-8-sig", errors="ignore")
    lines = raw_content.splitlines()

    if not lines:
        return 0

    header_cols = [c.strip().lower() for c in lines[0].split("\t")]
    col_map = {col: idx for idx, col in enumerate(header_cols)}

    code_idx = col_map.get("code")
    title_idx = col_map.get("title")
    uri_idx = col_map.get("foundation uri") or col_map.get("foundationuri")
    chap_idx = col_map.get("chapterno")
    class_idx = col_map.get("classkind")

    cur = conn.cursor()
    batch = []
    count = 0

    for line in lines[1:]:
        parts = line.split("\t")
        if len(parts) <= max(code_idx or 0, title_idx or 0):
            continue

        raw_title = parts[title_idx].strip() if title_idx is not None and title_idx < len(parts) else ""
        # Clean leading dashes and quotes in WHO titles: e.g. "- - Cholera" or "\"Cholera\""
        clean_title = re.sub(r'^[-\s"]+|[-\s"]+$', '', raw_title).strip()
        code = parts[code_idx].strip() if code_idx is not None and code_idx < len(parts) else ""
        uri = parts[uri_idx].strip() if uri_idx is not None and uri_idx < len(parts) else ""
        chap = parts[chap_idx].strip() if chap_idx is not None and chap_idx < len(parts) else ""
        class_kind = parts[class_idx].strip() if class_idx is not None and class_idx < len(parts) else "category"

        if not clean_title or len(clean_title) < 2:
            continue

        display_code = code if code else (f"WHO-{chap}" if chap else "WHO-ENTITY")
        chapter_title = f"WHO Chapter {chap}" if chap else "WHO Classification"

        batch.append((
            "WHO_ICD11",
            display_code,
            code,
            clean_title,
            clean_title,
            chapter_title,
            class_kind,
            1 if code else 0,
            uri,
            0
        ))
        count += 1

        if len(batch) >= 5000:
            cur.executemany("""
                INSERT INTO clinical_catalog (
                    source, code, raw_code, title, short_desc, category, chapter, is_billable, foundation_uri, has_curated_monograph
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, batch)
            conn.commit()
            batch = []

    if batch:
        cur.executemany("""
            INSERT INTO clinical_catalog (
                source, code, raw_code, title, short_desc, category, chapter, is_billable, foundation_uri, has_curated_monograph
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, batch)
        conn.commit()

    logger.info(f"[OK] Successfully imported {count:,} WHO ICD-11 entities.")
    return count


def populate_fts(conn: sqlite3.Connection):
    logger.info("Building FTS5 index for sub-millisecond search across entire catalog...")
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO clinical_catalog_fts (rowid, title, code, category)
        SELECT id, title, code, category FROM clinical_catalog
    """)
    conn.commit()
    logger.info("[OK] FTS5 search index successfully constructed.")


def main():
    logger.info("=========================================================")
    logger.info("🚀 Starting Master CMS & WHO Clinical Taxonomy Ingestion")
    logger.info(f"Target Database: {DB_PATH}")
    logger.info("=========================================================")

    curated_codes = load_curated_monograph_codes()
    conn = init_database(DB_PATH)

    cms_count = import_cms_icd10(conn, curated_codes)
    who_count = import_who_icd11(conn)
    populate_fts(conn)

    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM clinical_catalog")
    total_records = cur.fetchone()[0]

    cur.execute("SELECT COUNT(*) FROM clinical_catalog WHERE has_curated_monograph = 1")
    matched_monographs = cur.fetchone()[0]

    conn.close()

    db_size_mb = os.path.getsize(DB_PATH) / (1024 * 1024)

    logger.info("=========================================================")
    logger.info(f"✅ Ingestion Complete!")
    logger.info(f"   - CMS ICD-10-CM Records: {cms_count:,}")
    logger.info(f"   - WHO ICD-11 Records:    {who_count:,}")
    logger.info(f"   - Total Master Catalog:  {total_records:,} conditions")
    logger.info(f"   - Linked Rich Monographs:{matched_monographs:,} direct matches")
    logger.info(f"   - Database File Size:    {db_size_mb:.2f} MB")
    logger.info("=========================================================")


if __name__ == "__main__":
    main()
