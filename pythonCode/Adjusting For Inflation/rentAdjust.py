#Dataset comes from: https://ipropertymanagement.com/research/average-rent-by-year

import pandas as pd
import cpi

# Update the CPI database to the latest available data
cpi.update()

# Read the CSV file into a DataFrame
df = pd.read_csv(r'Original CSV Files/VisualizationTwo/monthlyRent.csv')

# Convert the 'Median Monthly Rent' to numeric values
df['Median Monthly Rent'] = pd.to_numeric(df['Median Monthly Rent'], errors='coerce')

# Ensure the 'Year' column is numeric and convert to integer
df['Year'] = pd.to_numeric(df['Year'], errors='coerce').astype(int)

# Create a new column for CPI-adjusted rent (adjusting to 2024 dollars)
df['CPI_Adjusted_Rent'] = df.apply(
    lambda row: cpi.inflate(row['Median Monthly Rent'], row['Year'], to=2024),
    axis=1
)

# Write the updated DataFrame to a new CSV file
output_path = r'Filtered And Updated CSV/VisualizationTwo/monthlyRent_adjusted.csv'
df.to_csv(output_path, index=False)
print("CSV file written to", output_path)
