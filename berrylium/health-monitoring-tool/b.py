def calculate_health(endpoint, is_responding, num_errors, total_requests):
        health = {}
        health['endpoint'] = endpoint   
 
        if is_responding:
            health['status'] = "healthy"
            success_percentage = (total_requests - num_errors) / total_requests * 100
            health['success_percentage'] = f"{success_percentage:.2f}%"
        else:
            health['status'] = "unhealthy"
            health['success_percentage'] = "0.00%"
 
        return health


#Testing the function         
print(calculate_health('www.example.com', True, 5, 20))