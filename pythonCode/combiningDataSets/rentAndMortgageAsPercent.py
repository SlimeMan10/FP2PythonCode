import pandas as pd

# Define file paths
income_path = r'Filtered And Updated CSV\VisualizationTwo\Median_Household_Monthly_Income_Adjusted.csv'
mortgage_path = r'Filtered And Updated CSV\VisualizationTwo\monthlyMortgage_Adjusted.csv'
rent_path = r'Filtered And Updated CSV\VisualizationTwo\monthlyRent_adjusted.csv'

# Load the CSV files into DataFrames
df_income = pd.read_csv(income_path)
df_mortgage = pd.read_csv(mortgage_path)
df_rent = pd.read_csv(rent_path)

# Merge the datasets on 'Year'. We use inner joins to keep only common years.
df_temp = pd.merge(df_income, df_mortgage, on="Year", how="inner")
df_all = pd.merge(df_temp, df_rent, on="Year", how="inner")

# Calculate the percentage of monthly income that goes to rent and mortgage:
# Rent percentage = (CPI_Adjusted_Rent / Monthly_CPI_Adjusted_Income) * 100
# Mortgage percentage = (Inflation_Adjusted_Monthly_Payment / Monthly_CPI_Adjusted_Income) * 100
df_all['Rent_Monthly_Percent'] = (df_all['CPI_Adjusted_Rent'] / df_all['Monthly_CPI_Adjusted_Income']) * 100
df_all['Mortgage_Monthly_Percent'] = (df_all['Inflation_Adjusted_Monthly_Payment'] / df_all['Monthly_CPI_Adjusted_Income']) * 100

# Create a new DataFrame with only the desired columns
output_df = df_all[['Year', 'Rent_Monthly_Percent', 'Mortgage_Monthly_Percent']]

# Define the output path for the new CSV file
output_path = r'Filtered And Updated CSV\VisualizationTwo\Income_Percentages.csv'
output_df.to_csv(output_path, index=False)

print("CSV file created with Year, Rent_Monthly_Percent, and Mortgage_Monthly_Percent at:", output_path)
