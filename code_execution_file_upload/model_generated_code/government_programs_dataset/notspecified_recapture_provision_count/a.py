import sys
sys.path.insert(1, '/root/code-sandbox/LLM-training/code_execution_file_upload/model_generated_code/government_programs_dataset')
from settings import file_path

import pandas as pd

# Load data
df = pd.read_csv(file_path)

# Find the state with the most "not specified"s in recapture provision
not_specified_df = df[df['Recapture Provisions'] == '(not specified)']
state_counts = not_specified_df['State'].value_counts()

# Print the state with the most "not specified"s
print(state_counts.index[0])

# Find the number of entries from that state with "Partial abatement" in the Abatement Method column
partial_abatement_df = df[df['Abatement Method'] == 'Partial abatement']
state_partial_abatement_counts = partial_abatement_df['State'].value_counts()

# Print the number of entries from that state with "Partial abatement" in the Abatement Method column
print(state_partial_abatement_counts.get(state_counts.index[0], 0))