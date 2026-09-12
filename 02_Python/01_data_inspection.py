# ============================================================
# PROJECT 5: MOVIE BOX OFFICE & REVENUE INTELLIGENCE
# PART A - DATA INSPECTION
# ============================================================

from pathlib import Path

# import numpy as np
import pandas as pd

# ------------------------------------------------------------
# 1. LOAD DATASET
# ------------------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_PATH = BASE_DIR / "01_Raw_Data" / "imdb_movies.csv"

df = pd.read_csv(DATA_PATH)


# ------------------------------------------------------------
# 2. BASIC DATASET INFORMATION
# ------------------------------------------------------------

print("\n========== DATASET SHAPE ==========\n")
print(df.shape)


print("\n========== COLUMN NAMES ==========\n")
print(df.columns.tolist())


print("\n========== FIRST 5 ROWS ==========\n")
print(df.head())


print("\n========== DATA TYPES ==========\n")
print(df.dtypes)


print("\n========== DATASET INFORMATION ==========\n")
df.info()


# ------------------------------------------------------------
# 3. MISSING VALUE ANALYSIS
# ------------------------------------------------------------

print("\n========== MISSING VALUES ==========\n")
print(df.isnull().sum())


print("\n========== MISSING VALUE PERCENTAGE ==========\n")

missing_percentage = (df.isnull().sum() / len(df)) * 100

print(missing_percentage.round(2))


# ------------------------------------------------------------
# 4. DUPLICATE ANALYSIS
# ------------------------------------------------------------

print("\n========== DUPLICATE RECORDS ==========\n")

duplicate_count = df.duplicated().sum()

print("Number of duplicate rows:", duplicate_count)


# ------------------------------------------------------------
# 5. NUMERICAL SUMMARY
# ------------------------------------------------------------

print("\n========== NUMERICAL SUMMARY ==========\n")

print(df.describe())


# ------------------------------------------------------------
# 8. INVESTIGATE IMDb RATINGS
# ------------------------------------------------------------

print("\n========== IMDb RATING INVESTIGATION ==========\n")

print("Minimum IMDb rating:", df["IMDb"].min())
print("Maximum IMDb rating:", df["IMDb"].max())

print("\nMovies with IMDb rating above 10:\n")

print(
    df[df["IMDb"] > 10][
        ["Movie Title", "IMDb"]
    ]
)



# ------------------------------------------------------------
# 9. INVESTIGATE TRAILER VIEWS
# ------------------------------------------------------------

print("\n========== TRAILER VIEWS INVESTIGATION ==========\n")

print("Data type:", df["Trailer Views (M)"].dtype)

print("\nSample Trailer Views values:\n")

print(df["Trailer Views (M)"].head(20).to_string(index=False))

print("\nUnique Trailer Views data types:\n")

print(
    df["Trailer Views (M)"]
    .apply(type)
    .value_counts()
)


# ------------------------------------------------------------
# 10. INVESTIGATE BUDGET VALUES
# ------------------------------------------------------------

print("\n========== BUDGET INVESTIGATION ==========\n")

print("Minimum Budget:", df["Budget (Cr)"].min())
print("Maximum Budget:", df["Budget (Cr)"].max())

print("\nMovies with Budget below 1 Cr:\n")

print(
    df[df["Budget (Cr)"] < 1][
        ["Movie Title", "Budget (Cr)", "Box Office Revenue"]
    ].sort_values("Budget (Cr)")
)



# ------------------------------------------------------------
# 11. INVESTIGATE ZERO REVENUE
# ------------------------------------------------------------

print("\n========== ZERO REVENUE INVESTIGATION ==========\n")

zero_revenue = df[df["Box Office Revenue"] == 0]

print("Number of movies with zero revenue:", len(zero_revenue))

print("\nMovies with zero revenue:\n")

print(
    zero_revenue[
        ["Movie Title", "Budget (Cr)", "Box Office Revenue"]
    ]
)



# ------------------------------------------------------------
# 12. INVESTIGATE SUCCESS RATES
# ------------------------------------------------------------

print("\n========== SUCCESS RATE INVESTIGATION ==========\n")

print(
    "Director Success Rate = 0:",
    (df["Director Success Rate"] == 0).sum()
)

print(
    "Lead Actor Success Rate = 0:",
    (df["Lead Actor Success Rate"] == 0).sum()
)

print("\nMovies with zero Director Success Rate:\n")

print(
    df[df["Director Success Rate"] == 0][
        ["Movie Title", "Director Success Rate"]
    ]
)



# ------------------------------------------------------------
# 13. GENRE INVESTIGATION
# ------------------------------------------------------------

print("\n========== GENRE INVESTIGATION ==========\n")

print("Number of unique genres:", df["Genre"].nunique())

print("\nGenre values:\n")

print(df["Genre"].value_counts())

# ------------------------------------------------------------
# INVESTIGATE MAYA IMDb VALUE
# ------------------------------------------------------------

print("\n========== MAYA INVESTIGATION ==========\n")

print(
    df[df["Movie Title"].str.lower() == "maya"][
        ["Movie Title", "Genre", "IMDb", "Budget (Cr)",
         "Box Office Revenue"]
    ]
)