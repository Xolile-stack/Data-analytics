#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 


# In[3]:


df= pd.read_csv('C:/Users/NgcoboXH/Downloads/Sales dataset.CSV')


# In[10]:


df


# In[11]:


print(df.head())


# In[10]:


# calculate the average Country Revenue 
avg__Revenue = df.groupby('Country')['Revenue'].mean()
print(avg__Revenue)

# plotting the data 
plt.figure(figsize=(10,4))
plt.bar(avg__Revenue.index, avg__Revenue.values, color= ['blue'])
plt.title('Average Revenue per Country')
plt.xlabel('Country')
plt.ylabel('Revenue ($)')

plt.show()


# In[11]:


avg__Order_Quantity = df.groupby('Age_Group')['Order_Quantity'].mean()
print(avg__Order_Quantity)


# In[15]:


#plotting that data (pie chart)
labels = avg__Order_Quantity.index
values = avg__Order_Quantity.values

plt.figure(figsize=(4, 4))
plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=90)
plt.title('Average Order Quantity by Age Group')
plt.show()


# In[16]:


# Converting Date column to datetime and extract the year
df['Date'] = pd.to_datetime(df['Date'])
df['Year'] = df['Date'].dt.year

df['Date'] = pd.to_datetime(df['Date'])
df['Year'] = df['Date'].dt.year

# Group by Year and sum up profits
yearly_profit = df.groupby('Year')['Profit'].sum()

max_profit_year = yearly_profit.idxmax()
max_profit_value = yearly_profit.max()

print(f"Year with greatest profit: {max_profit_year} with profit of {max_profit_value}")

print(yearly_profit)


# In[19]:


yearly_profit.plot(kind='bar', color='orange', figsize=(6, 4))
plt.title('Total Profit by Year')
plt.xlabel('Year')
plt.ylabel('Total Profit')
plt.xticks(rotation=0)
plt.show()


# In[20]:


# Finding which month has made a lot of profit 
df['Date'] = pd.to_datetime(df['Date'])

df_2011 = df[df['Date'].dt.year == 2011]
df_2011['Month'] = df_2011['Date'].dt.month
monthly_profit_2011 = df_2011.groupby('Month')['Profit'].sum()

max_profit_month = monthly_profit_2011.idxmax()
max_profit_value = monthly_profit_2011.max()

print(f"Month with greatest profit in 2011: {max_profit_month} with profit of {max_profit_value}")

print(monthly_profit_2011)


# In[26]:


# Plot monthly profits for 2011
monthly_profit_2011.plot(kind='bar', color='green', figsize=(6, 4))
plt.title('Monthly Profits in 2011')
plt.xlabel('Month')
plt.ylabel('Total Profit ($)')
plt.xticks(rotation=0)
plt.show()


# In[23]:


# Finding which month has made a lot of profit 
df['Date'] = pd.to_datetime(df['Date'])

df_2012 = df[df['Date'].dt.year == 2012]
df_2012['Month'] = df_2012['Date'].dt.month
monthly_profit_2012 = df_2012.groupby('Month')['Profit'].sum()

max_profit_month = monthly_profit_2012.idxmax()
max_profit_value = monthly_profit_2012.max()

print(f"Month with greatest profit in 2012: {max_profit_month} with profit of {max_profit_value}")

print(monthly_profit_2012)


# In[27]:


# Plot monthly profits for 2012
monthly_profit_2012.plot(kind='bar', color='Grey', figsize=(6, 4))
plt.title('Monthly Profits in 2012')
plt.xlabel('Month')
plt.ylabel('Total Profit ($)')
plt.xticks(rotation=0)
plt.show()


# In[31]:


# Finding which month has made a lot of profit 
df['Date'] = pd.to_datetime(df['Date'])

df_2013 = df[df['Date'].dt.year == 2013]
df_2013['Month'] = df_2013['Date'].dt.month
monthly_profit_2013 = df_2013.groupby('Month')['Profit'].sum()

max_profit_month = monthly_profit_2013.idxmax()
max_profit_value = monthly_profit_2013.max()

print(f"Month with greatest profit in 2013: {max_profit_month} with profit of {max_profit_value}")

print(monthly_profit_2013)


# In[32]:


# Plot monthly profits for 2013
monthly_profit_2013.plot(kind='bar', color='tan', figsize=(6, 4))
plt.title('Monthly Profits in 2013')
plt.xlabel('Month')
plt.ylabel('Total Profit ($)')
plt.xticks(rotation=0)
plt.show()


# In[34]:


# Finding which month has made a lot of profit 
df['Date'] = pd.to_datetime(df['Date'])

df_2014 = df[df['Date'].dt.year == 2014]
df_2014['Month'] = df_2014['Date'].dt.month
monthly_profit_2014 = df_2014.groupby('Month')['Profit'].sum()

max_profit_month = monthly_profit_2014.idxmax()
max_profit_value = monthly_profit_2014.max()

print(f"Month with greatest profit in 2014: {max_profit_month} with profit of {max_profit_value}")

print(monthly_profit_2014)


# In[37]:


# Plot monthly profits for 2014
monthly_profit_2014.plot(kind='bar', color='cyan', figsize=(6, 4))
plt.title('Monthly Profits in 2014')
plt.xlabel('Month')
plt.ylabel('Total Profit ($)')
plt.xticks(rotation=0)
plt.show()


# In[36]:


# Finding which month has made a lot of profit 
df['Date'] = pd.to_datetime(df['Date'])

df_2015 = df[df['Date'].dt.year == 2015]
df_2015['Month'] = df_2015['Date'].dt.month
monthly_profit_2015 = df_2015.groupby('Month')['Profit'].sum()

max_profit_month = monthly_profit_2015.idxmax()
max_profit_value = monthly_profit_2015.max()

print(f"Month with greatest profit in 2015: {max_profit_month} with profit of {max_profit_value}")

print(monthly_profit_2015)


# In[40]:


# Plot monthly profits for 2015
monthly_profit_2015.plot(kind='bar', color='maroon', figsize=(6, 4))
plt.title('Monthly Profits in 2015')
plt.xlabel('Month')
plt.ylabel('Total Profit ($)')
plt.xticks(rotation=0)
plt.show()


# In[41]:


# Finding which month has made a lot of profit 
df['Date'] = pd.to_datetime(df['Date'])

df_2016 = df[df['Date'].dt.year == 2016]
df_2016['Month'] = df_2016['Date'].dt.month
monthly_profit_2016 = df_2016.groupby('Month')['Profit'].sum()

max_profit_month = monthly_profit_2016.idxmax()
max_profit_value = monthly_profit_2016.max()

print(f"Month with greatest profit in 2016: {max_profit_month} with profit of {max_profit_value}")

print(monthly_profit_2016)


# In[42]:


# Plot monthly profits for 2016
monthly_profit_2016.plot(kind='bar', color='olive', figsize=(6, 4))
plt.title('Monthly Profits in 2016')
plt.xlabel('Month')
plt.ylabel('Total Profit ($)')
plt.xticks(rotation=0)
plt.show()


# In[47]:


# calculate the average blood pressure for each gender 
avg__Revenue = df.groupby('State')['Revenue'].mean()
print(avg__Revenue)

# plotting the data 
plt.figure(figsize=(70,40))
plt.bar(avg__Revenue.index, avg__Revenue.values, color= ['pink'])
plt.title('Average Revenue per State')
plt.xlabel('State')
plt.ylabel('Revenue ($)')

plt.show()


# In[54]:


avg__Revenue = df.groupby('Customer_Gender')['Revenue'].mean()
print(avg__Revenue)


# In[60]:


#plotting that data (pie chart)
labels = avg__Revenue.index
values = avg__Revenue.values

plt.figure(figsize=(4, 4))
plt.pie(values, labels=labels, autopct='%1.1f%%',colors= ['pink', 'blue'], startangle=90)
plt.title('Average Revenue by Gender')
plt.show()


# In[75]:


avg__Profit_Category = df.groupby('Product_Category')['Profit'].mean()
print(avg__Profit_Category)


# In[78]:


# plotting the data 
plt.figure(figsize=(6,3))
plt.bar(avg__Profit_Category.index, avg__Profit_Category.values, color= ['black'])
plt.title('Average Profit per Category')
plt.xlabel('Product Category')
plt.ylabel('Profit ($)')

plt.show()


# In[69]:


product_profit = df.groupby('Product')['Profit'].sum()

# Find the product with the maximum profit
max_profit_product = product_profit.idxmax()
max_profit_value = product_profit.max()

print(f"Product with the highest profit: {max_profit_product} with profit of {max_profit_value}")


# In[74]:


import plotly.express as px

# Plotting a treemap
fig = px.treemap(df.groupby('Product')['Profit'].sum().reset_index(), 
                 path=['Product'], 
                 values='Profit', 
                 title='Profit Distribution by Product')
fig.show()


# In[81]:


avg__UnitCost_Subategory = df.groupby('Sub_Category')['Unit_Cost'].mean()
print(avg__UnitCost_Subategory)


# In[98]:


import matplotlib.pyplot as plt


# avg__UnitCost_Subategory = ...

plt.figure(figsize=(30, 10))
bars = plt.bar(avg__UnitCost_Subategory.index, avg__UnitCost_Subategory.values, color=['yellow'])

plt.title('Average Unit Cost per Sub Category')
plt.xlabel('Sub Category')
plt.ylabel('Unit Cost($)')

# Add the numbers on top of the bars
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 0.1,  # Position text above the bar
             round(yval, 2),  # Display value rounded to 2 decimal places
             ha='center', va='bottom', fontsize=12)

plt.show()


# In[99]:


import plotly.express as px

# Plotting a treemap
fig = px.treemap(df.groupby('State')['Profit'].sum().reset_index(), 
                 path=['State'], 
                 values='Profit', 
                 title='Profit Distribution by State')
fig.show()


# In[103]:


df['Date'] = pd.to_datetime(df['Date'])

# Extract the year from the Date column
df['Year'] = df['Date'].dt.year

# Group by 'Year' and 'Product Category' to sum the costs
grouped_data = df.groupby(['Year', 'Product_Category'])['Cost'].sum().reset_index()

# Plotting the data as a line plot
plt.figure(figsize=(10, 6))

# Iterate over each product category and plot it as a line
for category in grouped_data['Product_Category'].unique():
    category_data = grouped_data[grouped_data['Product_Category'] == category]
    plt.plot(category_data['Year'], category_data['Cost'], label=category, marker='o')

# Adding title and labels
plt.title('Cost by Product Category and Year')
plt.xlabel('Year')
plt.ylabel('Cost($)')
plt.legend(title='Product Category')
plt.grid(True)

# Show the plot
plt.show()


# In[107]:


df['Date'] = pd.to_datetime(df['Date'])

# Extract the year from the Date column
df['Year'] = df['Date'].dt.year

# Group by 'Year' and 'Product Category' to sum the costs
grouped_data = df.groupby(['Year', 'Product_Category'])['Profit'].sum().reset_index()

# Plotting the data as a line plot
plt.figure(figsize=(10, 6))

# Iterate over each product category and plot it as a line
for category in grouped_data['Product_Category'].unique():
    category_data = grouped_data[grouped_data['Product_Category'] == category]
    plt.plot(category_data['Year'], category_data['Profit'], label=category, marker='o')

# Adding title and labels
plt.title('Profit by Product Category and Year')
plt.xlabel('Year')
plt.ylabel('Profit($)')
plt.legend(title='Product Category')
plt.grid(True)

# Show the plot
plt.show()


# In[106]:


df['Date'] = pd.to_datetime(df['Date'])

# Extract the year from the Date column
df['Year'] = df['Date'].dt.year

# Group by 'Year' and 'Product Category' to sum the costs
grouped_data = df.groupby(['Year', 'Product_Category'])['Revenue'].sum().reset_index()

# Plotting the data as a line plot
plt.figure(figsize=(10, 6))

# Iterate over each product category and plot it as a line
for category in grouped_data['Product_Category'].unique():
    category_data = grouped_data[grouped_data['Product_Category'] == category]
    plt.plot(category_data['Year'], category_data['Revenue'], label=category, marker='o')

# Adding title and labels
plt.title('Revenue by Product Category and Year')
plt.xlabel('Year')
plt.ylabel('Revenue($)')
plt.legend(title='Product Category')
plt.grid(True)

# Show the plot
plt.show()


# In[ ]:




