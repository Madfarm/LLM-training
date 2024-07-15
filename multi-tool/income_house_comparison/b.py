def house_income_comparison(year1, year2):
    # Define the median house prices and median incomes for each year
    median_house_prices = {
        1981: 83400,
        2024: 420800
    }
    median_incomes = {
        1981: 19010,
        2024: 59384
    }

    # Calculate the average monthly mortgage for each year
    average_monthly_mortgages = {
        1981: 376,
        2024: 2200
    }

    # Calculate the percent of annual income needed to buy the median house for each year
    percent_annual_income = {
        1981: (median_house_prices[1981] / median_incomes[1981]) * 100,
        2024: (median_house_prices[2024] / median_incomes[2024]) * 100
    }

    # Calculate the percent of monthly income the monthly mortgage makes up for each year
    percent_monthly_income = {
        1981: (average_monthly_mortgages[1981] / (median_incomes[1981] / 12)) * 100,
        2024: (average_monthly_mortgages[2024] / (median_incomes[2024] / 12)) * 100
    }

    # Print the results
    print(f"{year1}                                  {year2}")
    print(f"Median income                     {median_incomes[year1]}                {median_incomes[year2]}")
    print(f"Median House Price               {median_house_prices[year1]}         {median_house_prices[year2]}")
    print(f"Average Monthly Mortgage      {average_monthly_mortgages[year1]}            {average_monthly_mortgages[year2]}")
    print(f"Percent of Annual Income    {percent_annual_income[year1]:.2f}%    {percent_annual_income[year2]:.2f}%")
    print(f"Percent of Monthly Income  {percent_monthly_income[year1]:.2f}%  {percent_monthly_income[year2]:.2f}%")

house_income_comparison(1981, 2024)