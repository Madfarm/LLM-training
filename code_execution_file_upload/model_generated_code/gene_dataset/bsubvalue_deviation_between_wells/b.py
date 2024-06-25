import sys
sys.path.insert(1, '/root/code-sandbox/LLM-training/code_execution_file_upload/model_generated_code/gene_dataset')
from settings import file_path
import pandas as pd

# Load data
df = pd.read_csv(file_path, sep='\t')

# Calculate the deviation of bsub_value_b for each well
deviation = df.groupby('WELL')['BSUB_VALUE_B'].std()

# Find the well with the least deviation
least_deviation_well = deviation.idxmin()

print(f"The well with the least deviation in its bsub_value_b is {least_deviation_well}.")