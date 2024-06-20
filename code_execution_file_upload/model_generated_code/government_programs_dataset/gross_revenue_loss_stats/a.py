import sys
sys.path.insert(1, '/root/code-sandbox/LLM-training/code_execution_file_upload/model_generated_code/government_programs_dataset')
from settings import file_path

import pandas as pd


# Load data
df = pd.read_csv(file_path)

# Convert gross revenue loss column to numerical
df['Gross Revenue Loss'] = df['Gross Revenue Loss'].str.replace('$', '').str.replace(',', '').astype(float)

# Filter data for Missouri
df_mo = df[df['State Name'] == 'Missouri']

# Calculate mean, median, and standard deviation for gross revenue loss
mean = df_mo['Gross Revenue Loss'].mean()
median = df_mo['Gross Revenue Loss'].median()
std = df_mo['Gross Revenue Loss'].std()

# Output dictionary
output = {'mean': mean, 'median': median, 'standard deviation': std}

print(output)