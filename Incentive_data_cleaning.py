#!/usr/bin/env python
# coding: utf-8

# In[15]:


import pandas as pd

# Load the Excel file
file_path = "file.csv"  # Replace with the actual path to your Excel file
df = pd.read_csv(file_path)


# In[16]:


# Specify the columns to merge
columns_to_merge = [
    "Incentive Amount",
    "Maximum Incentive",
    "Eligible System Size",
    "Equipment Requirements",
    "Installation Requirements",
    "Carryover Provisions",
    "Fuel Mix",
    "Emissions",
    "Distribution and Frequency",
    "Standard Format Required",
    "Eligible Efficiency Technologies",
    "Green Building Requirement",
    "Equipment Efficiency Requirement",
    "Renewable Energy Requirement",
    "Standard",
    "Technology Minimum",
    "Compliance Multipliers",
    "REC Lifetime",
    "Credit Trading/Tracking System",
    "Alternative Compliance Payment",
    "Start Date",
    "Eligible Electric Vehicle Technologies",
    "Energy Reduction Goal/Requirement",
    "Expiration Date",
    "Funding Source",
    "Ownership of Renewable Energy Credits",
    "Budget",
    "Maximum Loan",
    "Loan Term",
    "Interest Rate",
    "Applicable Utilities",
    "System Capacity Limit",
    "Aggregate Capacity Limit",
    "Net Excess Generation",
    "Meter Aggregation",
    "Duration",
    "Renewables % or Amount",
    "Types",
    "Terms",
    "Test Methods",
    "Implementing Agency",
    "Standard Agreement",
    "Insurance Requirements",
    "External Disconnect Switch",
    "Net Metering Required",
]

# Merge the specified columns into a new column
df["Additional Details"] = df[columns_to_merge].apply(lambda row: "\n".join(row.dropna().astype(str)), axis=1)

# Drop the original columns that were merged
df.drop(columns=columns_to_merge, inplace=True)

# Save the modified DataFrame back to Excel
output_file_path = "C://Rashmi//UTD//Community Dreams//Dataset//Incentives dataset//OH_program_details_44136_modified.xlsx"
df.to_excel(output_file_path, index=False)

print("Merging and transformation completed. Saved to:", output_file_path)


# In[ ]:




