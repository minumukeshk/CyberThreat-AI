from pathlib import Path
import os

import pandas as pd
from sqlalchemy import create_engine, text
from sqlalchemy.engine import URL


# ==========================================
# CONFIGURATION
# ==========================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent
CSV_PATH = PROJECT_ROOT / "data" / "master_dataset.csv"

DATABASE_NAME = "cyberthreat_ai"
TABLE_NAME = "network_traffic"

MYSQL_USER = os.getenv("MYSQL_USER", "root")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD", "")
MYSQL_HOST = os.getenv("MYSQL_HOST", "localhost")
MYSQL_PORT = int(os.getenv("MYSQL_PORT", "3306"))

BATCH_SIZE = 2000


# ==========================================
# VERIFY DATASET
# ==========================================

if not CSV_PATH.exists():
    raise FileNotFoundError(f"Dataset not found: {CSV_PATH}")

print(f"Dataset found: {CSV_PATH}")

total_rows = sum(
    1 for _ in open(CSV_PATH, encoding="utf-8-sig")
) - 1

print(f"Total CSV records: {total_rows:,}")


# ==========================================
# DATABASE CONNECTION
# ==========================================

connection_url = URL.create(
    drivername="mysql+pymysql",
    username=MYSQL_USER,
    password=MYSQL_PASSWORD,
    host=MYSQL_HOST,
    port=MYSQL_PORT,
    database=DATABASE_NAME,
)

engine = create_engine(
    connection_url,
    pool_pre_ping=True,
)


# ==========================================
# TEST CONNECTION
# ==========================================

with engine.connect() as connection:
    connection.execute(text("SELECT 1"))

print("MySQL connection successful!", flush=True)


# ==========================================
# IMPORT DATA IN BATCHES
# ==========================================

imported_rows = 0
first_batch = True

try:
    for chunk in pd.read_csv(
        CSV_PATH,
        chunksize=BATCH_SIZE,
        low_memory=False,
    ):

        print(
            f"Processing batch: {len(chunk):,} records",
            flush=True
        )

        chunk.to_sql(
            name=TABLE_NAME,
            con=engine,
            if_exists="replace" if first_batch else "append",
            index=False,
            method=None,
            chunksize=200,
        )

        imported_rows += len(chunk)
        first_batch = False

        print(
            f"Imported {imported_rows:,} / {total_rows:,} records",
            flush=True
        )

except Exception:
    print("Import failed. Check the error above.", flush=True)
    raise


# ==========================================
# FINAL VERIFICATION
# ==========================================

with engine.connect() as connection:

    record_count = connection.execute(
        text(f"SELECT COUNT(*) FROM `{TABLE_NAME}`")
    ).scalar()

    column_count = connection.execute(
        text("""
            SELECT COUNT(*)
            FROM INFORMATION_SCHEMA.COLUMNS
            WHERE TABLE_SCHEMA = :database_name
            AND TABLE_NAME = :table_name
        """),
        {
            "database_name": DATABASE_NAME,
            "table_name": TABLE_NAME,
        },
    ).scalar()

    category_count = connection.execute(
        text(f"""
            SELECT COUNT(DISTINCT Label)
            FROM `{TABLE_NAME}`
        """)
    ).scalar()


# ==========================================
# IMPORT SUMMARY
# ==========================================

print("\n========== IMPORT SUMMARY ==========")
print(f"CSV Records       : {total_rows:,}")
print(f"Imported Records  : {record_count:,}")
print(f"Total Columns     : {column_count}")
print(f"Unique Categories : {category_count}")

if (
    record_count == total_rows
    and column_count == 77
    and category_count == 15
):
    print("\nSUCCESS: Dataset imported and verified!")

else:
    print("\nWARNING: Verification does not match expectations.")

engine.dispose()