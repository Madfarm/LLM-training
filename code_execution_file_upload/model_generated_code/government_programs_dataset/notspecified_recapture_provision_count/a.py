import sys
sys.path.insert(1, '/root/code-sandbox/LLM-training/code_execution_file_upload/model_generated_code/government_programs_dataset')
from settings import file_path
import pandas as pd

# Load data
df = pd.read_csv(file_path)

# Find the state with the most "not specified"s in recapture provision
most_not_specified_state = df['State'][df['Recapture Provisions'] == '(not specified)'].value_counts().idxmax()

print(f"The state with the most 'not specified's in recapture provision is {most_not_specified_state}")