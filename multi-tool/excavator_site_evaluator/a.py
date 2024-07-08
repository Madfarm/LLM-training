import math

def excavation_site_evaluator(designation, distance, pH, safety_rating, soil_surface_temperature, bioturbation_rating):
    # Define the weights for each factor
    distance_weight = 0.2
    pH_weight = 0.1
    safety_rating_weight = 0.4
    soil_surface_temperature_weight = 0.1
    bioturbation_rating_weight = 0.2

    # Calculate the rating for each factor
    distance_rating = 10 - (distance / 100)
    pH_rating = 10 - abs(8 - pH)
    safety_rating = safety_rating
    soil_surface_temperature_rating = 10 - (soil_surface_temperature / 100)
    bioturbation_rating = 10 - bioturbation_rating

    # Calculate the overall rating
    overall_rating = (distance_rating * distance_weight + pH_rating * pH_weight + safety_rating * safety_rating_weight + soil_surface_temperature_rating * soil_surface_temperature_weight + bioturbation_rating * bioturbation_rating_weight) / (distance_weight + pH_weight + safety_rating_weight + soil_surface_temperature_weight + bioturbation_rating_weight)

    return overall_rating

# Test the function
print(excavation_site_evaluator("Taiga Site 32a", 96, 7.5, 4, 41, 1))