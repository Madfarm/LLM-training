import sys
sys.path.insert(1, '/root/code-sandbox/LLM-training/code_execution_file_upload/model_generated_code/government_programs_dataset')
from settings import file_path
import pandas as pd

# Load data
df = pd.read_csv(file_path)

# Filter the data for Real Property Tax
real_property_tax_df = df[df['Applicable Taxes'].str.contains('Real Property Tax')]

# Convert Net Revenue Loss to numeric
real_property_tax_df['Net Revenue Loss'] = real_property_tax_df['Net Revenue Loss'].str.replace('$', '').str.replace(',', '').astype(float)

# Find the entry with the highest net revenue loss
max_net_revenue_loss_entry = real_property_tax_df.loc[real_property_tax_df['Net Revenue Loss'].idxmax()]

# Print the jurisdiction name of the entry with the highest net revenue loss
print(max_net_revenue_loss_entry['Jurisdiction Name'])