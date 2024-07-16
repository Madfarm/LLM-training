import random

# Starting value of 123 Bitcoin in 2021
starting_value = 123 * 3914967

# Number of years
years = 3

# Randomly lose or gain 1-5% every year
for _ in range(years):
    starting_value *= (1 + random.uniform(-0.05, 0.05))

# Current value of 123 Bitcoin
current_value = starting_value

print(f"The current value of 123 Bitcoin is {current_value:.2f} USD.")