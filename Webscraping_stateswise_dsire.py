#!/usr/bin/env python
# coding: utf-8

# In[29]:


#This code scrapes the table data of ebsite dsire.org.
#Chrome driver Operations: clicking next page button




from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd
import time

# Initialize the Chrome driver
driver_path = r'C:\Users\rashu\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe'
driver = webdriver.Chrome(driver_path)

# Open the webpage
driver.get("https://programs.dsireusa.org/system/program/fl")
time.sleep(5)

# Initialize page counter
page_counter = 1
data = []

while True:
    try:
        # Parse the HTML content of the page with BeautifulSoup
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        # Find the table on the webpage
        table = soup.find('div', attrs={'class': 'wrapper programs-table'})
        # Find all the rows in the table
        table_rows = table.find_all('tr')
        
        # Loop through each row
        for tr in table_rows:
            # Find all columns in each row
            td = tr.find_all('td')
            # Extract the text from the columns
            row = [i.text for i in td]
            data.append(row)
        
        if page_counter == 4:
            break
        
        # Find the 'next' button
        next_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="DataTables_Table_0_next"]')))
        
        # Use ActionChains to move to the 'next' button and click it
        actions = ActionChains(driver)
        actions.move_to_element(next_button).click().perform()
        
        # Increment the page counter
        page_counter += 1
        # Wait for the next page to load
        time.sleep(5)

    except Exception as e:
        print(f"An error occurred: {e}")
        break

# Close the driver
driver.close()

# Create a pandas DataFrame from the data and set column names
columns = ['Name', 'State/Territory', 'Category', 'Policy/Incentive Type', 'Created', 'Last Updated']
df = pd.DataFrame(data, columns=columns)

print(df)


# In[30]:


# Print unique records (drop duplicates)
unique_df = df.drop_duplicates()

# Reset the index after dropping duplicates
unique_df.reset_index(drop=True, inplace=True)

print(unique_df)


# In[31]:


# Export the DataFrame to an Excel file
unique_df.to_excel('florida.xlsx', index=False)


# In[32]:


# To check whether the file saving or not
import os

file_path = r'C:/Rashmi/UTD/Community Dreams/Dataset/florida.xlsx'

if os.path.exists(file_path):
    print(f"Excel file '{file_path}' exists.")
else:
    print(f"Excel file '{file_path}' does not exist.")

# To know where the file is storing 
print(os.getcwd())


# In[ ]:





# In[ ]:




