# 📊 Supply Chain Risk & Logistics Analytics (End-to-End BI Project)

## 📌 Overview

This project demonstrates an end-to-end Business Intelligence pipeline for analyzing global supply chain performance and risks. It covers data engineering, data modeling, SQL analytics, and dashboard development using Power BI.

The goal is to transform raw logistics data into actionable insights that support decision-making in supply chain operations.

---

## ⚙️ Tech Stack

* **Python** (Pandas, psycopg2) → ETL Pipeline
* **PostgreSQL** → Data Warehouse (Star Schema)
* **SQL** → Analytics Layer (Views)
* **Power BI** → Dashboard & Visualization
* **Git/GitHub** → Version Control

---

## 🏗️ Architecture

### 1. Data Ingestion

* Raw dataset: `global_supply_chain_risk_2026.csv`
* Loaded and processed using a Python ETL pipeline

### 2. Data Warehouse (PostgreSQL)

A structured **star schema** was implemented:

* **Fact Table**

  * `fact_shipments` (lead time, disruptions, risk score, etc.)

* **Dimension Tables**

  * `dim_date`
  * `dim_port`
  * `dim_product_category`
  * `dim_transport_mode`
  * `dim_weather`

---

## 🔄 ETL Pipeline

Implemented in:

```text
src/etl_pipeline.py
```

Key steps:

* Data cleaning & transformation
* Handling missing values
* Mapping surrogate keys
* Loading into PostgreSQL warehouse

---

## 🧠 Analytics Layer (SQL Views)

To support BI analysis, an **analytics schema** was created:

```text
analytics
```

Key views:

* `v_kpi_overview` → core KPIs
* `v_shipments_by_month` → trend analysis
* `v_lead_time_by_product` → product performance
* `v_lead_time_by_transport` → transport efficiency
* `v_weather_disruptions` → disruption analysis
* `v_risk_by_product` → risk vs performance
* `v_reliability_analysis` → carrier performance

👉 These views separate **data modeling** from **business logic**, following best practices.

---

## 📊 Power BI Dashboard

The dashboard provides a comprehensive overview of supply chain performance.

### 🔑 Key Metrics

* Average Lead Time
* Total Shipments
* Total Disruptions
* Average Reliability

---

### 📈 Visualizations

#### 1. Time Analysis

* Shipments by month → identifies trends and seasonality

#### 2. Product Analysis

* Lead time by product category → performance comparison

#### 3. Transport Analysis

* Delivery performance by transport mode

#### 4. Risk Analysis

* Scatter plot: **Geopolitical Risk vs Lead Time**
* Identifies how risk impacts delivery performance

#### 5. Carrier Performance

* Scatter plot: **Reliability vs Lead Time**
* Shows correlation between reliability and efficiency

#### 6. Disruptions

* Weather-related disruptions analysis

#### 7. Bottlenecks

* Lead time by port → identifies slow logistics hubs

---

## 📊 Key Insights

* Higher geopolitical risk is associated with increased delivery times
* Low carrier reliability leads to longer lead times
* Certain product categories show higher risk exposure
* Weather conditions significantly impact disruptions
* Some ports consistently have higher lead times (potential bottlenecks)

---

## 📁 Project Structure

```text
supply_chain/
│
├── data/
│   └── raw/
│       └── global_supply_chain_risk_2026.csv
│
├── notebooks/
│   ├── eda_supply_chain.ipynb
│   └── supply_chain_analysis.ipynb
│
├── sql/
│   ├── dashboard_queries/
│   └── views/
│
├── src/
│   ├── etl_pipeline.py
│   ├── data_access.py
│   ├── query_loader.py
│   └── run_analysis.py
│
├── dashboard/
│   └── supply_chain_dashboard.pbix
│
├── assets/
│   └── dashboard_overview.png
│
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 🔐 Environment Setup

Create a `.env` file:

```text
DB_HOST=localhost
DB_NAME=supply_chain
DB_USER=postgres
DB_PASSWORD=your_password
```

---

## ▶️ How to Run

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Run ETL pipeline

```bash
python src/etl_pipeline.py
```

### 3. Connect Power BI

* Connect to PostgreSQL
* Use `analytics` schema
* Load views

---

## 🚀 Key Learnings

* Designing a **data warehouse (star schema)**
* Building **ETL pipelines with Python**
* Creating **SQL-based analytics layers**
* Developing **interactive BI dashboards**
* Translating data into **business insights**

---

## 📬 Conclusion

This project demonstrates how raw data can be transformed into meaningful insights through a structured BI pipeline. It highlights both technical and analytical skills required for modern data-driven decision-making.

---
