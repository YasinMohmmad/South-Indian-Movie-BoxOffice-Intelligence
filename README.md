# South Indian Movie Box Office & Revenue Intelligence Dashboard

## 📌 Project Overview

This project analyzes movie performance using budget, box-office
revenue, profitability, ROI, IMDb ratings, genre, director success rate,
lead-actor success rate, trailer views, and Hit/Flop classification.

The project demonstrates an end-to-end data analytics workflow using
**Python/Pandas, MySQL, Excel, and Power BI**.

## 🎯 Business Objectives

The analysis is designed to answer key business questions:

-   Which genres generate the highest revenue and profit?
-   Does a higher movie budget guarantee commercial success?
-   How are director and lead-actor success rates associated with
    revenue?
-   Do trailer views indicate stronger box-office performance?
-   Which movies generate the highest absolute profit?
-   How does ROI vary across genres and budget levels?
-   What financial and data-quality risks should be considered when
    reporting movie performance?

## 🛠️ Technology Stack

  Tool              Purpose
  ----------------- -------------------------------------------------
  Python / Pandas   Data inspection, cleaning and transformation
  MySQL             Relational database and analytical SQL
  Excel             SQL-style output analysis and reporting
  Power BI          Interactive dashboard and business intelligence
  Git / GitHub      Version control and portfolio publishing

## 📂 Project Structure

``` text
Movie_BoxOffice_Intelligence/
│
├── 01_Raw_Data/
│   └── imdb_movies.csv
│
├── 02_Python/
│   ├── 01_data_inspection.py
│   ├── 02_data_cleaning.py
│   └── 03_load_mysql.py
│
├── 03_Clean_Data/
│   └── movies_clean.csv
│
├── 04_SQL/
│   ├── database_setup.sql
│   └── queries.sql
│
├── 05_Excel/
│   └── sql_outputs.xlsx
│
├── 06_PowerBI/
│   └── South_Indian_Movie_BoxOffice_Dashboard.pbix
│
├── 07_Reports/
│   ├── dashboard_screenshots.pdf
│   ├── data_quality_report.pdf
│   └── strategic_insights_report.docx
│
├── 08_Final_Submission/
│
├── .gitignore
└── README.md
```

> The local Python virtual environment (`.venv`) is intentionally
> excluded from version control.

## 🔄 Data Analytics Workflow

``` text
Raw CSV
   ↓
Python Data Inspection
   ↓
Data Cleaning & Validation
   ↓
Cleaned CSV
   ↓
MySQL Database
   ↓
SQL Analysis
   ↓
Excel Outputs
   ↓
Power BI Dashboard
   ↓
Strategic Insights & Reports
```

## 🧹 Data Cleaning & Quality

The raw dataset contains **560 movie records and 9 source columns**.

Key cleaning and validation steps included:

-   Standardized column names.
-   Converted trailer views to numeric values.
-   Validated IMDb ratings against the expected 0--10 range.
-   Converted the invalid IMDb value of **43.0 for Maya** to missing
    rather than guessing a correction.
-   Retained legitimate low-budget movies because an unusual value is
    not automatically a data error.
-   Retained the zero-revenue record for **The White Tiger** and created
    a revenue-status flag.
-   Retained zero director/actor success rates and created status flags.
-   Calculated profit as:

``` text
Profit = Box Office Revenue - Budget
```

-   Calculated ROI as:

``` text
ROI % = (Profit / Budget) × 100
```

-   Classified movies using:

``` text
Profit > 0 → Hit
Profit ≤ 0 → Flop
```

The cleaned dataset contains **560 rows** with no duplicate rows.

## 🗄️ SQL Analysis

The MySQL analysis covers:

-   Total movies
-   Total revenue
-   Average revenue per movie
-   Total budget
-   Total profit
-   Average profit
-   Top profitable movies
-   Top ROI movies
-   Revenue and profit by genre
-   ROI by genre
-   IMDb performance by genre
-   Hit vs Flop analysis
-   Hit rate by genre
-   Budget vs revenue
-   Director success segments
-   Lead-actor success segments
-   Trailer views analysis
-   Zero-revenue and loss-making movies
-   Data-quality checks

## 📊 Power BI Dashboard

The Power BI dashboard contains three analytical pages.

### Page 1 --- Executive Overview

Provides high-level KPIs and business performance:

-   Total Movies
-   Total Revenue
-   Total Profit
-   Hit Rate
-   Revenue by Genre
-   Hit vs Flop Distribution
-   Budget vs Box Office Revenue

### Page 2 --- Genre & Star Intelligence

Focuses on audience, creative and promotional indicators:

-   Average IMDb Rating by Genre
-   Director Success Rate vs Revenue
-   Lead Actor Success Rate vs Revenue
-   Trailer Views vs Box Office Revenue

### Page 3 --- Profitability & Risk

Focuses on financial performance and investment risk:

-   Top 10 Most Profitable Movies
-   Average Profit by Budget Segment
-   Average ROI by Genre
-   Top 10 Highest-Budget Movies
-   Budget vs Box Office Revenue

## 💡 Key Business Insights

### 1. Action leads absolute revenue

Action generated approximately **₹26,030.58 Cr** in total box-office
revenue and approximately **₹13,307.68 Cr** in total profit, making it
the strongest genre by absolute commercial contribution.

### 2. Higher budget does not guarantee success

Higher-budget movies can generate large revenues and profits, but budget
alone is not a reliable predictor of success. The dataset includes
high-budget movies that generated substantial losses.

### 3. Drama has the highest average IMDb rating

Drama has the highest average IMDb rating at approximately **7.95**.

### 4. Director success is associated with stronger outcomes

Movies in the high director-success segment average approximately
**₹172.87 Cr revenue** and have an **81.19% hit rate**, compared with
approximately **₹25.84 Cr revenue** and a **43.80% hit rate** for the
low-success segment.

### 5. Lead-actor success shows a positive performance pattern

The high lead-actor-success segment averages approximately **₹139.83 Cr
revenue** and an **80.88% hit rate**, compared with approximately
**₹79.56 Cr revenue** and a **56.49% hit rate** for the low-success
segment.

### 6. Trailer views are associated with commercial performance

The highest trailer-view quartile averages approximately **₹234.57 Cr
revenue** and a **75.54% hit rate**, while the lowest-view quartile
averages approximately **₹31.76 Cr revenue** and a **69.29% hit rate**.

This is an association, not proof that trailer views cause higher
revenue.

### 7. ROI can be heavily distorted by tiny budgets

Extremely small budgets can produce very large ROI percentages. For
example, a movie with a very small budget can generate a high percentage
return even when its absolute profit is modest.

Therefore, **ROI should always be interpreted together with absolute
profit and budget**.

## ⚠️ Risk & Governance Recommendations

-   Report Revenue, Profit and ROI together.
-   Do not use budget alone as a success indicator.
-   Flag zero-revenue records for review.
-   Validate financial values and ratings during data refreshes.
-   Review extreme ROI values separately.
-   Preserve data-quality flags instead of silently deleting unusual
    records.
-   Treat relationships between trailer views, success scores and
    revenue as associations rather than causal conclusions.

## 📌 Data Limitation

The current source dataset does **not contain a movie release-year/date
field**.

Therefore, reliable year-over-year revenue analysis and annual revenue
trends could not be performed without introducing unsupported
information. No artificial year values were created.

## 📈 Project Outcome

This project demonstrates an end-to-end analytics pipeline:

**Data → Cleaning → SQL → Excel → Power BI → Business Insights**

It combines technical data-processing skills with business-focused
analysis and data-quality governance.

## 📄 Deliverables

-   `movies_clean.csv` --- cleaned analytical dataset
-   `data_quality_report.pdf` --- data-quality and cleaning report
-   `queries.sql` --- SQL analysis queries
-   `sql_outputs.xlsx` --- analytical SQL outputs
-   `South_Indian_Movie_BoxOffice_Dashboard.pbix` --- Power BI dashboard
-   `dashboard_screenshots.pdf` --- exported dashboard pages
-   `strategic_insights_report.docx` --- strategic business analysis

## 👤 Project Focus

**Domain:** Movie / Entertainment Analytics\
**Analysis Type:** Revenue, Profitability, ROI, Audience & Performance
Intelligence\
**Tools:** Python, Pandas, MySQL, Excel, Power BI, Git, GitHub
