import csv

input_file = "data.csv"      # Your raw data file
output_file = "students.csv" # Cleaned output file

with open(input_file, newline='') as infile, open(output_file, 'w', newline='') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)
    header = next(reader)
    writer.writerow(header)
    n_cols = len(header)
    for row in reader:
        # Only write rows with the correct number of columns and not all empty
        if len(row) == n_cols and any(cell.strip() for cell in row):
            writer.writerow(row)