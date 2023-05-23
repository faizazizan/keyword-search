#!/usr/bin/env python
# coding: utf-8

# In[1]:


from googlesearch import search

# Query to search
query = 'faiz'

# Number of results to scrape
num_results = 100

# Scrape SERPs
results = search(query, num_results=num_results)

# Process and print the results
for i, result in enumerate(results, 1):
    print(f"Result {i}: {result}")


# In[ ]:




