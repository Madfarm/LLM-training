import sys
sys.path.insert(1, '/root/code-sandbox/LLM-training/code_execution_file_upload/model_generated_code/gene_dataset')
from settings import file_path
# Import necessary libraries
import pandas as pd

# Load the CSV file
df = pd.read_csv(file_path, sep='\t')

# Calculate the average raw_value_C for each unique chembank
average_raw_value_C = df.groupby('CHEMBANK_ID')['RAW_VALUE_C'].mean()

# Find the chembank with the highest average raw_value_C
max_chembank = average_raw_value_C.idxmax()

# Print the result
print("The chembank with the highest average raw_value_C is: ", max_chembank)