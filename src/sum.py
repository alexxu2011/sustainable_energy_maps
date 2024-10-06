import csv
from collections import defaultdict

# File paths
input_file = "energy_consumption_ca_2022.csv"
output_file = "energy_consumption_ca_2022_sum.csv"

# Data structure to store the sum of MMBtu and Expenditure for each county
county_sums = defaultdict(lambda: {'consumption_mmbtu': 0, 'expenditure_usd': 0})

# Filter the data for Washington state and the year 2022
with open(input_file, mode='r') as infile:
    reader = csv.DictReader(infile)
    
    # Process each row
    for row in reader:
        if row['State Name'] == 'California' and row['Year'] == '2022':
            county = row['County Name']
            county_sums[county]['consumption_mmbtu'] += float(row['Consumption MMBtu'])
            county_sums[county]['expenditure_usd'] += float(row['Expenditure US Dollars'])

# Write the results to a new CSV file
with open(output_file, mode='w', newline='') as outfile:
    fieldnames = ['County Name', 'Total Consumption MMBtu', 'Total Expenditure US Dollars']
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    
    writer.writeheader()
    
    # Write each county's summed data to the new CSV
    for county, data in county_sums.items():
        writer.writerow({
            'County Name': county,
            'Total Consumption MMBtu': data['consumption_mmbtu'],
            'Total Expenditure US Dollars': data['expenditure_usd']
        })

print(f"Summarized data has been written to {output_file}")