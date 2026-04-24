# NAVSEA Submarine Lifecycle Analysis

Submarine lifecycle data analysis using Python (Pandas) and Tableau to clean, structure, and visualize maintenance and operational trends.

---

## Project Overview
This project focuses on transforming raw submarine lifecycle data into structured, analyzable datasets. The goal was to improve data quality and enable clearer insights into maintenance patterns, operational timelines, and lifecycle trends.

---

## My Contributions
- Built Python data cleaning workflows using Pandas
- Standardized inconsistent categorical fields (location, ship class, period type)
- Fixed mixed date formats and corrected invalid records
- Enriched dataset by mapping hull numbers to ship names
- Developed Tableau dashboards for lifecycle visualization

---

## Tech Stack
- Python (Pandas, NumPy)
- Tableau
- Excel

---

## Repository Structure
```text
navsea-submarine-lifecycle-analysis/
│
├── data/
│   ├── submarine_lifecycle_cleaned.csv
│   └── submarine_names.csv
│
├── scripts/
│   ├── clean_data.py
│   └── get_hull_number.py
│
├── dashboards/
│   ├── submarine_dashboard.twb
│   └── Tableau_Dashboards.pdf
│
├── images/
│   └── dashboard_preview.png
│
└── README.md
```

## How to Run

1. Install dependencies:

```bash
pip install pandas numpy
```

2. Run data cleaning script:

```bash
python scripts/clean_data.py
```

## Dashboard Preview
![Line Chart Dashboard](images/Line-Chart-Dashboard.png)
![Gantt Chart Dashboard](images/Gantt-Chart-Dashboard.png)
![Bar Chart Dashboard](images/Bar-Chart-Dashboard.png)
![Scatter Map Chart Dashboard](images/Scatter-Map-Dashboard.png)
