import sys
sys.path.insert(1, '/root/code-sandbox/LLM-training/code_execution_file_upload/model_generated_code/scholars_dataset')
from settings import file_path

import pandas as pd

import pandas as pd

# Load data
df = pd.read_csv(file_path)

# Filter departments that contain the word "Dentistry"
dentistry_departments = df[df['Department'].str.contains('Dentistry', case=False)]

# Filter dentists with last names that start with the letter C
dentists_with_c = dentistry_departments[dentistry_departments['Last name'].str.startswith('C', na=False)]

# Print the results
print(dentists_with_c)