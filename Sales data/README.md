# Sales Data Analysis and Visualization  

## **Overview**  
This project involves the analysis and visualization of a large sales dataset to uncover patterns, trends, and actionable insights. The dataset includes over 113,000 transactions, spanning multiple years, countries, and product categories. Through data analysis and visualization, this project aims to provide insights into sales performance, customer demographics, and product profitability.

---

## **Table of Contents**  
- [Overview](#overview)  
- [Dataset Description](#dataset-description)  
- [Analysis and Visualizations](#analysis-and-visualizations)  
- [Tools and Techniques](#tools-and-techniques)  
- [Results and Findings](#results-and-findings)  
- [Repository Contents](#repository-contents)  
- [How to Run](#how-to-run)  
- [Installation](#installation)  
- [Examples of Visualizations](#examples-of-visualizations)  
- [Contributing](#contributing)  
- [License](#license)  

---

## **Dataset Description**  
This dataset contains detailed information on sales transactions. Key columns include:  
- **Date**: Transaction date  
- **Customer_Age**: Age of the customer  
- **Age_Group**: Customer age group  
- **Customer_Gender**: Gender of the customer  
- **Country** and **State**: Geographic information  
- **Product_Category** and **Sub_Category**: Product classifications  
- **Order_Quantity**: Quantity of items sold  
- **Unit_Cost** and **Unit_Price**: Pricing details  
- **Profit**, **Cost**, and **Revenue**: Financial information  

---

## **Analysis and Visualizations**  
Key analyses and visualizations include:  
- **Sales Trends**: Analyzing sales and profit over time (monthly, yearly).
  ![Total Profit by Year](https://github.com/user-attachments/assets/6c833e7b-40de-4434-9329-d87a4fdd7aac)
  ![Monthly Profits in 2011](https://github.com/user-attachments/assets/b5f5e905-244e-430e-b760-99c17a57f1cd)
  ![Monthly Profits in 2012](https://github.com/user-attachments/assets/dfbf12b0-f43a-4779-8af6-5e7fef3e15eb)
![Monthly Profits in 2013](https://github.com/user-attachments/assets/056320f8-37de-4ed4-a372-03148b9ff522)
![Monthly Profits in 2014](https://github.com/user-attachments/assets/0ecae7e2-45a6-4cc0-b559-ff58ddb786e7)
![Monthly Profits in 2015](https://github.com/user-attachments/assets/b11993ba-51c7-4586-9764-d363f79d7d69)
![Monthly Profits in 2016](https://github.com/user-attachments/assets/dd145001-32ba-4a48-b40d-3b7f40db7c79)
- **Demographic Insights**: Visualizing sales distribution by age group, gender, and geography.
![Average Revenue by Customer Gender](https://github.com/user-attachments/assets/28660098-01d7-4544-8cbe-24261915d61e)

![Average Order Quantity by Age Group](https://github.com/user-attachments/assets/26ce7681-9a13-49fd-ba9c-00a03d6ae2a4)

- **Product Performance**: Identifying top-selling and high-profit products.  ![Profit Distribution by Product](https://github.com/user-attachments/assets/3d12d5d8-1aaf-400a-b0f3-82c479fec494)
![Profit Distribution by State](https://github.com/user-attachments/assets/9e5e247b-3990-4f37-b8be-5afcff3c85b8)
![Profit Distribution by Product](https://github.com/user-attachments/assets/3d12d5d8-1aaf-400a-b0f3-82c479fec494)
![Profit Distribution by State](https://github.com/user-attachments/assets/9e5e247b-3990-4f37-b8be-5afcff3c85b8)
![Average Unit Cost per Sub Category](https://github.com/user-attachments/assets/c7fd13da-85b2-497a-a82b-faccd68faf1f)
![Cost by Product Category and Year](https://github.com/user-attachments/assets/8fbda488-f09d-49ac-8f9d-d7074044a3d4)

- **Profitability Analysis**: Assessing profit margins across categories and regions.  
![Revenue by Product Category and Year](https://github.com/user-attachments/assets/139683ee-0ffc-4c50-ae46-bf52f43dcdf7)
![Average Revenue per State](https://github.com/user-attachments/assets/cf94b877-25f6-4de4-a1fa-53f0b1cbd7e9)

---

## **Tools and Techniques**  
- **Python**: Pandas, NumPy for data analysis  
- **Visualization**: Matplotlib, Seaborn, Plotly for charts and graphs
- **Excel**: for Data cleaning
- **Jupyter Notebooks**: For step-by-step analysis and insights  

---

## **Results and Findings**  
Through analysis, the following trends were identified:  
- Senior customers (64+) account for a significant portion of sales in certain regions.
- Australia provide more revenue in the company.
- In some years (2014 & 2016), the were no sales for other months.
- **Accessories** and **Clothing** categories showed strong profitability.  
- Seasonal sales fluctuations were observed, with certain products peaking at different times of the year.  

These insights can guide future product development, marketing, and sales strategies.  

---

## **Repository Contents**  
- `data/`: Contains the raw and cleaned datasets.  
- `notebooks/`: Jupyter notebooks with detailed analysis and visualizations.  
- `visualizations/`: Saved images of charts and graphs.  
- `dashboard/`: (If applicable) Files for interactive dashboards (e.g., Tableau, Dash).  

---

## **Installation**  
To set up and run the analysis locally, follow these steps:  
1. Clone the repository:  
   ```bash  
   git clone https://github.com/yourusername/sales-data-analysis.git  
   cd sales-data-analysis  
