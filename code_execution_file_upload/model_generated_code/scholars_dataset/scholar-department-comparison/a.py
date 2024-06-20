file_path = "/root/code-sandbox/LLM-training/code-execution-file-upload/tested_datasets/scholars-dataset.csv"

import pandas as pd

# Load data
df = pd.read_csv(file_path)

# Extract entries in the Restorative Sciences department and Kinesiology
restorative_sciences = df[df['Department'].str.contains('Restorative Sciences', na=False)]
kinesiology = df[df['Department'].str.contains('Kinesiology', na=False)]

# Count the number of entries with Professor in their position in each department
restorative_sciences_professors = restorative_sciences[restorative_sciences['Position'].str.contains('Professor', na=False)]
kinesiology_professors = kinesiology[kinesiology['Position'].str.contains('Professor', na=False)]
print(kinesiology_professors)

# Determine which department has more entries with Professor in their position
if len(restorative_sciences_professors) > len(kinesiology_professors):
    print(f"The Restorative Sciences department has more entries with Professor in their position, with {len(restorative_sciences_professors)} entries.")
elif len(kinesiology_professors) > len(restorative_sciences_professors):
    print(f"The Kinesiology department has more entries with Professor in their position, with {len(kinesiology_professors)} entries.")
else:
    print(f"Both departments have the same number of entries with Professor in their position, with {len(restorative_sciences_professors)} entries.")