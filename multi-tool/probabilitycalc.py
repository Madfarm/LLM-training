# Define the total number of flavors
total_flavors = 50

# Probability of drawing the same flavor twice without removing any beans
probability_same_flavor_twice = (1 / total_flavors) * (1 / total_flavors)

# Convert probability to percentage
probability_same_flavor_twice_percentage = probability_same_flavor_twice * 100
print(f"The probability of grabbing the same flavor twice is {probability_same_flavor_twice_percentage}%")