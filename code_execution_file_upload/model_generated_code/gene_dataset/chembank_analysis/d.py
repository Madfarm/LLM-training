import sys
sys.path.insert(1, '/root/code-sandbox/LLM-training/code_execution_file_upload/model_generated_code/gene_dataset')
from settings import file_path
import pandas as pd

# Load data
df = pd.read_csv(file_path, sep='\t')

# Find the unique chembank with the highest average raw_value_C
chembank_id = df.groupby('CHEMBANK_ID')['RAW_VALUE_C'].mean().idxmax()

print(f"The unique chembank with the highest average raw_value_C is {chembank_id}.")