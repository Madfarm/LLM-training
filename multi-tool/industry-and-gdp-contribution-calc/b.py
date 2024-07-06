
def calculate_market_share(venture_value, industry_value):
    market_share = (venture_value / industry_value) * 100
    return market_share

def calculate_gdp_contribution(venture_value, gdp):
    gdp_contribution = (venture_value / gdp) * 100
    return gdp_contribution

# Test the functions
venture_value = 1000000000  # Value of the venture in USD
industry_value = 10000000000  # Value of the industry in USD
gdp = 1000000000000  # GDP of the country in USD

market_share = calculate_market_share(venture_value, industry_value)
gdp_contribution = calculate_gdp_contribution(venture_value, gdp)

print(f"The venture has a market share of {market_share}% in the industry.")
print(f"The venture contributes {gdp_contribution}% to the country's GDP.")