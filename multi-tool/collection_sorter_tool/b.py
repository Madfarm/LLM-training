def sort_collection(collection, criteria):
    # Check if the criteria exists on all items in the collection
    for item in collection:
        if criteria not in item:
            return "Error: Criteria does not exist on all items in the collection"

    # Sort the collection based on the criteria
    if criteria == "value":
        sorted_collection = sorted(collection, key=lambda x: x[criteria], reverse=True)
    elif criteria == "condition":
        condition_order = {"Mint": 0, "Excellent": 1, "Good": 2, "Fair": 3, "Poor": 4, "Damaged": 5}
        sorted_collection = sorted(collection, key=lambda x: condition_order[x[criteria]])
    else:
        return "Error: Criteria not recognized"

    return sorted_collection

# Demonstration 1: Sorting by value
pens = [
    {"name": "Pen 1", "value": 10, "condition": "Mint", "color": "Blue"},
    {"name": "Pen 2", "value": 5, "condition": "Excellent", "color": "Red"},
    {"name": "Pen 3", "value": 15, "condition": "Good", "color": "Green"}
]
print(sort_collection(pens, "value"))

# Demonstration 2: Sorting by condition
pens = [
    {"name": "Pen 1", "value": 10, "condition": "Mint", "color": "Blue"},
    {"name": "Pen 2", "value": 5, "condition": "Excellent", "color": "Red"},
    {"name": "Pen 3", "value": 15, "condition": "Good", "color": "Green"}
]
print(sort_collection(pens, "condition"))