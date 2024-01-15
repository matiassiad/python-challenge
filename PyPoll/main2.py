#!/usr/bin/env python
# coding: utf-8

# In[16]:


# Import Dependencies

import pandas as pd
import csv


# In[17]:


# Read file CSV

file_csv='Resources/election_data.csv'
df = pd.read_csv('Resources/election_data.csv')


# In[18]:


# Stores the header row

with open('Resources/election_data.csv', 'r') as file:
    csv_reader = csv.reader(file)
    header_row = next(csv_reader)
    print("Header Row:", header_row)


# In[19]:


# The total number of votes cast

total_votes = df['Ballot ID'].count()


# In[20]:


# Print count of votes

print(f"The total number of votes cast: {total_votes}")


# In[21]:


# The percentage of votes each candidate won

votes_per_candidate = df['Candidate'].value_counts()
percentage_per_candidate = (votes_per_candidate / total_votes) * 100


# In[22]:


# Print results

print("The percentage of votes each candidate won:")
for candidate, percentage in percentage_per_candidate.items():
    votes = votes_per_candidate[candidate]
    print(f"{candidate}: {percentage:.3f}%, ({votes})")


# In[23]:


# Show winner

winner = votes_per_candidate.idxmax()


# In[24]:


# Print winner

print(f"\n Winner: {winner}")


# In[25]:


# String with the results
results = f"""
Election Results
-------------------------
Total Votes: {total_votes}
-------------------------
Charles Casper Stockham: {percentage_per_candidate['Charles Casper Stockham']:.3f}%, {votes_per_candidate['Charles Casper Stockham']}
Diana DeGette: {percentage_per_candidate['Diana DeGette']:.3f}%, {votes_per_candidate['Diana DeGette']}
Raymon Anthony Doane: {percentage_per_candidate['Raymon Anthony Doane']:.3f}%, {votes_per_candidate['Raymon Anthony Doane']}
-------------------------
Winner: {winner}
-------------------------
"""

print(results)


# In[26]:


# Output file

output_file = 'analysis2.txt'


# In[27]:


# Export the string to a text file

with open(output_file, 'w') as file:
     file.write(results)

