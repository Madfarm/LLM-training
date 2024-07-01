import random

def probability_with_no_removal_calc(set, num_picks):
    # Calculate the total number of items in the set
    total_items = sum(set.values())
    
    # Calculate the probability of picking the same item twice
    probability = (1 / total_items) * (1 / total_items)
    
    # Convert probability to percentage
    probability_percentage = probability * 100
    
    # Pick items from the set without removing them
    picks = []
    for _ in range(num_picks):
        pick = random.choice(list(set.keys()))
        picks.append(pick)
    
    # Calculate the probability of the picked items
    picked_probability = 1
    for pick in picks:
        picked_probability *= (set[pick] / total_items)
    
    # Convert picked probability to percentage
    picked_probability_percentage = picked_probability * 100
    
    # Print the results
    print(f"The picked items are: {picks}")
    print(f"The probability of the picked items is {picked_probability_percentage}%")

# Define the set of items
set = {
    "Top Banana": 1,
    "Wet Dog": 1,
    "Licorice": 1,
    "Burnt Rubber": 1
}

# Define the number of picks
num_picks = 2

# Call the function
probability_with_no_removal_calc(set, num_picks)