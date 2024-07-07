import itertools
import random

def set_arranger(lst):
    return list(itertools.permutations(lst))

# Test the function
pokemon_funko_pops = ['Lucario', 'Grookey', 'Umbreon', 'Luxray', 'Wooloo', 'Aipom']
combinations = set_arranger(pokemon_funko_pops)

# Randomly select a combination
selected_combination = random.choice(combinations)
print("Selected Combination:", selected_combination)