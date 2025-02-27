#Link to source: https://fred.stlouisfed.org/series/MEHOINUSA672N

import pandas as pd
import cpi

# Load the dataset
df = pd.read_csv(r"Original CSV Files/Median Household Income Over time.csv")

# Extract the year from the date column
df["Year"] = pd.to_datetime(df["observation_date"]).dt.year

# Rename the income column for clarity
df.rename(columns={"MEHOINUSA672N": "Household_Income"}, inplace=True)

# Convert the household income to inflation-adjusted dollars (2023 as the base year)
cpi.update()  # Update CPI data to get the latest values
df["Inflation_Adjusted_Income"] = df.apply(lambda row: cpi.inflate(row["Household_Income"], row["Year"], to=2023), axis=1)

# Select and reorder relevant columns
df = df[["Year", "Household_Income", "Inflation_Adjusted_Income"]]

# Save to a new CSV file
df.to_csv("Median_Household_Income_Adjusted.csv", index=False)

print("New CSV file 'Median_Household_Income_Adjusted.csv' has been created successfully.")
