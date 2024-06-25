import sys
sys.path.insert(1, '/root/code-sandbox/LLM-training/code_execution_file_upload/model_generated_code/scholars_dataset')
from settings import file_path
import pandas as pd

# Load data
df = pd.read_csv(file_path)

# Create a dictionary to store the count of missing Overview for each Department
missing_overview_count = {}

# Iterate over each row in the dataframe
for index, row in df.iterrows():
    # Check if the Overview is missing
    if pd.isna(row['Overview']):
        # Get the Department
        department = row['Department']
        # If the Department is already in the dictionary, increment the count
        if department in missing_overview_count:
            missing_overview_count[department] += 1
        # If the Department is not in the dictionary, add it with a count of 1
        else:
            missing_overview_count[department] = 1

# Print the dictionary
print(missing_overview_count)

print(df.columns)