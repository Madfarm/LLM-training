def dynamic_range_calc(pmin, pmax):
    return 10 * math.log10(pmax / pmin)

# Test the function
pmin = 55
pmax = 16433
print("The dynamic range is: ", dynamic_range_calc(pmin, pmax), "dB")