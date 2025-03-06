import pandas as pd

# Load the data into a DataFrame (replace 'data.csv' with your file name or data source)
df = pd.read_csv(r'median home sale price\adjusted\Median_Housing_Price_Adjusted.csv')

# Filter rows: keep only those rows where observation_date ends with '01-01'
filtered_df = df[df['observation_date'].str.endswith('01-01')]

# Optionally, save the filtered DataFrame to a new CSV file
filtered_df.to_csv('filtered_data.csv', index=False)

# Print the filtered DataFrame
print(filtered_df)
