import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the scraped data
df = pd.read_csv('employment_data.csv')

# Data Cleaning
df['Date'] = pd.to_datetime(df['Date'])
df['Employment'] = pd.to_numeric(df['Employment'].str.replace(',', ''), errors='coerce')
df['Growth'] = pd.to_numeric(df['Growth'].str.replace('%', ''), errors='coerce')

# Handle missing values
df = df.dropna()

# Data Analysis - Example: Grouping by industry and calculating yearly averages
df.set_index('Date', inplace=True)
industry_growth = df.groupby('Industry').resample('Y').mean()

# Visualization - Example: Plotting employment trends by industry
plt.figure(figsize=(14, 7))
for industry in df['Industry'].unique():
    industry_data = df[df['Industry'] == industry].resample('Y').mean()
    plt.plot(industry_data.index, industry_data['Employment'], label=industry)

plt.title('Yearly Employment Trends by Industry')
plt.xlabel('Year')
plt.ylabel('Employment')
plt.legend(title='Industry')
plt.show()
