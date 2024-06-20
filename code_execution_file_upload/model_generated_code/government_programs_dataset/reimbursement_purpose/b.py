import sys
sys.path.insert(1, '/root/code-sandbox/LLM-training/code_execution_file_upload/model_generated_code/government_programs_dataset')
from settings import file_path
import pandas as pd

# Load data
df = pd.read_csv(file_path)

# Extract all entries that have more than $0 in the reimbursement column
df = df[df['Reimbursement'] > 0]

# Find the most common program purpose amongst these
most_common_program_purpose = df['Program Purpose'].mode()[0]

print(f"The most common program purpose amongst the entries with more than $0 in the reimbursement column is: {most_common_program_purpose}")