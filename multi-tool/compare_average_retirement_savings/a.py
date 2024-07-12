def compare_retirement_averages(data, actual_averages):
    # Convert actual averages into dictionary format
    actual_averages_dict = {
        "35 and under": 30170,
        "35-44": 131950,
        "45-54": 254720,
        "55-64": 408420,
        "65-74": 426070,
        "Over 70": 357920
    }

    results = []
    for age_range, average in data.items():
        actual_average = actual_averages_dict[age_range]
        difference = (average - actual_average) / actual_average * 100
        results.append({
            "Age Range": age_range,
            "Data Average": average,
            "Actual Average": actual_average,
            "Difference": difference
        })

    return results

data = {
    "35 and under": 32500,
    "35-44": 140300,
    "45-54": 212000,
    "55-64": 415000,
    "65-74": 189500,
    "Over 70": 365000
}

actual_averages = {
    "35 and under": 30170,
    "35-44": 131950,
    "45-54": 254720,
    "55-64": 408420,
    "65-74": 426070,
    "Over 70": 357920
}

results = compare_retirement_averages(data, actual_averages)
for result in results:
    print(f"Age Range: {result['Age Range']}, Data Average: {result['Data Average']}, Actual Average: {result['Actual Average']}, Difference: {result['Difference']}%")