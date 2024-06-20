import pandas as pd

file_path = "/root/code-sandbox/LLM-training/code-execution-file-upload/tested_datasets/scholars-dataset.csv"

# Load data
df = pd.read_csv(file_path)

# Find and output each entry where Preferred Title and Position differ
differing_entries = df[df['Preferred title'] != df['Position']]
print("Entries where Preferred Title and Position differ:")
print(differing_entries)

# Count the number of entries in which they differ
count = len(differing_entries)
print("Number of entries where Preferred Title and Position differ:", count)