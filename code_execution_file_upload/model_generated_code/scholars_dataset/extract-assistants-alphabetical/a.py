import pandas as pd

file_path = "/root/code-sandbox/LLM-training/code-execution-file-upload/tested_datasets/scholars-dataset.csv"

# Load data
df = pd.read_csv(file_path)

# Extract entries with "Assistant" in their preferred title, handling NaN values
assistant_entries = df[df['Preferred title'].str.contains('Assistant', na=False)]

# Sort alphabetically by first name
assistant_entries = assistant_entries.sort_values(by='First name')

# Print the results
print(assistant_entries)