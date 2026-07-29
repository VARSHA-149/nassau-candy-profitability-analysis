# Nassau Candy Distributor Analytics Project

## Overview
This repository contains an end-to-end data analysis and web application platform for **Nassau Candy Distributor**. It provides data processing workflows, executive analytics, automated report generation, and an interactive Streamlit web application.

---

## Directory Structure
```
Nassau_Candy_Project
│
├── data
│   └── Nassau Candy Distributor.csv
│
├── notebooks
│   └── exploratory_analysis.ipynb
│
├── app.py
│
├── analysis.py
│
├── requirements.txt
│
├── report.docx
│
└── README.md
```

---

## Component Description

- **`data/Nassau Candy Distributor.csv`**: Core dataset containing sales records, division details, product names, profit margins, cost, unit counts, and customer geographies.
- **`notebooks/exploratory_analysis.ipynb`**: Jupyter notebook for exploratory data analysis (EDA), trend modeling, and statistical visualizations.
- **`app.py`**: Streamlit interactive dashboard with glassmorphism UI, KPI counters, division comparison charts, regional distribution maps, and date/division filters.
- **`analysis.py`**: Business logic and data transformation layer providing KPI aggregation, regional analytics, and division performance functions.
- **`requirements.txt`**: List of dependencies required to run the project.
- **`report.docx`**: Formatted Microsoft Word executive report containing executive summary metrics, division breakdown tables, and top-performing products.
- **`README.md`**: Project documentation and quickstart instructions.

---

## Setup & Running the Application

### 1. Install Dependencies
```bash
python3 -m pip install -r requirements.txt
```

### 2. Launch Interactive Dashboard
```bash
streamlit run app.py
```

### 3. Generate Executive Word Report
```bash
python3 generate_report.py
```
