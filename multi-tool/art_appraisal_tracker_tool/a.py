import statistics
from datetime import datetime

def art_appraisal_tracker(name, appraisals):
    # Convert date strings to datetime objects
    for appraisal in appraisals:
        appraisal['date'] = datetime.strptime(appraisal['date'], '%Y-%m-%d')
    
    # Sort appraisals by date
    appraisals.sort(key=lambda x: x['date'])
    
    # Extract values
    values = [appraisal['value'] for appraisal in appraisals]
    
    # Calculate statistics
    mean = statistics.mean(values)
    median = statistics.median(values)
    std_dev = statistics.stdev(values)
    
    # Print output
    print(f'Name: {name}')
    print('Appraisals:')
    for appraisal in appraisals:
        print(f"Date: {appraisal['date'].strftime('%Y-%m-%d')}, Condition: {appraisal['condition']}, Value: {appraisal['value']}")
    print(f'Mean: {mean}')
    print(f'Median: {median}')
    print(f'Standard Deviation: {std_dev}')

# Example usage:
art_appraisal_tracker('Mona Lisa', [
    {'date': '2020-01-01', 'condition': 'Excellent', 'value': 1000000},
    {'date': '2021-01-01', 'condition': 'Good', 'value': 1100000},
    {'date': '2022-01-01', 'condition': 'Fair', 'value': 1200000},
])

brave_search.call(query="Andy Warhol's Kiku value")