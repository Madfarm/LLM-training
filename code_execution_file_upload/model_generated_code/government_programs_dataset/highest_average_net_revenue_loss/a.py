import sys
sys.path.insert(1, '/root/code-sandbox/LLM-training/code_execution_file_upload/model_generated_code/government_programs_dataset')
from settings import file_path
import pandas as pd

# Load the CSV file
df = pd.read_csv(file_path)

# Convert the 'Net Revenue Loss' column to numeric values
df['Net Revenue Loss'] = pd.to_numeric(df['Net Revenue Loss'].str.replace('$', '').str.replace(',', ''), errors='coerce')

# Group the data by 'State Name' and calculate the average 'Net Revenue Loss'
average_loss = df.groupby('State Name')['Net Revenue Loss'].mean()

# Find the state with the highest average 'Net Revenue Loss'
highest_loss_state = average_loss.idxmax()

# Print the state with the highest average 'Net Revenue Loss'
print(f"The state with the highest average net revenue loss is {highest_loss_state}.")