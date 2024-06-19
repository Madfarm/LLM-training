file_path = "/root/code-sandbox/LLM-training/code-execution-file-upload/tested_datasets/scholars-dataset.csv"

import pandas as pd

# Load data
df = pd.read_csv(file_path)

# Extract entries in the Restorative Sciences department and Kinesiology
restorative_sciences = df[df['Department'].str.contains('Restorative Sciences', na=False)]
kinesiology = df[df['Department'].str.contains('Kinesiology', na=False)]

# Extract entries with Professor in their position
restorative_sciences_professor = restorative_sciences[restorative_sciences['Position'].str.contains('Professor', na=False)]
kinesiology_professor = kinesiology[kinesiology['Position'].str.contains('Professor', na=False)]

# Count the number of professors in each department
restorative_sciences_professor_count = len(restorative_sciences_professor)
kinesiology_professor_count = len(kinesiology_professor)

# Determine which department has more professors
if restorative_sciences_professor_count > kinesiology_professor_count:
    print(f"The Restorative Sciences department has more professors, with {restorative_sciences_professor_count} professors.")
elif kinesiology_professor_count > restorative_sciences_professor_count:
    print(f"The Kinesiology department has more professors, with {kinesiology_professor_count} professors.")
else:
    print(f"Both departments have the same number of professors, with {restorative_sciences_professor_count} professors.")