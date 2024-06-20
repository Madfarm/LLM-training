import sys
sys.path.insert(1, '/root/code-sandbox/LLM-training/code_execution_file_upload/model_generated_code/gene_dataset')
from settings import file_path

import pandas as pd
# Load data
df = pd.read_csv(file_path, sep='\t')
# Get the most common well_type
most_common_well_type = df['WELL_TYPE'].mode()[0]
print("The most common well_type is:", most_common_well_type)