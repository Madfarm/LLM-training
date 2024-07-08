import pandas as pd

# Define the data
data = {
    "Brand": ["Levi's", "Wrangler", "Lee", "Calvin Klein", "American Eagle"],
    "Price (USD)": [49.99, 52.50, 47.75, 51.00, 47.85],
    "Durability (years)": [3, 4, 3.5, 4.2, 4.5],
    "Number of Pockets": [5, 4, 5, 4, 4]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Remove rows with durability less than or equal to 3
df = df[df["Durability (years)"] > 3]

# Calculate the best value brand
best_value_brand = df.loc[df["Price (USD)"] / df["Durability (years)"] / df["Number of Pockets"] == df["Price (USD)"] / df["Durability (years)"] / df["Number of Pockets"].min()]

# Print the best value brand
print("Best value brand:", best_value_brand["Brand"].values[0])

# Calculate the best value brand for your wife
df_wife = df.copy()
df_wife["Price (USD)"] = df_wife["Price (USD)"] * 0.58
df_wife = df_wife[df_wife["Durability (years)"] > 3]
best_value_brand_wife = df_wife.loc[df_wife["Price (USD)"] / df_wife["Durability (years)"] / df_wife["Number of Pockets"] == df_wife["Price (USD)"] / df_wife["Durability (years)"] / df_wife["Number of Pockets"].min()]

# Print the best value brand for your wife
print("Best value brand for your wife:", best_value_brand_wife["Brand"].values[0])

# Calculate the best value brand for your kid
df_kid = df.copy()
df_kid["Price (USD)"] = df_kid["Price (USD)"] * 0.26
best_value_brand_kid = df_kid.loc[df_kid["Price (USD)"] / df_kid["Number of Pockets"] == df_kid["Price (USD)"] / df_kid["Number of Pockets"].min()]

# Print the best value brand for your kid
print("Best value brand for your kid:", best_value_brand_kid["Brand"].values[0])