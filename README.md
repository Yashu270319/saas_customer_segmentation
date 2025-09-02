# SaaS Customer Segmentation Using KMeans

A complete end-to-end Data Science project that simulates a real-world SaaS company scenario. The project performs the entire data pipeline (ETL) and applies KMeans clustering to segment customers based on behavior, engagement, and usage metrics.

> This project demonstrates the practical, job-ready skills expected of a Data Analyst or Data Scientist.

---

## Project Overview

- Industry: SaaS / Data-Driven Businesses
- Type: Unsupervised Learning (Clustering)
- Tech Stack: Python, Pandas, Scikit-learn, Matplotlib, Seaborn
- Goal: Identify customer segments to support business decisions in product, marketing, and support.

---

## Problem Statement

SaaS companies handle large volumes of behavioral customer data. Understanding user segments can help:
- Target high-risk churners
- Optimize pricing tiers
- Improve support for high-value users

---

## Pipeline Breakdown

| Step | Description | File |
|------|-------------|------|
| Data Generation | Creates mock SaaS customer data | generate_mock_data.py |
| Extract | Reads the raw CSV | etl/extract.py |
| Transform | Cleans & engineers new features | etl/transform.py |
| Load | Saves the transformed dataset | etl/load.py |
| Clustering | KMeans segmentation (4 clusters) | ml/clustering.py |
| Visualization | 2D PCA cluster plot | visualize/plot_clusters.py |
| Runner | Runs full pipeline | main.py |

---

## Folder Structure

`bash
saas_customer_segmentation/
│
├── data/
│   ├── raw_customers.csv
│   ├── processed_customers.csv
│   └── cluster_plot.png
│
├── etl/
│   ├── extract.py
│   ├── transform.py
│   └── load.py
│
├── ml/
│   └── clustering.py
│
├── visualize/
│   └── plot_clusters.py
│
├── utils/
│   └── (optional helpers)
│
├── generate_mock_data.py
├── main.py
├── requirements.txt
└── README.md
