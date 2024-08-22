from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

# Set up Selenium with the Chrome browser driver
# Make sure to specify the correct path if ChromeDriver is not in your PATH
driver = webdriver.Chrome()  # If ChromeDriver is in your PATH
# driver = webdriver.Chrome(executable_path='path_to_chromedriver')  # If you need to specify the path

# Open the BLS website
driver.get('https://www.bls.gov/web/empsit/ceseesummary.htm')

# Optional: Wait for the page to fully load
driver.implicitly_wait(10)  # Wait up to 10 seconds for elements to load

# Extract the page source after JavaScript execution
html = driver.page_source

# Parse the HTML with BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Locate the table and scrape the data as before
table = soup.find('table')

if table:
    data = []
    rows = table.find_all('tr')
    for row in rows:
        cols = row.find_all(['td', 'th'])
        cols = [col.text.strip() for col in cols]
        data.append(cols)

    # Convert the data to a DataFrame
    df = pd.DataFrame(data)

    # Save the DataFrame to a CSV file
    df.to_csv('bls_employment_data.csv', index=False)
    print("Data successfully saved to 'bls_employment_data.csv'")
else:
    print("No table found on the page")

# Close the browser when done
driver.quit()
