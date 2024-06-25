import sys
sys.path.insert(1, '/root/code-sandbox/LLM-training/code_execution_file_upload/model_generated_code/scholars_dataset')
from settings import file_path
import pandas as pd

# Load data
df = pd.read_csv(file_path)

# Count the number of rows where Overview is NaN
overview_nan_count = df['Overview'].isna().sum()

# Create a dictionary with department as key and count of NaN Overview as value
department_nan_count = df.groupby('Department')['Overview'].isna().sum().to_dict()

print(f"Number of entries with NaN Overview: {overview_nan_count}")
print("Number of entries with NaN Overview by Department:")
print(department_nan_count)

