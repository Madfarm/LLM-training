def calculate_charitable_items(original_purchase, original_price, num_people, charitable_item, charitable_item_cost, months_invested, monthly_growth):
    # Calculate the total amount spent on the original purchase
    total_spent = num_people * original_price

    # Calculate the total amount after investing for the specified number of months
    total_after_investing = total_spent * (1 + (monthly_growth / 100)) ** months_invested

    # Calculate the number of charitable items that could be purchased with the invested amount
    num_charitable_items = total_after_investing / charitable_item_cost

    # Round the final calculation to the nearest whole number
    num_charitable_items = round(num_charitable_items)

    # Return the result as a string
    return f"If the {num_people} people that {original_purchase} had instead used that money for {charitable_item} they could've made {num_charitable_items} {charitable_item}."

# Test the function with the given arguments
original_purchase = "bought Super Bowl tickets"
original_price = 8000
num_people = 61629
charitable_item = "houses"
charitable_item_cost = 183699
monthly_growth = 0.4064
months_invested = 36

result = calculate_charitable_items(original_purchase, original_price, num_people, charitable_item, charitable_item_cost, months_invested, monthly_growth)
print(result)