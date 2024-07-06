def calculate_charitable_impact(original_purchase, original_price, num_people, charitable_item, charitable_item_cost, months_invested, monthly_growth):
    total_spent = num_people * original_price
    total_invested = total_spent * (1 + monthly_growth) ** months_invested
    charitable_item_count = total_invested / charitable_item_cost
    return f"If the {num_people} people that {original_purchase} had instead used that money for {charitable_item} they could've made {round(charitable_item_count)} {charitable_item}."

original_purchase = "bought Super Bowl tickets"
original_price = 8000
num_people = 61629
charitable_item = "houses"
charitable_item_cost = 183699
months_invested = 36
monthly_growth = 0.4064

print(calculate_charitable_impact(original_purchase, original_price, num_people, charitable_item, charitable_item_cost, months_invested, monthly_growth))