import sys
sys.path.insert(1, '/root/code-sandbox/LLM-training/code_execution_file_upload/model_generated_code/government_programs_dataset')
from settings import file_path
import pandas as pd

# Load data
df = pd.read_csv(file_path)

# Convert 'Net Revenue Loss' column to numeric
df['Net Revenue Loss'] = pd.to_numeric(df['Net Revenue Loss'].str.replace('$', '').str.replace(',', ''))

# Group by 'State' and calculate average 'Net Revenue Loss'
average_loss = df.groupby('State')['Net Revenue Loss'].mean()

# Find the state with the highest average 'Net Revenue Loss'
max_loss_state = average_loss.idxmax()

print(f"The state with the highest average net revenue loss is {max_loss_state}")