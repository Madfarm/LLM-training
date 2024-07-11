def revenue_growth_calc(years, companies):
    for company in companies:
        name, revenue, growth_factor = company
        growth_factor = growth_factor / 100
        for year in range(years):
            revenue += revenue * growth_factor
        print(f"{name}: {revenue:.2f} billion")

# Test the function
companies = [
    ["Intel", 1.6, 1.6],
    ["AMD", 6.7, 2.3],
    ["Nvidia", 60.9, 2.7],
]

revenue_growth_calc(4, companies)