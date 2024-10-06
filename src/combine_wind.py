import pandas as pd

# Load the three CSV files
file1 = "POWER_Regional_Monthly_2022_Wind_CA_Combined_Formatted.csv"
file2 = "POWER_Regional_Monthly_2022_Wind_OR_formatted.csv"
file3 = "POWER_Regional_Monthly_2022_Wind_WA_formatted.csv"

# Read the files into pandas dataframes
df1 = pd.read_csv(file1)
df2 = pd.read_csv(file2)
df3 = pd.read_csv(file3)

# Combine the three dataframes
combined_df = pd.concat([df1, df2, df3])

# Remove duplicate rows
combined_df = combined_df.drop_duplicates()

# Save the combined dataframe to a new CSV file
output_file = "POWER_Regional_Monthly_2022_Wind_WA_OR_CA_formatted.csv"
combined_df.to_csv(output_file, index=False)

print(f"Combined CSV file saved as {output_file}")