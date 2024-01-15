#!/usr/bin/env python
# coding: utf-8

# In[38]:


# Import Dependencies

import pandas as pd
import csv


# In[39]:


# Read file CSV

file_csv='Resources_/budget_data.csv'
df = pd.read_csv('Resources_/budget_data.csv')


# In[40]:


# Stores the header row

with open('Resources_/budget_data.csv', 'r') as file:
    csv_reader = csv.reader(file)
    header_row = next(csv_reader)
    print("Header Row:", header_row)


# In[41]:


# The total number of months included in the dataset

df['Date'] = pd.to_datetime(df['Date'], format='%b-%y', errors='coerce')
quantity_months = df['Date'].dt.to_period("M").nunique()


# In[42]:


# Print quantity of months
print(f"Total Months: {quantity_months}")


# In[43]:


# Net total amount of "Profit/Losses"
total_profit_losses = df['Profit/Losses'].sum()


# In[44]:


# Print Total
print(f"Total: ${total_profit_losses}")


# In[45]:


# Changes in "Profit/Losses"and average amount
df['Change_Profit/Losses'] = df['Profit/Losses'].diff()
average_change = df['Change_Profit/Losses'].mean()


# In[46]:


# Print Average
print(f"Average Change: $ {average_change:.2f}")


# In[47]:


# The greatest increase

max_increase_date = df.loc[df['Change_Profit/Losses'].idxmax(), 'Date']
max_increase_amount = df['Change_Profit/Losses'].max()


# In[48]:


print(f"Greatest Increase in Profits: {max_increase_date.strftime('%b-%y')}, (${max_increase_amount:.2f})")


# In[49]:


# The greatest decrease

max_decrease_date = df.loc[df['Change_Profit/Losses'].idxmin(), 'Date']
max_decrease_amount = df['Change_Profit/Losses'].min()


# In[50]:


print(f"Greatest Decrease in Profits: {max_decrease_date.strftime('%b-%y')}, (${max_decrease_amount:.2f})")


# In[51]:


# String with the results
results = f"""
Financial Analysis
----------------------------
Total Months: {quantity_months}
Total: ${total_profit_losses}
Average changes : ${average_change:.2f}
Greatest Increase in Profits: {max_increase_date.strftime('%b-%y')}, (${max_increase_amount:.0f})
Greatest Decrease in Profits: {max_decrease_date.strftime('%b-%y')}, (${max_decrease_amount:.0f})
"""


# In[52]:


print(results)


# In[53]:


with open('analysis.txt', 'w') as file:
    file.write(results)

