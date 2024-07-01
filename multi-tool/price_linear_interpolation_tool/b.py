def price_linear_interpolation(date1, price1, date2, price2, date3):
    # Check if date3 is between date1 and date2
    assert date1 <= date3 <= date2, "Date3 must be between date1 and date2"
    
    # Calculate the slope of the line passing through (date1, price1) and (date2, price2)
    slope = (price2 - price1) / (date2 - date1)
    
    # Calculate the price at date3 using the slope and date1, price1
    price3 = price1 + slope * (date3 - date1)
    
    return price3

# Usage
date1 = "July"
price1 = 1275
date2 = "October"
price2 = 1275
date3 = "September"
print(price_linear_interpolation(date1, price1, date2, price2, date3))