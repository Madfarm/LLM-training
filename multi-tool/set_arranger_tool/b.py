import itertools

def set_arranger(lst):
    return list(itertools.permutations(lst))

funko_pops = ['Lucario', 'Grookey', 'Umbreon', 'Luxray', 'Wooloo', 'Aipom']
combinations = set_arranger(funko_pops)

# Randomly select one combination
import random
selected_combination = random.choice(combinations)

print("Selected Combination:", selected_combination)