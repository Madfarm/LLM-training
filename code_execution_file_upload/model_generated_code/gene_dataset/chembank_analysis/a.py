import sys
sys.path.insert(1, '/root/code-sandbox/LLM-training/code_execution_file_upload/model_generated_code/gene_dataset')
from settings import file_path
import pandas as pd

# Load data
df = pd.read_csv(file_path, sep='\t')

# Count unique chembank IDs
unique_chembank_ids = df['CHEMBANK_ID'].nunique()

print("Number of unique chembank IDs:", unique_chembank_ids)