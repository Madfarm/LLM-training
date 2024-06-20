import sys
sys.path.insert(1, '/root/code-sandbox/LLM-training/code_execution_file_upload/model_generated_code/government_programs_dataset')
from settings import file_path

# Import necessary libraries
import pandas as pd
import numpy as np

# Load the CSV file
df = pd.read_csv(file_path)

# Convert the 'Gross Revenue Loss' column to numeric
df['Gross Revenue Loss'] = df['Gross Revenue Loss'].replace({r'[^\d.]+': ''}, regex=True).apply(pd.to_numeric, errors='coerce')

# Filter the data for Missouri
missouri_df = df[df['State'] == 'Missouri']

# Calculate the mean, median, and standard deviation of the 'Gross Revenue Loss' column
mean = missouri_df['Gross Revenue Loss'].mean()
median = missouri_df['Gross Revenue Loss'].median()
std_dev = missouri_df['Gross Revenue Loss'].std()

# Create a dictionary with the results
result = {
    'mean': mean,
    'median': median,
    'std_dev': std_dev
}

# Print the result
print(result)
