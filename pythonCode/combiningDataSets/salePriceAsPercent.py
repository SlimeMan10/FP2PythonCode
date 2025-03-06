import pandas as pd

# File paths (using raw strings to avoid issues with backslashes)
housing_path = r"median home sale price\adjusted\filtered_data.csv"
income_path = r"Median Income\original\Median Income (CPI Adjusted But Removed 01-01).csv"

# Load the datasets
housing_df = pd.read_csv(housing_path)
income_df = pd.read_csv(income_path)

# For housing, we assume the relevant column is 'Inflation_Adjusted_Median_Sale_Price'
# For income, we assume the relevant column is 'Household Income'
# If a 'Year' column doesn't exist in the income dataset, extract it from observation_date
if 'Year' not in income_df.columns:
    income_df["Year"] = pd.to_datetime(income_df["observation_date"]).dt.year

# Merge the two datasets on 'Year'
merged_df = pd.merge(
    housing_df[['Year', 'Inflation_Adjusted_Median_Sale_Price']],
    income_df[['Year', 'Household Income']],
    on='Year',
    how='inner'
)

# Calculate the median sale price as a percentage of the household income
merged_df['Sale_Price_as_Percent_of_Median_Income'] = (
    merged_df['Inflation_Adjusted_Median_Sale_Price'] / merged_df['Household Income'] * 100
)

# Select only the Year and the calculated percentage columns
final_df = merged_df[['Year', 'Sale_Price_as_Percent_of_Median_Income']]

# Save the result to a new CSV file
final_df.to_csv("Sale_Price_Percent_of_Median_Income.csv", index=False)

print("New CSV file 'Sale_Price_Percent_of_Median_Income.csv' created successfully.")
