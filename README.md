# Incentives Recommendation Engine

### 1. What was the primary goal or objective of the project?
Primary goal of the First stage of the project was to extract all the incentive programs data from a public website called DSIRE from the 5 States for all their zipcodes. I extracted all the data for Georgia state.

### 2. Can you briefly explain the main components of the project?
Step 1: Data gathering using Webscraping from DSIRE website for states GA, AZ, CO, OH and FL
Step 2: Cleaning the gathered data
Step 3: Creating a centralized Database for gathered data on Google Cloud Platform
Step 4: Builed Dashboards and recommendation engine for recommending incentives

### 3. What technology stack did you use for your project? Any particular reason for choosing this stack? (e.g., Python, React, Java, WordPress)
I used Python because it has:
Rich Ecosystem of Libraries: Python boasts a vast and powerful ecosystem of data analysis libraries, including NumPy, pandas, Matplotlib, Seaborn, SciPy, scikit-learn, and more. These libraries provide robust tools for data manipulation, analysis, visualization, and machine learning.
Data Science Community: Python has a thriving data science community, which means there is an abundance of resources, tutorials, and forums available for data analysts and scientists to seek help, share knowledge, and collaborate on projects.

### 4. Where is the codebase stored? Do we use a version control system like Git?
I did not use Git

### Were there any specific challenges you encountered during the development? How did you address them?
When I started Data Extraction, the Python library BeautifulSoup wasnt enough for webscraping, we figured out that Selenium was also needed web automation. Selenium allows you to control web browsers programmatically, interact with web elements, and automate repetitive tasks like form submissions, clicking links, and navigating web pages. The DSIRE website had to navigate through many pages in order to extract the complete data so we used Selenium too. Next, I faced issues in installing Chrome Webdriver package in order to use Selenium which I figured it out later by going through various documentations, articles and tutorial videos.

### Is there any documentation or README that can help me understand the project better?
Yes there is a documentation posted on our Slack group.

### Were there any third-party tools or APIs you integrated into the project?
No


