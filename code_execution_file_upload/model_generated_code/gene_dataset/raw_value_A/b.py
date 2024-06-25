import sys
sys.path.insert(1, '/root/code-sandbox/LLM-training/code_execution_file_upload/model_generated_code/gene_dataset')
from settings import file_path
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv(file_path, sep='\t')

# Calculate correlation between raw_value_A and reproducibility
correlation = df['RAW_VALUE_A'].corr(df['REPRODUCIBILITY'])

# Print correlation
print("Correlation between raw_value_A and reproducibility is:", correlation)

# Plot scatter plot
plt.figure(figsize=(10,6))
sns.scatterplot(x='RAW_VALUE_A', y='REPRODUCIBILITY', data=df)
plt.title('Scatter Plot of raw_value_A vs reproducibility')
plt.xlabel('raw_value_A')
plt.ylabel('reproducibility')
plt.show()