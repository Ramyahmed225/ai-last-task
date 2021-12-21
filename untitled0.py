# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 19:49:13 2021

@author: alquds
"""

#!/usr/bin/env python
# coding: utf-8

# # Build all python needed classes to get the following from the Wuzzuf jobs in Egypt data set:
# - 1.Read the dataset, convert it to DataFrame and display some from it.
# - 2.Display structure and summary of the data.
# - 3.Clean the data (null, duplications)
# - 4.Count the jobs for each company and display that in order (What are the most demanding companies for jobs?)
# - 5.Show step 4 in a pie chart
# - 6.Find out what are the most popular job titles.
# - 7.Show step 6 in bar chart
# - 8.Find out the most popular areas?
# - 9.Show step 8 in bar chart
# - 10.Print skills one by one and how many each repeated and order the output to find out the most important skills required?

# In[5]:


#import  libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt





df = pd.read_csv('Wuzzuf_Jobs.csv')
df.head()

df.describe()

df.info()

df.isnull().sum()



x = df.Company.value_counts()
print(x)











# the most freqancy companies
sorted_counts = df['Company'].value_counts()[:6]
plt.pie(sorted_counts, labels = sorted_counts.index, autopct='%1.0f%%')
plt.title("high hired company", fontsize=20)
plt.axis('square');













#6.Find out what are the most popular job titles.
x= df['Title'].value_counts()[:5]
x.plot(kind='barh',figsize=(15,15), color="green")












x= df['Location'].value_counts()[:10]
x.plot(kind='bar',figsize=(15,10), color="green")









x= df['Country'].value_counts()[:10]
x.plot(kind='bar',figsize=(15,10), color="green")