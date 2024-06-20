import sys
sys.path.insert(1, '/root/code-sandbox/LLM-training/code_execution_file_upload/model_generated_code/government_programs_dataset')
from settings import file_path
import pandas as pd

# Load data
df = pd.read_csv(file_path)

# Filter the data for Nevada and "Partial abatement"
nevada_df = df[df['State'] == 'NV']
partial_abatement_df = nevada_df[nevada_df['Abatement Method'] == 'Partial abatement']

# Print the number of entries
print(len(partial_abatement_df))