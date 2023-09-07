#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[5]:


residential_incentives = pd.read_csv("C:/Rashmi/UTD/Community Dreams/Dataset/Incentives dataset/Zipcode_wise_program_deatils/combined_data_with_zipcodes.csv")


# In[10]:


print(residential_incentives.head())


# In[13]:


# Filter rows where "Applicable Sectors" contains the word "residential"
residential_rows = residential_incentives[residential_incentives["Applicable Sectors"].str.contains("residential", case=False)]


# In[15]:


print(residential_rows)


# In[16]:


# Check for duplicate values in the "Program Name" column
duplicate_programs = residential_rows[residential_rows.duplicated("Program Name")]

# List the duplicate program names
if not duplicate_programs.empty:
    duplicate_names = duplicate_programs["Program Name"].tolist()
    print("Duplicate Program Names:")
    for name in duplicate_names:
        print(name)
else:
    print("No duplicate program names found.")






# In[18]:


# Count and list duplicate program names along with their counts
duplicate_counts = residential_rows["Program Name"].value_counts()
duplicate_programs = duplicate_counts[duplicate_counts > 1]

if not duplicate_programs.empty:
    print("Duplicate Program Names and Counts:")
    for name, count in duplicate_programs.items():
        print(f"{name}: {count} times")
else:
    print("No duplicate program names found.")


# In[20]:


# Replace empty cells with "unknown"
residential_rows_filled = residential_rows.fillna("unknown")

# Save the updated dataset
residential_rows_filled.to_csv("residential_cleaned_dataset.csv", index=False)


# In[21]:


# Calculate distinct program names and their counts
distinct_program_counts = residential_rows_filled["Program Name"].value_counts()

# Print distinct program names and their counts
print("Distinct Program Names and Counts:")
for program_name, count in distinct_program_counts.items():
    print(f"{program_name}: {count} times")






# In[ ]:




