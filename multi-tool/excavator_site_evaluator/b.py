def excavation_site_evaluator(designation, distance, pH, safety, temperature, bioturbation):
    # Calculate the weighted sum of the factors
    weighted_sum = (distance * 0.1) + (abs(pH - 8) * 0.2) + (safety * 0.4) + (temperature * 0.1) + (bioturbation * 0.2)
    
    # Calculate the overall rating
    overall_rating = 10 - (weighted_sum / 10)
    
    return overall_rating

# Test the function
designation = "Taiga Site 32a"
distance = 96
pH = 7.5
safety = 4
temperature = 41
bioturbation = 1

overall_rating = excavation_site_evaluator(designation, distance, pH, safety, temperature, bioturbation)
print(f"The overall rating of the {designation} is {overall_rating:.2f}")
