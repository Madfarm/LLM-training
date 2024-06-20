import sys
sys.path.insert(1, '/root/code-sandbox/LLM-training/code_execution_file_upload/model_generated_code/government_programs_dataset')
from settings import file_path
import pandas as pd

# Load data
df = pd.read_csv(file_path)

# Filter data to include only entries with "Energy production" in the program purpose column
energy_production_df = df[df['Program Purpose'].str.contains('Energy production')]

# Group by state and count the number of entries
state_counts = energy_production_df['State Name'].value_counts()[lambda x: x >= 2]

# Convert the counts to a dictionary
state_counts_dict = state_counts.to_dict()

# Print the dictionary
print(state_counts_dict)