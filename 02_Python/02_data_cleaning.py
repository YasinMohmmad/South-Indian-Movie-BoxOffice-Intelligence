# ============================================================
# PROJECT 5: MOVIE BOX OFFICE & REVENUE INTELLIGENCE
# PART A - DATA CLEANING
# ============================================================

from pathlib import Path

import numpy as np

import pandas as pd

# ------------------------------------------------------------
# 1. LOAD RAW DATA
# ------------------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

RAW_DATA_PATH = BASE_DIR / "01_Raw_Data" / "imdb_movies.csv"

OUTPUT_PATH = BASE_DIR / "03_Clean_Data" / "movies_clean.csv"

df = pd.read_csv(RAW_DATA_PATH)


print("\n========== RAW DATA LOADED ==========\n")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])


# ------------------------------------------------------------
# 2. CREATE A COPY
# ------------------------------------------------------------

clean_df = df.copy()


# ------------------------------------------------------------
# 3. STANDARDIZE COLUMN NAMES
# ------------------------------------------------------------

clean_df.columns = (
    clean_df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
    .str.replace("(", "", regex=False)
    .str.replace(")", "", regex=False)
)


print("\n========== STANDARDIZED COLUMNS ==========\n")
print(clean_df.columns.tolist())


print("\n========== TRAILER VIEWS VALIDATION ==========\n")

original_trailer_views = clean_df["trailer_views_m"].copy()

clean_df["trailer_views_m"] = pd.to_numeric(
    clean_df["trailer_views_m"],
    errors="coerce"
)

invalid_trailer_views = clean_df["trailer_views_m"].isna()

print("Invalid Trailer Views:", invalid_trailer_views.sum())

print("\nInvalid Trailer Views records:\n")
print(
    clean_df.loc[
        invalid_trailer_views,
        ["movie_title", "trailer_views_m"]
    ]
)

# ------------------------------------------------------------
# 5. VALIDATE IMDb RATINGS
# ------------------------------------------------------------

invalid_imdb = (clean_df["imdb"] < 0) | (clean_df["imdb"] > 10)

print("\n========== IMDb VALIDATION ==========\n")

print("Invalid IMDb ratings:", invalid_imdb.sum())

print("\nInvalid IMDb records:\n")

print(
    clean_df.loc[
        invalid_imdb,
        ["movie_title", "imdb"]
    ]
)

# Replace invalid ratings with missing values
clean_df.loc[invalid_imdb, "imdb"] = np.nan


# ------------------------------------------------------------
# 6. CREATE DATA QUALITY FLAGS
# ------------------------------------------------------------

clean_df["revenue_status"] = np.where(
    clean_df["box_office_revenue"] == 0,
    "Zero Revenue",
    "Available"
)


clean_df["director_success_status"] = np.where(
    clean_df["director_success_rate"] == 0,
    "No Recorded Success",
    "Recorded Success"
)


clean_df["actor_success_status"] = np.where(
    clean_df["lead_actor_success_rate"] == 0,
    "No Recorded Success",
    "Recorded Success"
)


# ------------------------------------------------------------
# 7. CALCULATE PROFIT
# ------------------------------------------------------------

clean_df["profit_cr"] = (
    clean_df["box_office_revenue"]
    - clean_df["budget_cr"]
)


# ------------------------------------------------------------
# 8. CALCULATE ROI
# ------------------------------------------------------------

clean_df["roi_percent"] = np.where(
    clean_df["budget_cr"] > 0,
    (clean_df["profit_cr"] / clean_df["budget_cr"]) * 100,
    np.nan
)


# ------------------------------------------------------------
# 9. HIT / FLOP CLASSIFICATION
# ------------------------------------------------------------

clean_df["hit_flop"] = np.where(
    clean_df["profit_cr"] > 0,
    "Hit",
    "Flop"
)


# ------------------------------------------------------------
# 10. FINAL VALIDATION
# ------------------------------------------------------------

print("\n========== FINAL VALIDATION ==========\n")

print("Rows:", len(clean_df))
print("Columns:", len(clean_df.columns))

print("\nMissing values:")
print(clean_df.isnull().sum())

print("\nDuplicate rows:")
print(clean_df.duplicated().sum())

print("\nHit / Flop distribution:")
print(clean_df["hit_flop"].value_counts())


print("\n========== PROFITABILITY ANALYSIS ==========\n")

print("Profitable movies:", (clean_df["profit_cr"] > 0).sum())
print("Loss-making movies:", (clean_df["profit_cr"] <= 0).sum())

print("\nProfit summary:")
print(clean_df["profit_cr"].describe())

print("\nROI summary:")
print(clean_df["roi_percent"].describe())

print("\n========== DATA QUALITY SUMMARY ==========\n")

print("Total Records:", len(clean_df))
print("Total Columns:", len(clean_df.columns))
print("Duplicate Records:", clean_df.duplicated().sum())

print("\nMissing Values:")
print(clean_df.isnull().sum())

print("\nGenre Distribution:")
print(clean_df["genre"].value_counts())

print("\nRevenue Status:")
print(clean_df["revenue_status"].value_counts())

print("\nHit / Flop Distribution:")
print(clean_df["hit_flop"].value_counts())

print("\nProfit Summary:")
print(clean_df["profit_cr"].describe())

print("\nROI Summary:")
print(clean_df["roi_percent"].describe())

print("\nIMDb Summary:")
print(clean_df["imdb"].describe())

# ------------------------------------------------------------
# 11. SAVE CLEAN DATA
# ------------------------------------------------------------

clean_df.to_csv(
    OUTPUT_PATH,
    index=False
)


print("\n========== CLEAN DATA EXPORTED ==========\n")
print("File:", OUTPUT_PATH)