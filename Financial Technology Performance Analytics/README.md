# Financial and Technology Performance Analytics

## Project Overview

This project analyses financial, operational, risk and technology performance using SQL Server and Power BI.

The analysis combines financial metrics such as revenue, net profit, operating costs, EBITDA, profit margin and ROI with operational and technology indicators including system uptime, automation efficiency, ERP response time, network latency, compliance and fraud risk.

The objective is to identify performance patterns across regions and departments and present the findings through an interactive Power BI dashboard.

## Tools Used

- SQL Server
- SQL Server Management Studio (SSMS)
- Power BI
- DAX

## Data Preparation and Cleaning
The dataset was imported into SQL Server and profiled before analysis to assess data quality and identify issues that could affect the results.
The cleaning process included:
- Checking for duplicate transaction records.
- Identifying missing values across key financial and operational fields.
- Detecting invalid negative values in operational metrics.
- Reviewing financial data ranges for unusual values.
- Checking Region and Department categories for consistency.
- Creating a separate cleaned table to preserve the original dataset.
- Replacing missing Network Latency values using the median value.
- Validating the cleaned dataset before performing analysis.

The cleaned dataset was then used for SQL analysis and Power BI visualisation.

## SQL Analysis

SQL Server was used to explore the cleaned dataset and analyse financial performance across regions and departments.

The analysis included:

- Calculating total revenue, net profit, operating costs and EBITDA.
- Measuring average ROI and gross margin.
- Comparing financial performance across regions.
- Comparing revenue, costs and profitability across departments.
- Calculating profit margin by region.
- Ranking regions based on net profit using SQL window functions.
- Analysing department performance within each region.
- Comparing ROI and gross margin across departments.

Advanced SQL techniques including Common Table Expressions (CTEs), aggregate functions, `RANK()` and conditional logic were used during the analysis.

## Power BI Dashboard

An interactive Power BI dashboard was developed using the cleaned SQL dataset. The dashboard consists of three analytical pages.

### 1. Executive Financial Overview

Provides a high-level view of financial performance, including revenue, net profit, operating costs, EBITDA, profit margin and ROI. It also compares performance across regions and departments.

![Executive Financial Overview](Executive%20Financial%20Overview.png)

### 2. Operational and Risk Analysis

Examines operational performance and risk indicators, including automation efficiency, fraud risk, compliance, system uptime, ERP response time and device error rates.

![Operational and Risk Analysis](Operational%20and%20Risk%20Analysis.png)

### 3. Technology and Financial Performance

Explores relationships between technology performance and financial outcomes using metrics such as automation efficiency, network latency, system uptime, ERP response time and net profit.

![Technology and Financial Performance](Technology%20and%20Financial%20Performance.png)

## Key Insights

- Total revenue reached approximately **R4.67 billion**, generating approximately **R1.36 billion in net profit**.
- The overall profit margin was approximately **29.22%**, while average ROI was **18.56%**.
- The **South region** generated the highest net profit, making it the strongest region by overall profit contribution.
- The **East region** achieved the highest profit margin, indicating strong profitability relative to revenue.
- The **West region** recorded the lowest profit margin, highlighting an opportunity for cost and profitability improvement.
- **Audit** generated the highest revenue among departments, while **Investment** generated the highest net profit.
- **Accounts** achieved the highest average ROI.
- Technology and operational indicators were analysed alongside financial performance to identify potential relationships between system performance and profitability.
