from pathlib import Path

import mysql.connector

import pandas as pd

# ============================================================
# PATHS
# ============================================================

BASE_DIR = Path(__file__).resolve().parent.parent

CSV_PATH = BASE_DIR / "03_Clean_Data" / "movies_clean.csv"


# ============================================================
# MYSQL CONNECTION
# ============================================================

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="yasinsql007",
    database="movie_boxoffice"
)

cursor = connection.cursor()


# ============================================================
# LOAD CLEAN CSV
# ============================================================

df = pd.read_csv(CSV_PATH)

print("\n========== CLEAN DATA LOADED ==========\n")
print("Rows:", len(df))
print("Columns:", len(df.columns))


# ============================================================
# CONVERT NaN → None
# MySQL connector converts Python None into SQL NULL
# ============================================================

df = df.astype(object)
df = df.where(pd.notna(df), None)


# ============================================================
# INSERT QUERY
# ============================================================

insert_query = """
INSERT INTO movies (
    s_no,
    movie_title,
    genre,
    budget_cr,
    director_success_rate,
    lead_actor_success_rate,
    imdb,
    trailer_views_m,
    box_office_revenue,
    revenue_status,
    director_success_status,
    actor_success_status,
    profit_cr,
    roi_percent,
    hit_flop
)
VALUES (
    %s, %s, %s, %s, %s,
    %s, %s, %s, %s, %s,
    %s, %s, %s, %s, %s
)
"""


# ============================================================
# PREPARE DATA
# ============================================================

records = [
    tuple(row)
    for row in df.itertuples(index=False, name=None)
]


# ============================================================
# INSERT DATA
# ============================================================

cursor.executemany(insert_query, records)

connection.commit()

print("\n========== MYSQL IMPORT COMPLETE ==========\n")
print("Rows inserted:", cursor.rowcount)


# ============================================================
# CLOSE CONNECTION
# ============================================================

cursor.close()
connection.close()

print("\nMySQL connection closed.")