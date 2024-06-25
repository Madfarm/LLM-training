import sys
sys.path.insert(1, '/root/code-sandbox/LLM-training/code_execution_file_upload/model_generated_code/gene_dataset')
from settings import file_path
import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv(file_path, sep='\t')

# Group the data by well type
grouped_data = df.groupby('WELL_TYPE')

# Create a scatter plot of the reproducibility
plt.figure(figsize=(10,6))
for well_type, data in grouped_data:
    plt.scatter(data['REPRODUCIBILITY'], data['CHEMBANK_ID'], label=well_type)

# Set the title and labels
plt.title('Reproducibility vs CHEMBANK ID')
plt.xlabel('Reproducibility')
plt.ylabel('CHEMBANK ID')

# Show the legend and plot
print('Plotting data')
plt.legend()
plt.show()