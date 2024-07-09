def tax_calculator(income, deductions):
    # Define tax brackets for 2024
    tax_brackets = {
        '10%': (0, 11600),
        '12%': (11601, 47150),
        '22%': (47151, 100525),
        '24%': (100526, 191950),
        '32%': (191951, 243725),
        '35%': (243726, 609350),
        '37%': (609351, float('inf')),
    }

    # Calculate total income
    total_income = income

    # Calculate tax owed
    tax_owed = 0
    for bracket, (lower_bound, upper_bound) in tax_brackets.items():
        if total_income > upper_bound:
            tax_owed += (upper_bound - lower_bound) * (int(bracket[:-1]) / 100)
        else:
            tax_owed += (total_income - lower_bound) * (int(bracket[:-1]) / 100)
            break

    # Apply deductions
    for deduction in deductions:
        if deduction[1][-1] == '%':
            tax_owed *= (1 - (int(deduction[1][:-1]) / 100))
        else:
            tax_owed -= deduction[1]

    return tax_owed

# Test the function
print(tax_calculator(48545, [("self-employment deduction", "7.3%"), ("charitable donations", 500), ("random deduction", 3000)]))