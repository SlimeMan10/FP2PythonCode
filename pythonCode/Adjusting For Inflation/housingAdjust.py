#Link to original dataset: https://fred.stlouisfed.org/series/MSPUS

import pandas as pd
import cpi

# Load the housing dataset
df = pd.read_csv(r"Original CSV Files\Median Sales Price of Houses Sold In the US Over time.csv")

# Convert observation_date to datetime format
df["observation_date"] = pd.to_datetime(df["observation_date"])

# Filter the data for years 1984 through 2023
df = df[(df["observation_date"].dt.year >= 1984) & (df["observation_date"].dt.year <= 2023)]

# Extract only the first quarter data (Q1 includes January, February, March)
df_q1 = df[df["observation_date"].dt.quarter == 1].copy()

# Extract the year for use in CPI adjustment
df_q1["Year"] = df_q1["observation_date"].dt.year

# Update CPI data to get the latest values
cpi.update()

# Adjust the median sale price to 2023 dollars using the cpi package
df_q1["Inflation_Adjusted_Median_Sale_Price"] = df_q1.apply(
    lambda row: cpi.inflate(row["Median Sale Price"], row["Year"], to=2023),
    axis=1
)

# Select and reorder relevant columns
df_q1 = df_q1[["Year", "observation_date", "Median Sale Price", "Inflation_Adjusted_Median_Sale_Price"]]

# Save to a new CSV file
df_q1.to_csv("Median_Housing_Price_Adjusted.csv", index=False)

print("New CSV file 'Median_Housing_Price_Adjusted.csv' has been created successfully.")
