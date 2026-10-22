"""
AegisMed Unified Clinical Taxonomy Service
Provides sub-millisecond search and lookup across 133,628 official CMS ICD-10-CM
and WHO ICD-11 conditions using SQLite FTS5 with linkage to rich Oxford CEBM monographs.
"""

import os
import sqlite3
import logging
from typing import List, Dict, Any, Optional
from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "data", "clinical_taxonomy.db")


class TaxonomyEntity(BaseModel):
    id: int
    source: str = Field(..., description="CMS_ICD10 or WHO_ICD11")
    code: str
    raw_code: Optional[str] = None
    title: str
    short_desc: Optional[str] = None
    category: str
    chapter: Optional[str] = None
    is_billable: bool = True
    foundation_uri: Optional[str] = None
    has_curated_monograph: bool = False
    monograph_id: Optional[str] = None


class TaxonomySearchResponse(BaseModel):
    total_matches: int
    query: str
    results: List[TaxonomyEntity]
    latency_ms: float


class ClinicalTaxonomyService:
    def __init__(self, db_path: str = DB_PATH):
        self.db_path = db_path
        self._ensure_database()

    def _ensure_database(self):
        if not os.path.exists(self.db_path):
            logger.warning(f"Taxonomy database not found at {self.db_path}. Running importer...")
            try:
                import subprocess
                script_path = os.path.join(os.path.dirname(BASE_DIR), "scripts", "import_cms_and_who_catalog.py")
                subprocess.run(["python", script_path], check=True)
            except Exception as e:
                logger.error(f"Failed to auto-import clinical taxonomy: {e}")

    def _get_connection(self) -> sqlite3.Connection:
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        return conn

    def search(
        self,
        query: str,
        source: Optional[str] = None,
        limit: int = 25,
        offset: int = 0
    ) -> List[Dict[str, Any]]:
        """
        Fast full-text search across 133,628 CMS and WHO conditions.
        Supports prefix queries, exact codes, and multi-word terms.
        """
        if not os.path.exists(self.db_path):
            return []

        clean_query = query.strip()
        if not clean_query:
            return []

        # Sanitize for FTS5 (escape quotes and special tokens)
        sanitized_words = [re.sub(r'[^a-zA-Z0-9\.]', '', w) for w in clean_query.split()]
        sanitized_words = [w for w in sanitized_words if w]
        if not sanitized_words:
            return []

        # Exact code match first: e.g. "I10", "A00.0", "1A00"
        conn = self._get_connection()
        cur = conn.cursor()

        exact_results = []
        code_query = clean_query.upper().replace(" ", "")
        cur.execute("""
            SELECT id, source, code, raw_code, title, short_desc, category, chapter, is_billable, foundation_uri, has_curated_monograph
            FROM clinical_catalog
            WHERE code = ? OR raw_code = ?
            LIMIT 5
        """, (code_query, code_query))
        for row in cur.fetchall():
            exact_results.append(dict(row))

        # FTS5 search expression: e.g. "cholera*" OR "heart*"
        fts_query = " ".join([f'"{w}"*' for w in sanitized_words])

        source_clause = ""
        params = [fts_query]
        if source:
            source_clause = "AND c.source = ?"
            params.append(source)

        params.extend([limit, offset])

        query_sql = f"""
            SELECT c.id, c.source, c.code, c.raw_code, c.title, c.short_desc, c.category, c.chapter, c.is_billable, c.foundation_uri, c.has_curated_monograph,
                   rank
            FROM clinical_catalog_fts f
            JOIN clinical_catalog c ON f.rowid = c.id
            WHERE clinical_catalog_fts MATCH ?
            {source_clause}
            ORDER BY rank
            LIMIT ? OFFSET ?
        """

        try:
            cur.execute(query_sql, params)
            fts_rows = [dict(r) for r in cur.fetchall()]
        except Exception as e:
            # Fallback to standard LIKE if FTS expression has syntax quirk
            logger.debug(f"FTS match notice, falling back to LIKE: {e}")
            like_term = f"%{clean_query}%"
            cur.execute("""
                SELECT id, source, code, raw_code, title, short_desc, category, chapter, is_billable, foundation_uri, has_curated_monograph
                FROM clinical_catalog
                WHERE title LIKE ? OR code LIKE ?
                LIMIT ?
            """, (like_term, like_term, limit))
            fts_rows = [dict(r) for r in cur.fetchall()]

        conn.close()

        # Combine exact code hits at top with FTS rows
        seen_ids = set()
        merged = []
        for r in exact_results + fts_rows:
            if r["id"] not in seen_ids:
                seen_ids.add(r["id"])
                r["is_billable"] = bool(r["is_billable"])
                r["has_curated_monograph"] = bool(r["has_curated_monograph"])
                merged.append(r)

        return merged[:limit]

    def get_by_code(self, code: str) -> Optional[Dict[str, Any]]:
        """Look up condition directly by ICD-10 or ICD-11 code."""
        if not os.path.exists(self.db_path):
            return None

        clean_code = code.strip().upper()
        conn = self._get_connection()
        cur = conn.cursor()
        cur.execute("""
            SELECT id, source, code, raw_code, title, short_desc, category, chapter, is_billable, foundation_uri, has_curated_monograph
            FROM clinical_catalog
            WHERE code = ? OR raw_code = ?
            LIMIT 1
        """, (clean_code, clean_code))
        row = cur.fetchone()
        conn.close()
        if row:
            res = dict(row)
            res["is_billable"] = bool(res["is_billable"])
            res["has_curated_monograph"] = bool(res["has_curated_monograph"])
            return res
        return None

    def get_stats(self) -> Dict[str, Any]:
        """Returns catalog statistics."""
        if not os.path.exists(self.db_path):
            return {"total_conditions": 0, "status": "not_initialized"}

        conn = self._get_connection()
        cur = conn.cursor()
        cur.execute("SELECT COUNT(*) FROM clinical_catalog")
        total = cur.fetchone()[0]

        cur.execute("SELECT source, COUNT(*) FROM clinical_catalog GROUP BY source")
        by_source = {row[0]: row[1] for row in cur.fetchall()}

        cur.execute("SELECT COUNT(*) FROM clinical_catalog WHERE has_curated_monograph = 1")
        rich_monographs = cur.fetchone()[0]

        conn.close()
        return {
            "total_conditions": total,
            "cms_icd10_count": by_source.get("CMS_ICD10", 0),
            "who_icd11_count": by_source.get("WHO_ICD11", 0),
            "linked_rich_monographs": rich_monographs,
            "status": "ready"
        }


import re

# Singleton instance
taxonomy_service = ClinicalTaxonomyService()
