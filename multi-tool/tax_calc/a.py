import re

def tax_calculator(kind_of_tax, total_income, deductions):
    tax_brackets = {
        "1099": {
            0.10: 11600,
            0.12: 47150,
            0.22: 100525,
            0.24: 191950,
            0.32: 243725,
            0.35: 609350,
            0.37: 1000000000,
        },
        "W2": {
            0.10: 6000,
            0.12: 34600,
            0.22: 89350,
            0.24: 191950,
            0.32: 243725,
            0.35: 609350,
            0.37: 1000000000,
        }
    }

    income_tax = 0
    remaining_income = total_income
    for tax_rate in tax_brackets[kind_of_tax].keys():
        if remaining_income > tax_brackets[kind_of_tax][tax_rate]:
            income_tax += (tax_brackets[kind_of_tax][tax_rate] * tax_rate)
            remaining_income -= tax_brackets[kind_of_tax][tax_rate]
        else:
            income_tax += (remaining_income * tax_rate)
            break

    for deduction in deductions:
        if isinstance(deduction[1], str):
            percent = re.findall(r"(\d+\.\d+)%", deduction[1])
            if percent:
                income_tax *= (1 - float(percent[0]) / 100)
        else:
            income_tax -= deduction[1]

    return income_tax

kind_of_tax = "1099"
total_income = 48545
deductions = [("self-employment deduction", "7.3%"), ("charitable donations", 500), ("random deduction", 3000)]

income_tax = tax_calculator(kind_of_tax, total_income, deductions)
print(f"Total Owed: {income_tax}")