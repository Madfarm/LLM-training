import math

def dynamic_range_calc(pmin, pmax):
    return 10 * math.log10(pmax / pmin)

# Example usage:
pmin = 55
pmax = 16433

dynamic_range = dynamic_range_calc(pmin, pmax)
print(f"The dynamic range is {dynamic_range} dB.")