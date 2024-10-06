import pandas as pd

# Load the two CSV files into dataframes
file1 = 'POWER_Regional_Monthly_2022_wind_CA_West_formatted.csv'
file2 = 'POWER_Regional_Monthly_2022_wind_CA_East_formatted.csv'

# Read the CSV files
df1 = pd.read_csv(file1)
df2 = pd.read_csv(file2)

# Concatenate the two dataframes
combined_df = pd.concat([df1, df2])

# Remove duplicate rows based on all columns
combined_df.drop_duplicates(inplace=True)

# Save the result to a new CSV file
output_file = 'POWER_Regional_Monthly_2022_Wind_CA_Combined_Formatted.csv'
combined_df.to_csv(output_file, index=False)

print(f'Combined file saved as {output_file}')