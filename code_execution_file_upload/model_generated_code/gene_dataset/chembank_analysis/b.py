import sys
sys.path.insert(1, '/root/code-sandbox/LLM-training/code_execution_file_upload/model_generated_code/gene_dataset')
from settings import file_path
import pandas as pd
# Load data
df = pd.read_csv(file_path, sep='\t')
# Get unique CHEMBANK_IDs
unique_chembank_ids = df['CHEMBANK_ID'].unique()
# Print the number of unique CHEMBANK_IDs
print("Number of unique CHEMBANK_IDs:", len(unique_chembank_ids))