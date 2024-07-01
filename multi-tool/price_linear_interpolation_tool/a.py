import datetime

def price_linear_interpolation(date1, price1, date2, price2, date3):
    # Convert dates to days of the year (assuming January 1st is day 1)
    day1 = (date1.month - 1) * 30 + date1.day
    day2 = (date2.month - 1) * 30 + date2.day
    day3 = (date3.month - 1) * 30 + date3.day

    # Calculate the slope of the line
    slope = (price2 - price1) / (day2 - day1)

    # Calculate the price for the given date
    price3 = price1 + slope * (day3 - day1)

    return price3

# Example usage:
date1 = datetime.date(2024, 7, 1)  # July 1st, 2024
price1 = 875  # Price in July
date2 = datetime.date(2024, 10, 1)  # October 1st, 2024
price2 = 1275  # Price in October
date3 = datetime.date(2024, 9, 1)  # September 1st, 2024

assert date1 <= date3 <= date2, "Date3 must be between date1 and date2"

price3 = price_linear_interpolation(date1, price1, date2, price2, date3)
print(f"The estimated price of a Korean Air flight from San Francisco to Seoul in September is: ${price3:.2f}")