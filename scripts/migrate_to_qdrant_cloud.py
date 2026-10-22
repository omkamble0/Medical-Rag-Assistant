#!/usr/bin/env python3
"""
AegisMed - Qdrant Cloud Free Tier Database Migrator
Migrates the entire structured clinical database (100 conditions, 800+ symptoms,
300+ GDMT solutions, research papers, and vector embeddings) to Qdrant Cloud (Free Tier).

Usage:
    python scripts/migrate_to_qdrant_cloud.py
    python scripts/migrate_to_qdrant_cloud.py --url https://xxxx.us-east4-0.gcp.cloud.qdrant.io:6333 --api-key YOUR_KEY
    python scripts/migrate_to_qdrant_cloud.py --verify-only
"""

import os
import sys
import json
import re
import hashlib
import argparse
from pathlib import Path
from typing import List, Dict, Any, Optional

# Add root directory to sys.path
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))
sys.path.insert(0, str(BASE_DIR / "api"))

DATABASE_FILE = BASE_DIR / "api" / "app" / "data" / "medical_database.json"
COLLECTION_NAME = "medical_knowledge_collection"
VECTOR_DIM = 128


def load_env_variables() -> Dict[str, str]:
    """Loads environment variables from .env files if present."""
    env_vars: Dict[str, str] = {}
    for env_path in [BASE_DIR / ".env", BASE_DIR / "api" / ".env"]:
        if env_path.exists():
            with open(env_path, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if not line or line.startswith("#") or "=" not in line:
                        continue
                    k, v = line.split("=", 1)
                    k = k.strip()
                    v = v.strip().strip("'\"")
                    if k and v and k not in env_vars:
                        env_vars[k] = v
                        if k not in os.environ:
                            os.environ[k] = v
    return env_vars


def text_to_dense_vector(text: str, dim: int = 128) -> List[float]:
    """Generates deterministic dense semantic projection vector."""
    tokens = re.findall(r"[a-zA-Z0-9]+", text.lower())
    vec = [0.0] * dim
    for token in tokens:
        h = int(hashlib.md5(token.encode("utf-8")).hexdigest(), 16)
        idx = h % dim
        weight = 1.0 + (len(token) * 0.1)
        vec[idx] += weight
    norm = sum(x * x for x in vec) ** 0.5
    if norm > 0:
        vec = [x / norm for x in vec]
    return vec


def print_cloud_setup_guide():
    """Prints instructions for obtaining a 100% free Qdrant Cloud cluster."""
    print("=" * 76)
    print(" AegisMed: Qdrant Cloud (100% Free Tier) Setup Instructions")
    print("=" * 76)
    print("Qdrant Cloud provides a permanently free 1-node cluster (1 GB RAM / 4 GB disk),")
    print("which requires NO credit card and has more than enough capacity for the entire")
    print("clinical database, symptom indexes, and vector embeddings.\n")
    print("Steps to get your free online cloud database in 60 seconds:")
    print("  1. Open your browser and go to: https://cloud.qdrant.io")
    print("  2. Sign up with Google, GitHub, or Email (no credit card needed).")
    print("  3. Click 'Create Cluster' and select the 'Free Forever' (1GB RAM) plan.")
    print("  4. Once created, click on your cluster details:")
    print("     - Copy your Cluster URL (e.g., https://xxxxxxxx.us-east4-0.gcp.cloud.qdrant.io:6333)")
    print("     - Go to 'API Keys' tab and copy your API Key.")
    print("  5. Add them to your .env file:")
    print("     QDRANT_URL=https://xxxxxxxx.us-east4-0.gcp.cloud.qdrant.io:6333")
    print("     QDRANT_API_KEY=your_api_key_here\n")
    print("  6. Run this migration script again:")
    print("     python scripts/migrate_to_qdrant_cloud.py")
    print("=" * 76)



def migrate(cloud_url: str, api_key: Optional[str], verify_only: bool = False):
    """Executes the cloud migration to Qdrant Cloud."""
    try:
        from qdrant_client import QdrantClient
        from qdrant_client.models import VectorParams, Distance, PointStruct
    except ImportError:
        print("[!] Error: 'qdrant-client' is not installed in current environment.")
        print("    Install it via: pip install qdrant-client")
        sys.exit(1)

    print(f"[*] Connecting to Qdrant Cloud cluster at: {cloud_url} ...")
    try:
        client = QdrantClient(url=cloud_url, api_key=api_key, timeout=20.0)
        collections = client.get_collections().collections
        existing_names = [c.name for c in collections]
        print(f"[OK] Successfully authenticated with Qdrant Cloud cluster!")
        print(f"[*] Existing collections in cluster: {existing_names or 'None'}")
    except Exception as e:
        print(f"[!] Authentication / Connection error: {e}")
        print("\nPlease check your QDRANT_URL and QDRANT_API_KEY in .env.")
        sys.exit(1)

    if verify_only:
        if COLLECTION_NAME not in existing_names:
            print(f"[!] Collection '{COLLECTION_NAME}' does not exist on Qdrant Cloud yet.")
            print("    Run without '--verify-only' to perform the migration.")
            return

        info = client.get_collection(COLLECTION_NAME)
        print(f"[OK] Collection '{COLLECTION_NAME}' is ACTIVE on Qdrant Cloud!")
        print(f"     Total Indexed Vectors: {info.points_count}")
        print(f"     Vector Dimension: {info.config.params.vectors.size}")

        # Run test vector query
        test_query = "atrial fibrillation stroke prevention anticoagulation"
        test_vec = text_to_dense_vector(test_query, dim=VECTOR_DIM)
        hits = client.query_points(
            collection_name=COLLECTION_NAME,
            query=test_vec,
            limit=2
        ).points
        print(f"[*] Test query: '{test_query}'")
        for i, hit in enumerate(hits, 1):
            name = hit.payload.get("name") if hit.payload else "Unknown"
            score = round(hit.score, 4)
            print(f"    Rank #{i}: {name} (Similarity: {score})")
        print("\n[SUCCESS] Cloud database is online and fully responsive!")
        return

    # Check database file
    if not DATABASE_FILE.exists():
        print(f"[*] {DATABASE_FILE} not found. Building medical database first...")
        try:
            from scripts.build_medical_database import generate_database_and_qdrant
            generate_database_and_qdrant()
        except Exception as e:
            print(f"[!] Could not build database: {e}")
            sys.exit(1)

    print(f"[*] Reading clinical database from {DATABASE_FILE} ...")
    with open(DATABASE_FILE, "r", encoding="utf-8") as f:
        records = json.load(f)

    print(f"[OK] Loaded {len(records)} clinical disease records.")

    # Recreate or ensure collection
    if COLLECTION_NAME in existing_names:
        print(f"[*] Collection '{COLLECTION_NAME}' already exists on cluster. Resetting for fresh upload...")
        client.delete_collection(COLLECTION_NAME)

    print(f"[*] Creating collection '{COLLECTION_NAME}' with Cosine distance and {VECTOR_DIM}-dim vectors...")
    client.create_collection(
        collection_name=COLLECTION_NAME,
        vectors_config=VectorParams(size=VECTOR_DIM, distance=Distance.COSINE)
    )

    # Prepare vector points with full records as payload
    print(f"[*] Encoding {len(records)} conditions and generating dense vector embeddings...")
    points = []
    for i, rec in enumerate(records):
        symptom_text = " ".join([s["name"] for s in rec["symptoms"]])
        solution_text = " ".join([s["name"] + " " + s["description"] for s in rec["solutions"]])
        paper_text = " ".join([p["title"] + " " + p["key_findings"] for p in rec["research_papers"]])
        full_context = f"{rec['name']} {rec['specialty']} {rec['icd10_code']} {symptom_text} {solution_text} {paper_text}"

        vec = text_to_dense_vector(full_context, dim=VECTOR_DIM)

        points.append(
            PointStruct(
                id=i + 1,
                vector=vec,
                payload={
                    "disease_id": rec["id"],
                    "name": rec["name"],
                    "icd10": rec["icd10_code"],
                    "specialty": rec["specialty"],
                    "organ_system": rec["organ_system"],
                    "symptoms": [s["name"] for s in rec["symptoms"]],
                    "solutions": [s["name"] for s in rec["solutions"]],
                    "symptoms_count": len(rec["symptoms"]),
                    "solutions_count": len(rec["solutions"]),
                    "papers_count": len(rec["research_papers"]),
                    "patient_summary": rec["patient_plain_language"],
                    "overview": rec["overview"][:250],
                    # Entire structured monograph stored online in cloud payload
                    "full_record": rec
                }
            )
        )

    # Upload in batches of 25 points
    batch_size = 25
    total_uploaded = 0
    print(f"[*] Uploading points to Qdrant Cloud cluster in batches of {batch_size}...")
    for offset in range(0, len(points), batch_size):
        chunk = points[offset : offset + batch_size]
        client.upsert(collection_name=COLLECTION_NAME, points=chunk)
        total_uploaded += len(chunk)
        print(f"    [+] Uploaded {total_uploaded}/{len(points)} records...")

    # Verification
    info = client.get_collection(COLLECTION_NAME)
    print(f"\n" + "=" * 76)
    print(" [OK] MIGRATION COMPLETE!")
    print("=" * 76)
    print(f" Cloud Collection Name:  {COLLECTION_NAME}")
    print(f" Total Conditions:       {info.points_count}")
    print(f" Storage Type:           Qdrant Cloud Free Cluster (Online & Persistent)")
    print(f" Status:                 Ready for queries from any client anywhere!")

    # Test verification query
    print("\n[*] Performing live verification query against Qdrant Cloud:")
    test_query = "type 2 diabetes first line metformin hba1c"
    test_vec = text_to_dense_vector(test_query, dim=VECTOR_DIM)
    hits = client.query_points(
        collection_name=COLLECTION_NAME,
        query=test_vec,
        limit=3
    ).points

    for rank, hit in enumerate(hits, 1):
        d_name = hit.payload.get("name") if hit.payload else "Unknown"
        d_icd = hit.payload.get("icd10") if hit.payload else "N/A"
        print(f"  #{rank}: {d_name} (ICD-10: {d_icd}) - Similarity: {round(hit.score, 4)}")

    print("\n[OK] Your application will now automatically connect to Qdrant Cloud when started!")
    print("=" * 76)


def main():
    parser = argparse.ArgumentParser(description="Migrate AegisMed database to Qdrant Cloud Free Tier")
    parser.add_argument("--url", type=str, help="Qdrant Cloud cluster URL")
    parser.add_argument("--api-key", type=str, help="Qdrant Cloud API Key")
    parser.add_argument("--verify-only", action="store_true", help="Verify existing cloud collection without re-uploading")
    args = parser.parse_args()

    env_vars = load_env_variables()

    cloud_url = args.url or os.environ.get("QDRANT_URL") or env_vars.get("QDRANT_URL")
    api_key = args.api_key or os.environ.get("QDRANT_API_KEY") or env_vars.get("QDRANT_API_KEY")

    if not cloud_url:
        print("[!] No QDRANT_URL found in command arguments or .env file.\n")
        print_cloud_setup_guide()
        sys.exit(0)

    migrate(cloud_url=cloud_url, api_key=api_key, verify_only=args.verify_only)


if __name__ == "__main__":
    main()
