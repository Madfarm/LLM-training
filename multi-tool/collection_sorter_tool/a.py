def sort_collection(collection, criteria):
    # Check if the criteria exists on all items in the collection
    if not all(criteria in item for item in collection):
        return "Error: Criteria does not exist on all items in the collection"
    
    # Sort the collection based on the criteria
    if criteria == "condition":
        # Define the order of the condition
        condition_order = {"Mint": 0, "Excellent": 1, "Good": 2, "Fair": 3, "Poor": 4, "Damaged": 5}
        collection.sort(key=lambda x: condition_order[x[criteria]])
    else:
        collection.sort(key=lambda x: x[criteria], reverse=True)
    
    return collection

# Demonstration 1: Sorting by value
pens = [
    {"name": "Pen 1", "value": 10, "condition": "Mint", "color": "Blue"},
    {"name": "Pen 2", "value": 5, "condition": "Excellent", "color": "Red"},
    {"name": "Pen 3", "value": 15, "condition": "Good", "color": "Green"}
]
sorted_pens = sort_collection(pens, "value")
print(sorted_pens)

# Demonstration 2: Sorting by condition
sorted_pens = sort_collection(pens, "condition")
print(sorted_pens)