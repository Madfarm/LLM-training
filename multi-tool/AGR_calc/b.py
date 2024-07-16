import random

def calculate_value(starting_value, years):
    value = starting_value
    for _ in range(years):
        value *= (1 + random.uniform(-0.05, 0.05))
    return value

def AGR_calc(starting_value, ending_value, years):
    AGR = ((ending_value / starting_value)**(1/years)) - 1
    return f"The annualized growth rate for this asset is {AGR*100}%"

starting_value = 3914967
years = 3
ending_value = calculate_value(starting_value, years)
print(AGR_calc(starting_value, ending_value, years))