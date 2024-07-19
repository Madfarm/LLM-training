import random

def place_order(products):
    # Validation
    for product in products:
        if not all(key in product for key in ('name', 'price')):
            return {"Error": "Invalid input data. Each product must have 'name', 'price', and 'quantity'."}  
        elif not isinstance(product.get('price', None), (int, float)) or product.get('price', None) <= 0:
            return {"Error": "Invalid 'price' value. It must be a positive number."}   
        elif 'quantity' not in product or not isinstance(product.get('quantity', None), int) or product.get('quantity', None) <= 0:
            return {"Error": "Invalid 'quantity' value. It must be a positive integer."}        
    # Calculate total price
    total_price = sum(product['price'] * product['quantity'] for product in products)
    
    # Generate a random order number
    order_number = random.randint(10000, 99999)    
    # Creating the final dictionary
    order_details = {        "order_number": order_number,        "total_price": total_price,        "products": []    }
    
    for product in products:        
         order_details['products'].append({"name": product['name'], "quantity": product['quantity']})   
    
    return order_details

# Example to test the function    
products_list = [        {'name': 'Pencil', 'price': 5.0},  
        {'name': 'Eraser', 'price': 1.0, 'quantity': 3},  
        {'name': 'Pen', 'price': 7.5, 'quantity': 4}    ]
result = place_order(products_list)
print(result)