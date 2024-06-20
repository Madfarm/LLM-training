import pandas as pd

file_path = "/root/code-sandbox/LLM-training/code-execution-file-upload/tested_datasets/scholars-dataset.csv"

# Load data
df = pd.read_csv(file_path)

# Extract entries with "Assistant" in their preferred title
assistant_titles = df[df['Preferred title']]

# Sort alphabetically
assistant_titles = assistant_titles.sort_values(by='Preferred title')

# Print the sorted entries
print(assistant_titles)