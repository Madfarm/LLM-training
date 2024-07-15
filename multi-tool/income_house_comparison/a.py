
def house_income_comparison(year1, year2):
    if year1 == 1981:
        median_price1 = 54000
        median_income1 = 19010
        avg_mortgage1 = 408
    elif year1 == 2024:
        median_price1 = 420800
        median_income1 = 59384
        avg_mortgage1 = 2200
    else:
        return "Data not available for this year"

    if year2 == 1981:
        median_price2 = 54000
        median_income2 = 19010
        avg_mortgage2 = 408
    elif year2 == 2024:
        median_price2 = 420800
        median_income2 = 59384
        avg_mortgage2 = 2200
    else:
        return "Data not available for this year"

    annual_percent1 = (median_price1 / median_income1) * 100
    monthly_percent1 = (avg_mortgage1 / (median_income1 / 12)) * 100

    annual_percent2 = (median_price2 / median_income2) * 100
    monthly_percent2 = (avg_mortgage2 / (median_income2 / 12)) * 100

    print(f"{year1}                             {year2}")
    print(f"Median income                     {median_income1}                {median_income2}")
    print(f"Median House Price               {median_price1}                {median_price2}")
    print(f"Average Monthly Mortgage      {avg_mortgage1}                {avg_mortgage2}")
    print(f"Percent of Annual Income    {annual_percent1:.2f}%          {annual_percent2:.2f}%")
    print(f"Percent of Monthly Income  {monthly_percent1:.2f}%          {monthly_percent2:.2f}%")

house_income_comparison(1981, 2024)