# Automated Data Quality Monitoring System

## 1. System Overview

The Automated Data Quality Monitoring System is a web-based application that analyzes datasets and identifies data quality issues.

The system validates uploaded datasets and generates quality metrics, reports, and an overall quality score.

---

## 2. System Flow

User Uploads CSV
↓
Data Ingestion Module
↓
Validation Engine
├── Missing Value Checker
├── Duplicate Checker
├── Outlier Checker
└── Schema Validator
↓
Quality Score Engine
↓
Database Storage
↓
Dashboard & Reports

---

## 3. Validation Modules

### Missing Value Checker

Purpose:
Identify null or missing values in the dataset.

Output:

* Missing value count
* Missing value rate
* Column-wise missing statistics

---

### Duplicate Checker

Purpose:
Identify duplicate records.

Output:

* Duplicate row count
* Duplicate rate

---

### Outlier Checker

Purpose:
Detect abnormal values using the IQR method.

Output:

* Outlier count
* Outlier rate
* Affected columns

---

### Schema Validator

Purpose:
Compare uploaded dataset structure against expected schema.

Checks:

* Missing columns
* Extra columns
* Data type mismatches

---

## 4. Standard Validation Output Format

All validation modules return data in a standardized format.

Example:

{
"status": "PASS",
"issue_count": 0,
"details": {}
}

or

{
"status": "FAIL",
"issue_count": 2,
"details": {
"customer_id": 1,
"amount": 1
}
}

---

## 5. Quality Score Design

Quality score starts at 100.

The score is based on issue percentages rather than absolute issue counts.

Metrics:

1. Missing Value Rate
   = Missing Cells / Total Cells × 100

2. Duplicate Rate
   = Duplicate Rows / Total Rows × 100

3. Outlier Rate
   = Outlier Rows / Total Rows × 100

Schema validation is treated separately.

The final quality score is calculated using the issue rates.

---

## 6. Quality Status Categories

Excellent : Score >= 95

Good : Score >= 85

Warning : Score >= 70

Critical : Score < 70

---

## 7. Configuration Management

Application settings are stored in config.py.

Examples:

* Database name
* Quality thresholds
* Validation thresholds
* Schema validation settings

This allows business rules to be modified without changing application logic.

---

## 8. Future Enhancements

* Email alerts
* Scheduled scans
* PDF reports
* Historical trend analysis
* API data ingestion
* Multi-user support
* Cloud deployment




## Implementation Progress

### Day -3 Completed

- Missing Value Checker

Features:
- Detects missing values using Pandas
- Returns standardized response format
- Provides column-wise missing value statistics

Example Output:

{
    "status": "FAIL",
    "issue_count": 2,
    "details": {
        "customer_id": 1,
        "amount": 1
    }
}