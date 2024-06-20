import sys
sys.path.insert(1, '/root/code-sandbox/LLM-training/code_execution_file_upload/model_generated_code/government_programs_dataset')
from settings import file_path
import pandas as pd

# Load data
df = pd.read_csv(file_path)

# Filter for Real Property Tax
df = df[df['Applicable Taxes'].str.contains('Real Property Tax', na=False)]

# Convert Net Revenue Loss to numeric value
df['Net Revenue Loss'] = df['Net Revenue Loss'].str.replace('$', '').str.replace(',', '').astype(float)

# Find the jurisdiction with the highest net revenue loss
max_loss_jurisdiction = df.loc[df['Net Revenue Loss'].idxmax()]

# Print the jurisdiction name
print(max_loss_jurisdiction['Jurisdiction Name'])