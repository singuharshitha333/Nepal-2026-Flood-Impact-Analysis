# Nepal 2026 Flood Impact Analysis

## Project Overview

This project analyzes the impact of the **25–26 August 2026 Nepal flood/mudflow event** in **Syapru Besi, Rasuwa, Nepal**, using satellite-based damage assessment data from the **Copernicus Emergency Management Service (CEMS)**.

The analysis focuses on buildings, transportation infrastructure, land use, and facilities within the selected Area of Interest (AOI).

The project demonstrates an end-to-end data analytics workflow:

**Raw data → Excel data cleaning → SQL analysis → Python EDA & visualization → Interactive-style Excel dashboard → Insights**

---

## Objectives

* Assess the extent of building damage within the AOI.
* Compare residential and non-residential building impacts.
* Quantify affected transportation infrastructure.
* Analyze affected land-use categories.
* Identify affected facilities.
* Calculate key impact percentages and summarize findings through a dashboard.

---

## Tools & Technologies

* **Microsoft Excel** — data cleaning, validation, summaries, and dashboard
* **Microsoft SQL Server / SSMS** — data storage and SQL analysis
* **Python** — exploratory data analysis and visualization
* **Pandas** — data manipulation
* **Matplotlib** — visualization

---

## Data Source

**Copernicus Emergency Management Service (CEMS)**

Event: Nepal flood/mudflow, August 2026
Product: **EMSR927 – AOI 01 Syapru Besi, Rasuwa**

The original source workbook was preserved, while separate analytical tables were created for cleaning and analysis.

---

## Key Findings

### Building Impact

* **559 buildings** were represented within the AOI.
* **433 buildings** were classified as affected.
* Overall building affected rate: **77.46%**.
* **323 buildings** were classified as destroyed.
* **78 buildings** were classified as possibly damaged.
* **32 buildings** were classified as damaged.
* **126 buildings** had no visible damage.

### Residential vs Non-Residential

| Asset Type      | Total Buildings | Affected | Affected Rate |
| --------------- | --------------: | -------: | ------------: |
| Residential     |             517 |      392 |        75.82% |
| Non-residential |              42 |       41 |        97.62% |

### Transportation Impact

| Transportation Type       | Affected | Unit  |
| ------------------------- | -------: | ----- |
| Primary Road              |      5.4 | km    |
| Local Road                |      1.1 | km    |
| Cart Track                |      1.1 | km    |
| Bridges/elevated highways |        5 | count |
| Helipad                   |     0.01 | ha    |

### Land Use Impact

A total of **111.0 hectares** of the represented land-use area was affected.

| Land Use                   | Affected Area | Total Area | Affected Rate |
| -------------------------- | ------------: | ---------: | ------------: |
| Forests                    |       61.6 ha |   228.8 ha |        26.92% |
| Shrub/herbaceous           |       31.8 ha |    93.1 ha |        34.16% |
| Inland wetlands            |       12.1 ha |    14.6 ha |        82.88% |
| Other                      |        3.4 ha |     4.3 ha |        79.07% |
| Heterogeneous agricultural |        2.1 ha |     5.1 ha |        41.18% |

### Facilities

* **0.8 hectares** of power plant construction area was affected.

---

## Project Structure

```text
Nepal-Flood-Impact-Analysis/
│
├── data/
│   └── nepal_flood_cleaned.xlsx.xlsx
│
├── sql/
│   └── analysis.sql
│
├── python/
│   └── eda.py
│
├── visualizations/
│   ├── building_damage_status.png
│   ├── affected_buildings_by_asset_type.png
│   ├── transportation_impact.png
│   ├── landuse_impact.png
│   ├── transportation_affected_percentage.png
│   └── landuse_affected_area.png
│
└── README.md
```

---

## Analytical Workflow

### 1. Excel

* Reviewed the original CEMS workbook.
* Preserved original source sheets.
* Created cleaned analytical tables.
* Validated building, transportation, land-use, and facility data.
* Created project summaries and an Excel dashboard.

### 2. SQL Server

Loaded the cleaned analytical tables into SQL Server and performed analysis including:

* Building damage status analysis.
* Residential vs non-residential impact.
* Transportation impact percentages.
* Land-use affected percentages.
* Overall impact summaries.

### 3. Python

Used Pandas to load and analyze the cleaned Excel tables.

Python calculations included:

* Damage-status aggregation.
* Asset-type impact rates.
* Transportation affected percentages.
* Land-use affected percentages.
* Overall affected land calculations.

Matplotlib was used to create six visualizations.

---

## Dashboard

The Excel dashboard summarizes the analysis using:

* Building status
* Building impact by asset type
* Transportation impact
* Transportation affected percentage
* Land-use impact
* Land-use affected area
* Key project KPIs

---

## Data Quality Note

The analysis uses satellite-based damage assessment data from the CEMS rapid mapping product. Damage classifications represent mapped observations within the specified AOI and should not be interpreted as a complete ground-survey inventory.

---

## Skills Demonstrated

**Data Analysis:** Data cleaning, validation, aggregation, percentage calculations, exploratory analysis

**Excel:** Data preparation, analytical tables, formulas, dashboard design

**SQL:** Database creation, table design, aggregation, grouping, filtering, analytical queries

**Python:** Pandas, Matplotlib, EDA, data transformation, visualization

**Data Storytelling:** KPI development, dashboard design, interpretation of infrastructure and environmental impacts
