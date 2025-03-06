import pandas as pd

# Define file paths
income_path = r'Median Income\original\Median Income (CPI Adjusted But Removed 01-01).csv'
mortgage_path = r'monthlyPayments\adjusted\monthlyMortgage_Adjusted.csv'
rent_path = r'monthlyPayments\adjusted\monthlyRent_adjusted.csv'

# Load the CSV files into DataFrames
df_income = pd.read_csv(income_path)
df_mortgage = pd.read_csv(mortgage_path)
df_rent = pd.read_csv(rent_path)

# For the income dataset:
if "observation_date" in df_income.columns:
    df_income["observation_date"] = pd.to_datetime(df_income["observation_date"])
    df_income["Year"] = df_income["observation_date"].dt.year
elif "Year" not in df_income.columns:
    raise KeyError("Income dataset must have either 'observation_date' or 'Year' column.")

# For the mortgage dataset:
if "Year" not in df_mortgage.columns:
    if "observation_date" in df_mortgage.columns:
        df_mortgage["observation_date"] = pd.to_datetime(df_mortgage["observation_date"])
        df_mortgage["Year"] = df_mortgage["observation_date"].dt.year
    else:
        raise KeyError("Mortgage dataset must have either 'observation_date' or 'Year' column.")

# For the rent dataset:
if "Year" not in df_rent.columns:
    if "observation_date" in df_rent.columns:
        df_rent["observation_date"] = pd.to_datetime(df_rent["observation_date"])
        df_rent["Year"] = df_rent["observation_date"].dt.year
    else:
        raise KeyError("Rent dataset must have either 'observation_date' or 'Year' column.")

# Merge the datasets on 'Year' using inner joins (only overlapping years)
merged_df = pd.merge(df_income, df_mortgage, on="Year", how="inner")
merged_df = pd.merge(merged_df, df_rent, on="Year", how="inner")

# Calculate the percentages:
# Annualize the monthly rent (multiply by 12) then compute rent percentage.
merged_df["Rent_Percentage"] = (merged_df["CPI_Adjusted_Rent"] * 12 / merged_df["Household Income"]) * 100

# Compute the mortgage percentage using the inflation-adjusted monthly mortgage payment (annualized)
merged_df["Mortgage_Percentage"] = (merged_df["Inflation_Adjusted_Monthly_Payment"] * 12 / merged_df["Household Income"]) * 100

# Create the final DataFrame with only 3 columns: Year, Rent_Percentage, Mortgage_Percentage.
final_df = merged_df[["Year", "Rent_Percentage", "Mortgage_Percentage"]]

# Define the output path for the new CSV file and save it
output_path = r'Income_Percentages.csv'
final_df.to_csv(output_path, index=False)

print("CSV file created with Year, Rent_Percentage, and Mortgage_Percentage at:", output_path)
