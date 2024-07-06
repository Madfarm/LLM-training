class KPopIndustry:
    def __init__(self, name, value, country, country_GDP, industry, industry_value):
        self.name = name
        self.value = value
        self.country = country
        self.country_GDP = country_GDP
        self.industry = industry
        self.industry_value = industry_value

    def calculate_market_share(self):
        market_share = (self.value / self.industry_value) * 100
        return market_share

    def calculate_GDP_contribution(self):
        GDP_contribution = (self.value / self.country_GDP) * 100
        return GDP_contribution

    def print_results(self):
        market_share = self.calculate_market_share()
        GDP_contribution = self.calculate_GDP_contribution()
        print(f"{self.name} contributes to {GDP_contribution}% of {self.country}'s GDP.")
        print(f"{self.name} has a market share of {market_share}% of the {self.industry} industry.")

# Usage
BTS = KPopIndustry("BTS", 3.6e9, "South Korea", 1.72e12, "K-pop", 8.9e9)
BTS.print_results()