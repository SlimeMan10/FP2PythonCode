import pandas as pd

# Read the CSV file containing the inflation-adjusted household income
input_path = r'Filtered And Updated CSV\VisualizationOne\Median_Household_Income_Adjusted.csv'
df = pd.read_csv(input_path)

# Calculate the monthly CPI adjusted income by dividing the annual inflation-adjusted income by 12
df['Monthly_CPI_Adjusted_Income'] = df['Inflation_Adjusted_Income'] / 12

# Create a new DataFrame with just the 'Year' and 'Monthly_CPI_Adjusted_Income' columns
output_df = df[['Year', 'Monthly_CPI_Adjusted_Income']]

# Define the output path for the new CSV file
output_path = r'Filtered And Updated CSV\VisualizationTwo\Median_Household_Monthly_Income_Adjusted.csv'
output_df.to_csv(output_path, index=False)

print("CSV file with Year and monthly CPI adjusted income has been written to:", output_path)
