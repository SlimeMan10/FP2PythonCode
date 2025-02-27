import pandas as pd

# Load the inflation-adjusted housing and income datasets
housing_df = pd.read_csv(r"Filtered And Updated CSV\Median_Housing_Price_Adjusted.csv")
income_df = pd.read_csv(r"Filtered And Updated CSV\Median_Household_Income_Adjusted.csv")

# For housing, we assume the relevant column is 'Inflation_Adjusted_Median_Sale_Price'
# For income, we assume the relevant column is 'Inflation_Adjusted_Income'
# (Adjust these column names if they differ in your CSV files.)

# Merge the two datasets on 'Year'
merged_df = pd.merge(
    housing_df[['Year', 'Inflation_Adjusted_Median_Sale_Price']],
    income_df[['Year', 'Inflation_Adjusted_Income']],
    on='Year',
    how='inner'
)

# Calculate the median sale price as a percentage of the median household income
merged_df['Median_Sale_Price_as_Percent_of_Household_Income'] = (
    merged_df['Inflation_Adjusted_Median_Sale_Price'] / merged_df['Inflation_Adjusted_Income'] * 100
)

# Select only the Year and the calculated percentage columns
final_df = merged_df[['Year', 'Median_Sale_Price_as_Percent_of_Household_Income']]

# Save the result to a new CSV file
final_df.to_csv("Median_Sale_Price_Percentage_of_Household_Income.csv", index=False)

print("New CSV file 'Median_Sale_Price_Percentage_of_Household_Income.csv' created successfully.")
