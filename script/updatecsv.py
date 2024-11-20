import pandas as pd

# Paths for the input and output files
input_file_path = "/home/floriane/Documents/16thExegesisDH/HTR_Paul_corpus/corpus/files_control.csv"
output_file_path = "/home/floriane/Documents/16thExegesisDH/HTR_Paul_corpus/corpus/updated_files_control.csv"

# Read the existing CSV file
existing_data = pd.read_csv(input_file_path)

# Define new repository and filename details
new_repository = "lefevre_Rm_001"
new_base_filename = "bsb11059254_"
new_start_index = 203
new_end_index = 284

# Generate new rows
new_rows = []
for i in range(new_start_index, new_end_index + 1):
    file_number = str(i).zfill(5)  # Format as 5-digit zero-padded number
    filename = f"{new_base_filename}{file_number}.xml"
    new_rows.append([new_repository, filename, "", "", "", "", ""])

# Create a DataFrame for new rows
new_data = pd.DataFrame(new_rows, columns=existing_data.columns)

# Append the new rows to the existing data
updated_data = pd.concat([existing_data, new_data], ignore_index=True)

# Save the updated data to a new CSV file
updated_data.to_csv(output_file_path, index=False)

output_file_path
