import csv

# Input and output file paths
input_file = 'energy_consumption_net_electricity_natural_gas_county.csv'  # Replace with the path to your CSV file
output_file = 'filtered_energy_consumption_net_electricity_natural_gas_county_ca.csv'   # Output file with filtered results

# Open the input CSV file
with open(input_file, 'r') as infile:
    reader = csv.reader(infile)
    
    # Get the header
    header = next(reader)
    
    # Filter rows for WA state and the year 2022
    filtered_rows = [header]  # Start with header row
    for row in reader:
        state_name = row[1]
        year = row[4]
        if state_name == "California" and year == "2022":
            filtered_rows.append(row)

# Write the filtered rows to a new CSV file
with open(output_file, 'w', newline='') as outfile:
    writer = csv.writer(outfile)
    writer.writerows(filtered_rows)

print(f"Filtered data written to {output_file}")