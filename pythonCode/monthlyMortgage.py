import pandas as pd
import cpi
from io import StringIO

# Hard-coded CSV data as a multi-line string
data = """Year,Average 30-year fixed mortgage rate,Typical monthly mortgage payment
1971,7.54,141.65
1972,7.38,152.16
1973,8.04,192.09
1974,9.19,236.01
1975,9.05,253.94
1976,8.86,281.12
1977,8.85,310.56
1978,9.64,380.27
1979,11.20,485.67
1980,13.74,603.12
1981,16.67,771.64
1982,16.06,747.41
1983,13.24,678.37
1984,13.88,751.77
1985,11.85,685.72
1986,10.39,667.38
1987,10.40,759.93
1988,10.38,813.21
1989,10.25,863.30
1990,9.97,856.45
1991,9.09,778.50
1992,8.27,730.85
1993,7.17,684.88
1994,8.28,786.07
1995,7.86,773.12
1996,7.76,804.59
1997,7.57,816.66
1998,6.91,801.28
1999,7.46,892.19
2000,8.08,991.02
2001,7.01,922.24
2002,6.57,947.51
2003,5.89,910.67
2004,5.88,1032.91
2005,5.93,1126.09
2006,6.47,1228.69
2007,6.40,1225.74
2008,6.23,1128.32
2009,5.38,966.60
2010,4.86,941.22
2011,4.65,927.73
2012,3.88,919.97
2013,4.16,1036.54
2014,4.31,1132.72
2015,3.99,1122.10
2016,3.79,1136.01
2017,4.14,1252.35
2018,4.70,1349.60
2019,4.13,1242.42
2020,3.38,1161.32
2021,3.15,1316.71
2022,5.53,1973.12
2023,7.00,2270.15
2024,6.90,2207.36"""

# Create DataFrame from the hard-coded CSV data
df = pd.read_csv(StringIO(data))

# Set the base year for inflation adjustment
base_year = 2024

# Adjust the mortgage payment to 2024 dollars.
# Using January (month=1) for the CPI lookup.
df['Adjusted Mortgage Payment'] = df.apply(
    lambda row: cpi.inflate(row['Typical monthly mortgage payment'], row['Year'], to=base_year, month=1),
    axis=1
)

# Output the new CSV file to the root folder
output_csv = "monthlyMortgage_adjusted.csv"
df.to_csv(output_csv, index=False)

print("Adjusted CSV file created at:", output_csv)
