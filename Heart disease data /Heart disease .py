#!/usr/bin/env python
# coding: utf-8

# In[24]:


import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
df= pd.read_csv('C:/Users/NgcoboXH/Downloads/heart disease.csv')
df


# In[2]:


df.info()


# In[4]:


import seaborn as sns


# In[8]:


# calculate the average blood pressure for each gender 
avg__blood_pressure = df.groupby('Gender')['Blood Pressure'].mean()
print(avg_blood_pressure)


# In[12]:


import matplotlib.pyplot as plt

# plotting the data 
plt.figure(figsize=(4,3))
plt.bar(avg_blood_pressure.index, avg_blood_pressure.values, color= ['pink', 'blue'])
plt.title('Average Blood Pressure by Gender')
plt.xlabel('Gender')
plt.ylabel('Blood pressure (mmHg)')

plt.show()


# In[16]:


# calculate the average blood pressure for each gender 
avg__Cholesterol_Level = df.groupby('Gender')['Cholesterol Level'].mean()
print(avg__Cholesterol_Level)


# In[17]:


# plotting the data 
plt.figure(figsize=(4,3))
plt.bar(avg__Cholesterol_Level, avg__Cholesterol_Level.values, color= ['pink', 'blue'])
plt.title('Average Blood Pressure by Gender')
plt.xlabel('Gender')
plt.ylabel('Cholesterol Level(mmol/L)')

plt.show()


# In[19]:


sns.scatterplot(x='Age', y='Cholesterol Level', hue='Heart Disease Status', data=df)


# In[21]:


sns.scatterplot(x='BMI', y='Blood Pressure', hue='High Blood Pressure', data=df)


# In[42]:


exercise_heart_disease = df.groupby('Exercise Habits')['Heart Disease Status'].value_counts(normalize=True).unstack()

# Plotting
exercise_heart_disease.plot(kind='bar', stacked=True, figsize=(10, 6), color=['lightblue', 'orange'])
plt.title('Heart Disease by Exercise Habits')
plt.xlabel('Exercise Habits')
plt.ylabel('Proportion')
plt.legend(title='Heart Disease Status')

plt.show()


# In[7]:


smoking_heart_disease = df.groupby('Smoking')['Heart Disease Status'].value_counts(normalize=True).unstack()

# Plotting
smoking_heart_disease.plot(kind='bar', stacked=True, figsize=(10, 6), color=['green', 'red'])
plt.title('Smoking by Heart diesase')
plt.xlabel('Smoking')
plt.ylabel('Proportion')
plt.legend(title='Heart Disease Status with smoking habits')

plt.show()


# In[6]:


count_data = df.groupby(['Stress Level', 'Heart Disease Status']).size().unstack()

# Plot
count_data.plot(kind='bar', stacked=True)
plt.title('Stress Level vs Heart Disease')
plt.ylabel('Count')
plt.xlabel('Stress Level')
plt.legend(title='Heart Disease')

plt.show()


# In[12]:


Heart_disease = df.groupby('Family Heart Disease')['Heart Disease Status'].value_counts(normalize=True).unstack()

# Plotting
Heart_disease.plot(kind='bar', stacked=True, figsize=(10, 6), color=['purple', 'pink'])
plt.title('Family heart disease vs individual heart disease status')
plt.xlabel('Family heart disease')
plt.ylabel('Proportion')
plt.legend(title='Heart Disease Status with Family heart disease')

plt.show()


# In[15]:


# calculate the average blood pressure for each gender 
avg__Sleeping_Diabetes = df.groupby('Diabetes')['Sleep Hours'].mean()
print(avg__Sleeping_Diabetes)


# In[20]:


Heart_disease = df.groupby('Sugar Consumption')['Heart Disease Status'].value_counts(normalize=True).unstack()

# Plotting
Heart_disease.plot(kind='bar', stacked=True, figsize=(10, 6), color=['yellow', 'orange'])
plt.title('Sugar Consumptions having direct impact on Heart Disease')
plt.xlabel('Sugar Consumption')
plt.ylabel('Proportion')
plt.legend(title='Sugar consumption vs Heart diesease')

plt.show()


# In[ ]:




