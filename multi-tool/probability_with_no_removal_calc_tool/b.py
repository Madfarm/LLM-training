import random

def probability_with_no_removal_calc(set, num_picks):
    # Define the set of flavors
    flavors = list(set.keys())

    # Calculate the probability of picking the same flavor twice without removing
    probability = (1 / len(flavors)) * (1 / len(flavors))

    # Convert probability to percentage
    probability_percentage = probability * 100

    # Pick two flavors at random without removing
    picks = random.choices(flavors, k=num_picks)

    # Output the picks and probability
    print(f"Picks: {picks}")
    print(f"Probability of picking the same flavor twice without removing: {probability_percentage}%")

# Define the set of flavors
set = {
    "Top Banana": 1,
    "Wet Dog": 1,
    "Licorice": 1,
    "Burnt Rubber": 1
}

# Execute the function with 2 as the number of picks
probability_with_no_removal_calc(set, 2)