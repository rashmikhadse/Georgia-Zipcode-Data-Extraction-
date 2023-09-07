#!/usr/bin/env python
# coding: utf-8

# In[1]:


import time
import csv
from selenium import webdriver
#from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import pandas as pd

# Set up the Chrome WebDriver (you can use other WebDriver options if desired)
driver = webdriver.Chrome(ChromeDriverManager().install())


# In[3]:


# List of zip codes to iterate over

zip_codes = [
    "31136","31139","31141","31145","31146","31150","31156","31169","31192”
]


# In[4]:


# Iterate over each zip code
for zip_code in zip_codes:
    print(f"Processing data for zip code: {zip_code}")

    # Step 1: Visit the initial page with the list of programs
    url = f"https://programs.dsireusa.org/system/program?zipcode={zip_code}"
    driver.get(url)

    # Wait for the dynamic content to load (you might need to adjust the wait time depending on the page)
    time.sleep(5)

    # Get the page source after the dynamic content has loaded
    page_source = driver.page_source

    # Step 2: Parse the page source with BeautifulSoup to get the links to individual program pages
    soup = BeautifulSoup(page_source, "html.parser")

    # Find the table containing the data
    table = soup.find("table")

    if table:
        # Find all rows in the table except the header row
        rows = table.find_all("tr")[1:]

        # Initialize an empty list to store the structured data
        structured_data = []

        # Extract data from each row
        for row in rows:
            cells = row.find_all(["th", "td"])
            link = cells[0].find("a")["href"]  # Get the link to the program page
            program_name = cells[0].text.strip()

            # Step 3: Visit the individual program page
            program_url = f"https://programs.dsireusa.org{link}"
            driver.get(program_url)

            # Wait for the dynamic content to load (you might need to adjust the wait time depending on the page)
            time.sleep(5)

            # Get the page source after the dynamic content has loaded
            program_page_source = driver.page_source

            # Step 4: Parse the program page to extract the data from the "program-detail wrapper" division
            program_soup = BeautifulSoup(program_page_source, "html.parser")
            program_detail_div = program_soup.find("div", {"class": "programOverview"})

            if program_detail_div:
                # Find all points in the "program-detail wrapper" division
                points = program_detail_div.find_all("li")

                # Create a dictionary to store the details of the current program
                program_details = {
                    "Program Name": program_name
                }

                # Extract and store the details in the dictionary
                for point in points:
                    parts = point.get_text(strip=True).split(":", 1)
                    if len(parts) == 2:
                        key, value = parts
                        program_details[key.strip()] = value.strip()

                # Append the dictionary to the structured_data list
                structured_data.append(program_details)
            else:
                print(f"No 'program-detail wrapper' division found on the program page for '{program_name}'.")

        # CSV file path to save the data
        import os 
        current_directory = os.getcwd()
        file_name = f"OH_program_details_{zip_code}.csv"
        csv_file_path = os.path.join(current_directory, file_name)
        print("CSV File Path:", csv_file_path)


        # Use pandas to normalize (flatten) the nested dictionarie
        flattened_data = pd.json_normalize(structured_data)

        # Write the flattened data to a CSV file
        flattened_data.to_csv(csv_file_path, index=False, encoding="utf-8")

        print(f"CSV file for zip code {zip_code} has been created successfully.")
    else:
        print(f"No table found on the initial page for zip code {zip_code}.")

# Close the browser
driver.quit()


# In[ ]:




