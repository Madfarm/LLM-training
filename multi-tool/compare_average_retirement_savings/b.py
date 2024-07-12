def compare_retirement_averages(data_set, actual_averages):
    results = []
    for age_range, data_average in data_set.items():
        actual_average = actual_averages[age_range]
        difference = (data_average - actual_average) / actual_average * 100
        results.append({
            'age_range': age_range,
            'data_average': data_average,
            'actual_average': actual_average,
            'difference': difference
        })
    return results

data_set = {
    '35 and under': 32500,
    '35-44': 140300,
    '45-54': 212000,
    '55-64': 415000,
    '65-74': 189500,
    'Over 70': 365000
}

actual_averages = {
    '35 and under': 30170,
    '35-44': 131950,
    '45-54': 254720,
    '55-64': 408420,
    '65-74': 426070,
    'Over 70': 357920
}

results = compare_retirement_averages(data_set, actual_averages)

for result in results:
    print(f"Age Range: {result['age_range']}, Data Average: {result['data_average']}, Actual Average: {result['actual_average']}, Difference: {result['difference']}%")