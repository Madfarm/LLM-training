import random

def adjusted_randomizer(options, odds):
    if len(options) != len(odds):
        raise ValueError("The number of options and odds must be the same.")
    if sum(odds) != 1:
        raise ValueError("The odds must add up to 1.")
    random_number = random.random()
    cumulative_sum = 0
    for option, odd in zip(options, odds):
        cumulative_sum += odd
        if random_number <= cumulative_sum:
            return option
    return options[-1]

# Test the function
options = ["Company A", "Company B", "Company C"]
odds = [0.45, 0.35, 0.2]
print(adjusted_randomizer(options, odds))