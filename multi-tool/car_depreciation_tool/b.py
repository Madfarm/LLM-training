import datetime

def car_depreciation(car_info, target_date=None):
    if target_date is None:
        target_date = datetime.date.today()
    else:
        target_date = datetime.datetime.strptime(target_date, "%Y-%m-%d").date()
    
    car_name = car_info['name']
    car_value = car_info['value']
    car_date = datetime.datetime.strptime(car_info['date'], "%Y-%m-%d").date()
    
    years = (target_date - car_date).days / 365.25
    depreciation = car_value * (1 - (1 - 0.07) ** years)
    
    return f"The value of {car_name} on {target_date} is {depreciation}"

# Example usage:
car_info = {
    'name': '2013 Ford Mustang',
    'value': 4478,
    'date': '2013-01-01'
}

print(car_depreciation(car_info))