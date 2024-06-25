import sys
sys.path.insert(1, '/root/code-sandbox/LLM-training/code_execution_file_upload/model_generated_code/gene_dataset')
from settings import file_path
import pandas as pd
# Load data
df = pd.read_csv(file_path, sep='\t')
# Calculate correlation between raw_value_A and reproducibility
correlation = df['RAW_VALUE_A'].corr(df['REPRODUCIBILITY'])
print("Correlation between raw_value_A and reproducibility is:", correlation)