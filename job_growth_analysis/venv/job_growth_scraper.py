import requests
from bs4 import BeautifulSoup
import pandas as pd

# Example URL (replace with the actual URL you're using)
url = 'https://www.example-labor-statistics.com/employment-data'

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Example: Extracting data from a table
data = []
table = soup.find('table', {'class': 'employment-data-table'})
rows = table.find_all('tr')

for row in rows[1:]:
    cols = row.find_all('td')
    date = cols[0].text.strip()
    industry = cols[1].text.strip()
    employment = cols[2].text.strip()
    growth = cols[3].text.strip()
    data.append([date, industry, employment, growth])

# Convert to DataFrame
df = pd.DataFrame(data, columns=['Date', 'Industry', 'Employment', 'Growth'])

# Save to CSV for future use
df.to_csv('employment_data.csv', index=False)

print("Data successfully scraped and saved to 'employment_data.csv'.")
