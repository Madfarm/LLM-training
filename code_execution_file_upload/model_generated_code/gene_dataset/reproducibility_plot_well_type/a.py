import sys
sys.path.insert(1, '/root/code-sandbox/LLM-training/code_execution_file_upload/model_generated_code/gene_dataset')
from settings import file_path
import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv(file_path, sep='\t')

# Group data by well type
df_grouped = df.groupby('WELL_TYPE')

# Create a scatterplot of reproducibility for each well type
for well_type, group in df_grouped:
    plt.scatter(group['REPRODUCIBILITY'], group['COMPOSITE_Z'], label=well_type)

# Set title and labels
plt.title('Reproducibility vs Composite Z Score')
plt.xlabel('Reproducibility')
plt.ylabel('Composite Z Score')

# Show legend
plt.legend()

# Show plot
print('Plotting data')
plt.show()

