import datetime
from dateutil.relativedelta import relativedelta

def car_depreciation(car_info, target_date=None):
    # Extract the car's name, value, and date from the input dictionary
    car_name = car_info['name']
    car_value = car_info['value']
    car_date = car_info['date']
    
    # If a target date is not provided, use today's date
    if target_date is None:
        target_date = datetime.datetime.now()
    else:
        target_date = datetime.datetime.strptime(target_date, '%Y-%m-%d')
    
    # Calculate the difference in years between the two dates
    years_diff = relativedelta(target_date, car_date).years
    
    # Calculate the depreciated value of the car
    depreciated_value = car_value * (1 - 0.07) ** years_diff
    
    # Format the output string
    output = f"The value of {car_name} on {target_date.strftime('%Y-%m-%d')} is {depreciated_value:.2f}"
    
    return output

# Example usage:
car_info = {
    'name': '2013 Ford Mustang',
    'value': 4478,
    'date': datetime.datetime(2013, 1, 1)
}
print(car_depreciation(car_info))