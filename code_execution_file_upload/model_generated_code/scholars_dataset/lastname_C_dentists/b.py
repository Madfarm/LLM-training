import sys
sys.path.insert(1, '/root/code-sandbox/LLM-training/code_execution_file_upload/model_generated_code/scholars_dataset')
from settings import file_path
import pandas as pd

# Load data
df = pd.read_csv(file_path)

# Filter rows where department contains 'Dentistry' and last name starts with 'C'
dentists_with_last_name_c = df[df['Department'].str.contains('Dentistry', na=False) & df['Last name'].str.startswith('C', na=False)]

# Find the longest first name
longest_first_name = max(dentists_with_last_name_c['First name'].str.len())

# Print the results
print("The longest first name among these dentists is:", longest_first_name)