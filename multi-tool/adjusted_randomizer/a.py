import random

def adjusted_randomizer(options, odds):
    assert len(options) == len(odds), "Options and odds must be the same length"
    assert sum(odds) == 1, "Odds must add up to 1"
    return random.choices(options, weights=odds)[0]

# Example usage:
options = ["Iktos", "Atomwise", "Protai"]
odds = [0.45, 0.35, 0.2]
selected_company = adjusted_randomizer(options, odds)
print(selected_company)