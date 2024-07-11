import random

def drive_time_estimator(start_address, end_address, stops):
    # Estimate the total miles between the two addresses
    total_miles = abs(int(start_address[-5:]) - int(end_address[-5:])) * 4

    # Divide the total distance into three segments
    segment_distance = total_miles / 3

    # For each segment, randomly select a speed in miles per hour from 25-40
    speeds = [random.randint(25, 40) for _ in range(3)]

    # Calculate the time for each segment
    segment_times = [segment_distance / speed for speed in speeds]

    # Add the times from each segment with the times from the stops
    total_time = sum(segment_times) + sum(stops)

    return total_time

# Example usage:
start_address = "123 Main St, Atlanta, GA 30301"
end_address = "456 Elm St, Atlanta, GA 30305"
stops = [10/60]  # 10 minutes

drive_time = drive_time_estimator(start_address, end_address, stops)
print(f"The estimated drive time is {drive_time:.2f} hours.")