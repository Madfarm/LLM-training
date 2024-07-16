def AGR_calc(starting_value, ending_value, years):
    AGR = ((ending_value / starting_value)**(1/years)) - 1
    return f"The annualized growth rate for this asset is {AGR*100}%"

starting_value = 3914967
ending_value = 4063566.982400252
years = 3
print(AGR_calc(starting_value, ending_value, years))