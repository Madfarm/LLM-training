import random

def generate_order(products):
    # Check if the input is valid
    if not isinstance(products, list):
        raise TypeError("The input should be a list.")
    for product in products:
        if not isinstance(product, dict) or "name" not in product or "price" not in product or "quantity" not in product:
            raise ValueError("Each product should be a dictionary containing 'name', 'price', and 'quantity'.")
        if not isinstance(product["name"], str) or not isinstance(product["price"], (int, float)) or not isinstance(product["quantity"], int):
            raise ValueError("The 'name' should be a string, the 'price' and 'quantity' should be numbers.")
        if product["quantity"] <= 0:
            raise ValueError("The 'quantity' should be a positive integer.")

    # Generate a random order number
    order_number = random.randint(10000, 99999)

    # Calculate the total price
    total_price = sum(product["price"] * product["quantity"] for product in products)

    # Create a dictionary with the order number, total price, and a list of products with their quantities
    result = {
        "order_number": order_number,
        "total_price": total_price,
        "products": [
            {
                "name": product["name"],
                "quantity": product["quantity"]
            }
            for product in products
        ]
    }

    return result

# Example usage:
products = [
    {
        "name": "Product 1",
        "price": 10,
        "quantity": 3
    },
    {
        "name": "Product 2",
        "price": 20,
        "quantity": 2
    },
    {
        "name": "Product 3",
        "price": 5,
        "quantity": 4
    }
]

try:
    result = generate_order(products)
    print(result)
except Exception as e:
    print(f"Error: {e}")