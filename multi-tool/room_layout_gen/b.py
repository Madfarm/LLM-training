def generate_room_layout(objects, room_dimensions):
    # Initialize the room layout with empty spaces
    room_layout = [[' ' for _ in range(room_dimensions[0])] for _ in range(room_dimensions[1])]
    
    # Place each object in the room
    for object in objects:
        # Calculate the position of the object in the room
        x = object['position'][0]
        y = object['position'][1]
        
        # Place the object in the room layout
        for i in range(object['dimensions'][0]):
            for j in range(object['dimensions'][1]):
                room_layout[y + i][x + j] = object['symbol']
    
    # Print the room layout
    for row in room_layout:
        print(''.join(row))

# Define the objects and their dimensions
objects = [
    {'name': 'DAJLIEN utility cart', 'dimensions': [16.5, 15.375], 'position': [10, 10], 'symbol': 'C'},
    {'name': 'TV stand', 'dimensions': [11, 15], 'position': [30, 30], 'symbol': 'T'}
]

# Define the room dimensions
room_dimensions = [100, 100]

# Generate the room layout
generate_room_layout(objects, room_dimensions)