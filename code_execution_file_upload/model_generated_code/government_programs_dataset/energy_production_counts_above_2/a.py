import sys
sys.path.insert(1, '/root/code-sandbox/LLM-training/code_execution_file_upload/model_generated_code/government_programs_dataset')
from settings import file_path
import pandas as pd

# Load data
df = pd.read_csv(file_path)

# Filter the data to only include entries with "Energy production" in the program purpose column
df_energy_production = df[df['Program Purpose'].str.contains('Energy production')]

# Group the data by state and count the number of entries with "Energy production" in the program purpose column
df_grouped = df_energy_production.groupby('State Name')['Program Purpose'].count()

# Create a dictionary with the state name as the key and the count of entries with "Energy production" in the program purpose column as the value
energy_production_counts = df_grouped.to_dict()

# Print the dictionary
print(energy_production_counts)