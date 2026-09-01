USE FinancialAnalyticsDB;
GO
------1. DATA PROFILING----------------
SELECT TOP 10 *
FROM dbo.IoT_Financial_Management_Dataset;

SELECT COUNT(*) AS TotalRows
FROM dbo.IoT_Financial_Management_Dataset;

------Checking Duplicate transactions--------
SELECT
    Transaction_ID,
    COUNT(*) AS RecordCount
FROM dbo.IoT_Financial_Management_Dataset
GROUP BY Transaction_ID
HAVING COUNT(*) > 1;

--------Chceck missing values-----------
SELECT
    SUM(CASE WHEN Transaction_ID IS NULL THEN 1 ELSE 0 END) AS Missing_Transaction_ID,
    SUM(CASE WHEN Revenue IS NULL THEN 1 ELSE 0 END) AS Missing_Revenue,
    SUM(CASE WHEN Net_Profit IS NULL THEN 1 ELSE 0 END) AS Missing_Net_Profit,
    SUM(CASE WHEN Operating_Cost IS NULL THEN 1 ELSE 0 END) AS Missing_Operating_Cost,
    SUM(CASE WHEN Gross_Margin IS NULL THEN 1 ELSE 0 END) AS Missing_Gross_Margin,
    SUM(CASE WHEN ROI IS NULL THEN 1 ELSE 0 END) AS Missing_ROI,
    SUM(CASE WHEN EBITDA IS NULL THEN 1 ELSE 0 END) AS Missing_EBITDA,
    SUM(CASE WHEN Network_Latency_ms IS NULL THEN 1 ELSE 0 END) AS Missing_Network_Latency
FROM dbo.IoT_Financial_Management_Dataset;

-------Check financial ranges----------
SELECT
    COUNT(*) AS Total_Records,
    SUM(CASE 
        WHEN Network_Latency_ms IS NULL THEN 1 
        ELSE 0 
    END) AS Missing_Records,
    CAST(
        100.0 * SUM(CASE 
            WHEN Network_Latency_ms IS NULL THEN 1 
            ELSE 0 
        END) / COUNT(*) 
        AS DECIMAL(5,2)
    ) AS Missing_Percentage
FROM dbo.IoT_Financial_Management_Dataset;

SELECT *
FROM dbo.IoT_Financial_Management_Dataset
WHERE Network_Latency_ms IS NULL;
SELECT
    Transaction_ID,
    COUNT(*) AS RecordCount
FROM dbo.IoT_Financial_Management_Dataset
GROUP BY Transaction_ID
HAVING COUNT(*) > 1;

SELECT
    Transaction_ID,
    COUNT(*) AS RecordCount
FROM dbo.IoT_Financial_Management_Dataset
GROUP BY Transaction_ID
HAVING COUNT(*) > 1;

SELECT *
FROM dbo.IoT_Financial_Management_Dataset
WHERE Network_Latency_ms < 0
   OR ERP_Response_Time_ms < 0
   OR Transaction_Processing_Time_ms < 0
   OR Cloud_Sync_Delay_s < 0;

   SELECT
    MIN(Revenue) AS Min_Revenue,
    MAX(Revenue) AS Max_Revenue,
    AVG(Revenue) AS Avg_Revenue,
    
    MIN(Net_Profit) AS Min_Net_Profit,
    MAX(Net_Profit) AS Max_Net_Profit,
    AVG(Net_Profit) AS Avg_Net_Profit,
    
    MIN(Operating_Cost) AS Min_Operating_Cost,
    MAX(Operating_Cost) AS Max_Operating_Cost,
    AVG(Operating_Cost) AS Avg_Operating_Cost,
    
    MIN(ROI) AS Min_ROI,
    MAX(ROI) AS Max_ROI,
    AVG(ROI) AS Avg_ROI
FROM dbo.IoT_Financial_Management_Dataset;

SELECT DISTINCT Region
FROM dbo.IoT_Financial_Management_Dataset
ORDER BY Region;

SELECT DISTINCT Department
FROM dbo.IoT_Financial_Management_Dataset
ORDER BY Department;

SELECT *
FROM dbo.IoT_Financial_Management_Dataset
WHERE Network_Latency_ms IS NULL;

USE FinancialAnalyticsDB;
GO

-----------2. DATA CLEANING-------------
SELECT *
INTO dbo.FinancialData_Clean
FROM dbo.IoT_Financial_Management_Dataset;

SELECT COUNT(*) AS TotalRows
FROM dbo.FinancialData_Clean;

SELECT DISTINCT
    PERCENTILE_CONT(0.5)
    WITHIN GROUP (ORDER BY Network_Latency_ms)
    OVER () AS Median_Network_Latency
FROM dbo.FinancialData_Clean
WHERE Network_Latency_ms IS NOT NULL;

USE FinancialAnalyticsDB;
GO

SELECT 
    (SELECT COUNT(*) 
     FROM dbo.IoT_Financial_Management_Dataset) AS Raw_Rows,

    (SELECT COUNT(*) 
     FROM dbo.FinancialData_Clean) AS Clean_Rows;
---------------3. DATA VALIDATION---------------------    
SELECT COUNT(*) AS Missing_Network_Latency
FROM dbo.FinancialData_Clean
WHERE Network_Latency_ms IS NULL;

SELECT DISTINCT
    PERCENTILE_CONT(0.5)
    WITHIN GROUP (ORDER BY Network_Latency_ms)
    OVER () AS Median_Network_Latency
FROM dbo.FinancialData_Clean
WHERE Network_Latency_ms IS NOT NULL;

UPDATE dbo.FinancialData_Clean
SET Network_Latency_ms = 34.9799995422363
WHERE Network_Latency_ms IS NULL;

SELECT COUNT(*) AS Missing_Network_Latency
FROM dbo.FinancialData_Clean
WHERE Network_Latency_ms IS NULL;

SELECT
    Transaction_ID,
    Network_Latency_ms,
    ERP_Response_Time_ms,
    Transaction_Processing_Time_ms,
    Cloud_Sync_Delay_s
FROM dbo.FinancialData_Clean
WHERE Network_Latency_ms < 0
   OR ERP_Response_Time_ms < 0
   OR Transaction_Processing_Time_ms < 0
   OR Cloud_Sync_Delay_s < 0;

SELECT
    SUM(CASE WHEN Network_Latency_ms < 0 THEN 1 ELSE 0 END) AS Negative_Network_Latency,
    SUM(CASE WHEN ERP_Response_Time_ms < 0 THEN 1 ELSE 0 END) AS Negative_ERP_Response,
    SUM(CASE WHEN Transaction_Processing_Time_ms < 0 THEN 1 ELSE 0 END) AS Negative_Transaction_Time,
    SUM(CASE WHEN Cloud_Sync_Delay_s < 0 THEN 1 ELSE 0 END) AS Negative_Cloud_Sync
FROM dbo.FinancialData_Clean;

-------Categorised data cleanings----
SELECT
    Region,
    COUNT(*) AS Record_Count
FROM dbo.FinancialData_Clean
GROUP BY Region
ORDER BY Region;

SELECT
    Department,
    COUNT(*) AS Record_Count
FROM dbo.FinancialData_Clean
GROUP BY Department
ORDER BY Department;

SELECT
    COLUMN_NAME,
    DATA_TYPE
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_NAME = 'FinancialData_Clean'
ORDER BY ORDINAL_POSITION;
---------------------4. EXPLORATORY DATA ANALYSIS-------------------------------
SELECT
    COUNT(*) AS Total_Transactions,
    ROUND(SUM(Revenue), 2) AS Total_Revenue,
    ROUND(SUM(Operating_Cost), 2) AS Total_Operating_Cost,
    ROUND(SUM(Net_Profit), 2) AS Total_Net_Profit,
    ROUND(AVG(Gross_Margin), 2) AS Avg_Gross_Margin,
    ROUND(AVG(ROI), 2) AS Avg_ROI,
    ROUND(SUM(EBITDA), 2) AS Total_EBITDA
FROM dbo.FinancialData_Clean;

SELECT
    Region,
    COUNT(*) AS Total_Transactions,
    ROUND(SUM(Revenue), 2) AS Total_Revenue,
    ROUND(SUM(Operating_Cost), 2) AS Total_Operating_Cost,
    ROUND(SUM(Net_Profit), 2) AS Total_Net_Profit,
    ROUND(AVG(ROI), 2) AS Avg_ROI
FROM dbo.FinancialData_Clean
GROUP BY Region
ORDER BY Total_Net_Profit DESC;

SELECT
    Department,
    COUNT(*) AS Total_Transactions,
    ROUND(SUM(Revenue), 2) AS Total_Revenue,
    ROUND(SUM(Operating_Cost), 2) AS Total_Operating_Cost,
    ROUND(SUM(Net_Profit), 2) AS Total_Net_Profit,
    ROUND(AVG(Gross_Margin), 2) AS Avg_Gross_Margin,
    ROUND(AVG(ROI), 2) AS Avg_ROI
FROM dbo.FinancialData_Clean
GROUP BY Department
ORDER BY Total_Net_Profit DESC;

SELECT
    Region,
    ROUND(SUM(Revenue), 2) AS Total_Revenue,
    ROUND(SUM(Net_Profit), 2) AS Total_Net_Profit,
    ROUND(
        SUM(Net_Profit) * 100.0 / NULLIF(SUM(Revenue), 0),
        2
    ) AS Profit_Margin_Percentage
FROM dbo.FinancialData_Clean
GROUP BY Region
ORDER BY Profit_Margin_Percentage DESC;
-----------------------5. ADVANCED ANALYSIS-------------------------
WITH RegionalPerformance AS
(
    SELECT
        Region,
        SUM(Revenue) AS Total_Revenue,
        SUM(Net_Profit) AS Total_Net_Profit
    FROM dbo.FinancialData_Clean
    GROUP BY Region
)

SELECT
    Region,
    ROUND(Total_Revenue, 2) AS Total_Revenue,
    ROUND(Total_Net_Profit, 2) AS Total_Net_Profit,

    RANK() OVER (
        ORDER BY Total_Net_Profit DESC
    ) AS Profit_Rank

FROM RegionalPerformance
ORDER BY Profit_Rank;

------Find high-revenue----------
WITH RegionalPerformance AS
(
    SELECT
        Region,
        SUM(Revenue) AS Total_Revenue,
        SUM(Net_Profit) AS Total_Net_Profit,
        SUM(Operating_Cost) AS Total_Operating_Cost,
        SUM(Net_Profit) * 100.0 /
            NULLIF(SUM(Revenue), 0) AS Profit_Margin
    FROM dbo.FinancialData_Clean
    GROUP BY Region
)

SELECT
    Region,
    ROUND(Total_Revenue, 2) AS Total_Revenue,
    ROUND(Total_Operating_Cost, 2) AS Total_Operating_Cost,
    ROUND(Total_Net_Profit, 2) AS Total_Net_Profit,
    ROUND(Profit_Margin, 2) AS Profit_Margin
FROM RegionalPerformance
ORDER BY Profit_Margin DESC;

--------------Analyse department performance within each region--------------------------
SELECT
    Region,
    Department,
    COUNT(*) AS Total_Transactions,
    ROUND(SUM(Revenue), 2) AS Total_Revenue,
    ROUND(SUM(Operating_Cost), 2) AS Total_Operating_Cost,
    ROUND(SUM(Net_Profit), 2) AS Total_Net_Profit,
    ROUND(
        SUM(Net_Profit) * 100.0 /
        NULLIF(SUM(Revenue), 0),
        2
    ) AS Profit_Margin
FROM dbo.FinancialData_Clean
GROUP BY Region, Department
ORDER BY Region, Total_Net_Profit DESC;

--------------Analyse ROI by department-----------------
SELECT
    Department,
    ROUND(AVG(ROI), 2) AS Avg_ROI,
    ROUND(MIN(ROI), 2) AS Min_ROI,
    ROUND(MAX(ROI), 2) AS Max_ROI,
    ROUND(AVG(Gross_Margin), 2) AS Avg_Gross_Margin
FROM dbo.FinancialData_Clean
GROUP BY Department
ORDER BY Avg_ROI DESC;