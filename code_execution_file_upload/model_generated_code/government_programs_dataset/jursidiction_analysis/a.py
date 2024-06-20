import sys
sys.path.insert(1, '/root/code-sandbox/LLM-training/code_execution_file_upload/model_generated_code/government_programs_dataset')
from settings import file_path
import pandas as pd

# Load data
df = pd.read_csv(file_path)

# Find the most commonly occurring jurisdiction name in Colorado
colorado_df = df[df['State'] == 'CO']
most_common_jurisdiction = colorado_df['Jurisdiction Name'].value_counts().index[0]

print(f"The most commonly occurring jurisdiction name in Colorado is {most_common_jurisdiction}.")