import pandas as pd
import cpi

# Specify the input file path
file_path = r"Original CSV Files\VisualizationTwo\monthlyMortgage.csv"

# Read the CSV file
df = pd.read_csv(file_path)

# Strip any extra whitespace from column names
df.columns = df.columns.str.strip()

# Ensure the Year, mortgage rate, and monthly payment columns are numeric.
df['Year'] = pd.to_numeric(df['Year'], errors='coerce')
df['Average 30-year fixed mortgage rate'] = pd.to_numeric(df['Average 30-year fixed mortgage rate'], errors='coerce')

# Remove any commas from the payment and convert to float
df['Typical monthly mortgage payment'] = (
    df['Typical monthly mortgage payment']
    .replace({r',': ''}, regex=True)
    .astype(float)
)

# Filter the DataFrame to only include years from 1990 to 2023
df = df[(df['Year'] >= 1990) & (df['Year'] <= 2023)]

# Update CPI data to ensure we have the latest values
cpi.update()

# Define a function to adjust the monthly payment for inflation:
# Convert the monthly payment to an annual amount, inflate to 2023 dollars, then convert back to a monthly figure.
def adjust_monthly_payment(row):
    annual_payment = row['Typical monthly mortgage payment'] * 12
    inflated_annual = cpi.inflate(annual_payment, int(row['Year']), to=2023)
    return inflated_annual / 12

# Apply the inflation adjustment to create a new column
df['Inflation_Adjusted_Monthly_Payment'] = df.apply(adjust_monthly_payment, axis=1)

# Define the output file path
output_file = r"Original CSV Files\VisualizationTwo\monthlyMortgage_Adjusted.csv"

# Save the updated DataFrame to a new CSV file
df.to_csv(output_file, index=False)

print(f"CSV file '{output_file}' has been created successfully.")
