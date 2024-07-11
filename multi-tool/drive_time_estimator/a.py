import random

def drive_time_estimator(address1, address2, stops):
    # Estimate the total miles between the two addresses
    total_miles = abs(int(address1.split()[-1]) - int(address2.split()[-1])) * 4

    # Divide the total distance into three segments
    segment1 = total_miles / 3
    segment2 = total_miles / 3
    segment3 = total_miles / 3

    # Randomly select a speed for each segment
    speed1 = random.randint(25, 40)
    speed2 = random.randint(25, 40)
    speed3 = random.randint(25, 40)

    # Calculate the time for each segment
    time1 = segment1 / speed1
    time2 = segment2 / speed2
    time3 = segment3 / speed3

    # Add the times from each segment with the times from the stops
    total_time = time1 + time2 + time3 + sum(stops)

    return total_time

# Example usage:
address1 = "123 Main St, Atlanta, GA 30301"
address2 = "456 Elm St, Atlanta, GA 30302"
stops = [0.5, 1.0, 0.75]  # 30 minutes, 1 hour, 45 minutes
print(drive_time_estimator(address1, address2, stops))