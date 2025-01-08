import csv
import os
import json

# Function to convert CSV to JSONL
def convert_csv_to_jsonl(csv_file_path, jsonl_file_path):
    with open(csv_file_path, mode='r', encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file)
        with open(jsonl_file_path, mode='w', encoding='utf-8') as jsonl_file:
            for row in reader:
                # Skip empty rows
                if any(row.values()):
                    jsonl_file.write(json.dumps(row) + '\n')
                else:
                    print(f"Skipping empty row: {row}")

# List of CSV files to convert
csv_files = [
    "datasets/nfl_passing.csv",
    "datasets/nfl_rushing.csv",
    "datasets/nfl_receiving.csv",
   
]

# Convert each CSV file to JSONL
for csv_file in csv_files:
    jsonl_file = os.path.splitext(csv_file)[0] + '.jsonl'  # Change extension to .jsonl
    convert_csv_to_jsonl(csv_file, jsonl_file)
    print(f"Converted {csv_file} to {jsonl_file}") 