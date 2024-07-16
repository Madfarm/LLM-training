import random

def calculate_value(starting_value, years):
    value = starting_value
    for _ in range(years):
        value *= (1 + random.uniform(-0.05, 0.05))
    return value

starting_value = 3914967
years = 3
current_value = calculate_value(starting_value, years)
print(f"The current value of 123 Bitcoin is {current_value}")