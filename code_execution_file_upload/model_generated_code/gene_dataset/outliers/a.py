import sys
sys.path.insert(1, '/root/code-sandbox/LLM-training/code_execution_file_upload/model_generated_code/gene_dataset')
from settings import file_path

# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv(file_path, sep='\t')

# Identify outliers in REPRODUCIBILITY
Q1 = df['REPRODUCIBILITY'].quantile(0.25)
Q3 = df['REPRODUCIBILITY'].quantile(0.75)
IQR = Q3 - Q1

outliers = df[(df['REPRODUCIBILITY'] < (Q1 - 1.5 * IQR)) | (df['REPRODUCIBILITY'] > (Q3 + 1.5 * IQR))]

# Print outliers
print(outliers)

# Plot histogram of REPRODUCIBILITY
plt.figure(figsize=(10,6))
plt.hist(df['REPRODUCIBILITY'], bins=50, label='REPRODUCIBILITY')
plt.title('Histogram of REPRODUCIBILITY')
plt.xlabel('REPRODUCIBILITY')
plt.ylabel('Frequency')
plt.legend()
plt.show()