import requests
import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Your BLS API key
api_key = ''  # Replace with your actual API key

# BLS API URL
url = 'https://api.bls.gov/publicAPI/v2/timeseries/data/'

# Series IDs (for example, employment data)
series_ids = ['CEU0000000001']  # Replace with your desired series ID

# Determine the date range (last 10 years)
import datetime
end_year = datetime.datetime.now().year
start_year = end_year - 10

# Data payload for the API request
headers = {'Content-type': 'application/json'}
data = json.dumps({
    "seriesid": series_ids,
    "startyear": str(start_year),
    "endyear": str(end_year),
    "registrationkey": api_key
})

# Make the API request
response = requests.post(url, data=data, headers=headers)
json_data = response.json()

# Extract and process the data
all_data = []
for series in json_data['Results']['series']:
    series_id = series['seriesID']
    for item in series['data']:
        year = item['year']
        period = item['periodName']
        value = float(item['value'])
        all_data.append([series_id, year, period, value])

# Create a DataFrame from the extracted data
df = pd.DataFrame(all_data, columns=['Series ID', 'Year', 'Month', 'Value'])

# Convert to datetime for easier plotting
df['Date'] = pd.to_datetime(df['Year'] + ' ' + df['Month'])

# Sort the DataFrame by date
df = df.sort_values('Date')

# Plot the data
plt.figure(figsize=(10, 6))
sns.lineplot(data=df, x='Date', y='Value', marker='o')
plt.title(f'Employment Trends Over the Last 10 Years ({start_year} - {end_year})')
plt.xlabel('Date')
plt.ylabel('Employment (in thousands)')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

# Provide a summary statement below the chart
summary_statement = f"""
Summary of Employment Trends ({start_year} - {end_year}):
Over the past decade, there has been a general trend in employment data
in the series {series_ids[0]}. This trend indicates economic growth/stability
as reflected by the employment figures, which exhibit (growth/stability/decline).
Notable fluctuations or steady increases/decreases are observed in certain years
that may correspond to economic events such as (recession, recovery, pandemic effects, etc.).
"""
print(summary_statement)
