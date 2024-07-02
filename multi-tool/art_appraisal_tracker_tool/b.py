import statistics

def art_appraisal_tracker(piece_name, appraisals):
    values = [appraisal['value'] for appraisal in appraisals]
    mean_value = statistics.mean(values)
    median_value = statistics.median(values)
    stdev_value = statistics.stdev(values)

    print(f'Name: {piece_name}')
    print('Appraisals:')
    for appraisal in appraisals:
        print(f'{appraisal["date"]}: Condition: {appraisal["condition"]}, Value: {appraisal["value"]}')
    print(f'Mean Value: {mean_value}')
    print(f'Median Value: {median_value}')
    print(f'Standard Deviation: {stdev_value}')

# Example usage:
mona_lisa_appraisals = [
    {'date': '2020-01-01', 'condition': 'Excellent', 'value': 80000000},
    {'date': '2021-01-01', 'condition': 'Good', 'value': 70000000},
    {'date': '2022-01-01', 'condition': 'Fair', 'value': 60000000},
]

art_appraisal_tracker('Mona Lisa', mona_lisa_appraisals)