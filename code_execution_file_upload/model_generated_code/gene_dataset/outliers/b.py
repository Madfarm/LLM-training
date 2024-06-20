import sys
sys.path.insert(1, '/root/code-sandbox/LLM-training/code_execution_file_upload/model_generated_code/gene_dataset')
from settings import file_path
import pandas as pd
# Load data
df = pd.read_csv(file_path, sep='\t')
# Print the summary of the data
print("Number of rows and columns in the data:", df.shape)
print("Columns of the data are:", len(df.columns))
print("Columns of the data are:", df.columns)
print("Datatype of the columns are:", df.dtypes)
print("Data sample from file:")
print(df.head())
# Check for outliers in reproducibility
print("Outliers in reproducibility:")
print(df[df['REPRODUCIBILITY'] > 1.5])
print(df[df['REPRODUCIBILITY'] < 0.5])