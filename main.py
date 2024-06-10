import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('dataset.csv')

# Basic exploration
print(df.head())
print(df.columns)
print(df.info())
print(df.describe())

# Strip whitespace from column names
df.columns = df.columns.str.strip()
print("Columns after stripping whitespace:", df.columns)

# Check if 'Date' column exists and convert it to datetime
if 'Date' in df.columns:
    df['Date'] = pd.to_datetime(df['Date'])
    print("Converted 'Date' column to datetime.")
else:
    print("Column 'Date' not found in DataFrame.")
    # Optionally, you could exit the script or handle the missing column case
    exit()

# Data cleaning
df = df.dropna()

# Analysis
print("Average Temperature:", df['Temperature'].mean())
print("Total Precipitation:", df['Precipitation'].sum())

# Visualizations
plt.figure(figsize=(10, 5))
plt.plot(df['Date'], df['Temperature'])
plt.title('Daily Temperature Over Time')
plt.xlabel('Date')
plt.ylabel('Temperature')
plt.show()

plt.figure(figsize=(10, 5))
sns.histplot(df['Precipitation'], bins=20)
plt.title('Precipitation Distribution')
plt.xlabel('Precipitation')
plt.ylabel('Frequency')
plt.show()

# Trend analysis
df['Month'] = df['Date'].dt.month
monthly_avg_temp = df.groupby('Month')['Temperature'].mean()
monthly_avg_precip = df.groupby('Month')['Precipitation'].mean()

plt.figure(figsize=(10, 5))
plt.plot(monthly_avg_temp.index, monthly_avg_temp, label='Avg Temperature')
plt.plot(monthly_avg_precip.index, monthly_avg_precip, label='Avg Precipitation')
plt.title('Monthly Average Temperature and Precipitation')
plt.xlabel('Month')
plt.ylabel('Value')
plt.legend()
plt.show()

# Correlation analysis
correlation_matrix = df.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()
