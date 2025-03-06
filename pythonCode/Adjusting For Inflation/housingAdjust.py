import pandas as pd
import cpi

# Load the housing dataset
df = pd.read_csv(r"median home sale price\original\Median Sale Price.csv")

# Convert observation_date to datetime format.
# The dates in your dataset are in the format YYYY-MM-DD.
df["observation_date"] = pd.to_datetime(df["observation_date"])

# Filter the data for years 1984 through 2023
df = df[(df["observation_date"].dt.year >= 1984) & (df["observation_date"].dt.year <= 2023)]

# Create a 'Year' column for use in CPI adjustment.
df["Year"] = df["observation_date"].dt.year

# Update CPI data to get the latest values
cpi.update()

# Define a helper function for inflation adjustment.
def adjust_price(row):
    # Adjust the median sale price to 2023 dollars
    return cpi.inflate(row["Median Sale Price"], row["Year"], to=2023)

# Apply the inflation adjustment to each row
df["Inflation_Adjusted_Median_Sale_Price"] = df.apply(adjust_price, axis=1)

# Select and reorder relevant columns
df = df[["Year", "observation_date", "Median Sale Price", "Inflation_Adjusted_Median_Sale_Price"]]

# Save to a new CSV file
output_path = "Median_Housing_Price_Adjusted.csv"
df.to_csv(output_path, index=False)

print("New CSV file 'Median_Housing_Price_Adjusted.csv' has been created successfully.")
