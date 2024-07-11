import random

def fabric_revenue_calc(total_fabric, clothing_items):
    # Randomly assume 1-10% of the total fabric will be unusable
    unusable_fabric = total_fabric * (random.randint(1, 10) / 100)
    usable_fabric = total_fabric - unusable_fabric

    # Calculate the revenue for each item
    revenue = {}
    for item in clothing_items:
        name, fabric_required, price = item
        num_items = usable_fabric // fabric_required
        revenue[name] = num_items * price

    return revenue

# Test the function
total_fabric = 1000
clothing_items = [
    ["t-shirt", 50, 14.99],
    ["jacket", 150, 45.99],
    ["hat", 20, 4.99],
    ["cardigan", 175, 49.99]
]

print(fabric_revenue_calc(total_fabric, clothing_items))