import pandas as pd

# Define the data
data = {
    "Brand": ["Levi's", "Wrangler", "Lee", "Calvin Klein"],
    "Price (USD)": [49.99, 52.50, 47.75, 51.00],
    "Durability (years)": [3, 4, 3.5, 4.2],
    "Number of Pockets": [5, 4, 5, 4]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Add American Eagle
df.loc[len(df.index)] = ["American Eagle", 47.85, 4.5, 4]

# Remove jeans with a durability of 3 years or less
df = df[df["Durability (years)"] > 3]

# Calculate the best value brand
df['Value'] = df['Durability (years)'] * df['Number of Pockets'] / df['Price (USD)']
best_value_brand = df.loc[df['Value'].idxmax()]

# Lower prices by 42% for your wife's jeans
df['Price (USD)'] *= 0.58
# Remove jeans with a durability of 3 years or less
df = df[df["Durability (years)"] > 3]
# Calculate the best value brand for your wife
df['Value'] = df['Durability (years)'] * df['Number of Pockets'] / df['Price (USD)']
best_value_brand_wife = df.loc[df['Value'].idxmax()]

# Lower prices by 74% for your kid's jeans
df['Price (USD)'] *= 0.26
# Ignore durability
df['Value'] = df['Number of Pockets'] / df['Price (USD)']
best_value_brand_kid = df.loc[df['Value'].idxmax()]

# Print the results
print("Best value brand for you:", best_value_brand["Brand"])
print("Best value brand for your wife:", best_value_brand_wife["Brand"])
print("Best value brand for your kid:", best_value_brand_kid["Brand"])