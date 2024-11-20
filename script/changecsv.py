import csv

# Define the repository and base filename details
repository = "Bucer_Eph_001"
base_filename = "bsb00035303_"
start_index = 1
end_index = 224
output_path = "/home/floriane/Documents/16thExegesisDH/HTR_Paul_corpus/corpus/files_control.csv"

# Define the headers for the CSV
headers = [
    "Repository",
    "Filename",
    "Presegmented",
    "SGM Manually Corrected",
    "SGM GitHub Corrected",
    "Transcript",
    "Transcript Manually Corrected"
]

# Generate rows for the CSV file
rows = []
for i in range(start_index, end_index + 1):
    file_number = str(i).zfill(5)  # Format as 5-digit zero-padded number
    filename = f"{base_filename}{file_number}.xml"
    rows.append([repository, filename, "", "", "", "", ""])

# Write the rows to a new CSV file
with open(output_path, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(headers)  # Write the header row
    writer.writerows(rows)    # Write the data rows

output_path
