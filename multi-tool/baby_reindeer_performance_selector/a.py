import random

# List of actors and actresses from Baby Reindeer with descriptions of their performances
performances = [
    {"name": "Richard Gadd", "description": "Excellent performance as Donny, conveying the character's flaws and vulnerabilities"},
    {"name": "Amy Gunning", "description": "Instantly able to switch from childlike naivete to heart-wrenching melancholy, sexual aggression, and outright violence"},
]

# Randomly select one of the actors/actresses
selected_performance = random.choice(performances)

# Print the selected performance
print(f"Selected Performance: {selected_performance['name']}")
print(f"Description: {selected_performance['description']}")