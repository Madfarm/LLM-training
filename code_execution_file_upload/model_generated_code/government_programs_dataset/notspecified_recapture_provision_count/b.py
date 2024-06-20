import sys
sys.path.insert(1, '/root/code-sandbox/LLM-training/code_execution_file_upload/model_generated_code/government_programs_dataset')
from settings import file_path
# Import necessary libraries
import pandas as pd

# Load the CSV file
df = pd.read_csv(file_path)

# Find the state with the most "not specified" recapture provisions
state_with_most_not_specified = df['State'][df['Recapture Provisions'] == '(not specified)'].value_counts().idxmax()

print("The state with the most 'not specified' recapture provisions is: ", state_with_most_not_specified)