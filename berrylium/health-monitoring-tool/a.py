def calculate_health(is_healthy, endpoint, num_errors, total_requests):
    # Calculate the percentage of successful requests
    if total_requests == 0:
        percentage_successful = 0
    else:
        percentage_successful = (total_requests - num_errors) / total_requests * 100

    # Create a dictionary to store the results
    results = {
        "endpoint": endpoint,
        "is_healthy": is_healthy,
        "percentage_successful": percentage_successful
    }

    return results

# Example usage:
is_healthy = True
endpoint = "/api/users"
num_errors = 5
total_requests = 20

result = calculate_health(is_healthy, endpoint, num_errors, total_requests)
print(result)