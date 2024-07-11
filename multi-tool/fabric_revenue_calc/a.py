def fabric_revenue_calc(total_fabric, clothing_items):
    unusable_fabric = total_fabric * 0.1
    usable_fabric = total_fabric - unusable_fabric
    revenue = {}
    
    for item in clothing_items:
        item_name = item['name']
        item_fabric_required = item['fabric_required']
        item_price = item['price']
        
        num_items = int(usable_fabric / item_fabric_required)
        item_revenue = num_items * item_price
        revenue[item_name] = item_revenue
    
    return revenue

clothing_items = [
    {'name': 't-shirt', 'fabric_required': 50, 'price': 14.99},
    {'name': 'jacket', 'fabric_required': 150, 'price': 45.99},
    {'name': 'hat', 'fabric_required': 20, 'price': 4.99},
    {'name': 'cardigan', 'fabric_required': 175, 'price': 49.99}
]

total_fabric = 1000
print(fabric_revenue_calc(total_fabric, clothing_items))