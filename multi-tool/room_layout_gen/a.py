def generate_room_layout(objects, room_dimensions):
    # Initialize the room layout with empty spaces
    room_layout = [[' ' for _ in range(room_dimensions[0])] for _ in range(room_dimensions[1])]
    
    # Place each object in the room
    for object in objects:
        # Calculate the position of the object
        x = object['x']
        y = object['y']
        width = object['width']
        height = object['height']
        
        # Check if the object fits in the room
        if x + width > room_dimensions[0] or y + height > room_dimensions[1]:
            return "Object does not fit in the room"
        
        # Place the object in the room layout
        for i in range(height):
            for j in range(width):
                room_layout[y + i][x + j] = 'X'
    
    # Convert the room layout to ASCII
    ascii_layout = ''
    for row in room_layout:
        ascii_layout += ''.join(row) + '\n'
    
    return ascii_layout

# Define the objects and room dimensions
objects = [
    {'x': 0, 'y': 0, 'width': 16, 'height': 25},  # DAJLIEN utility cart
    {'x': 20, 'y': 0, 'width': 11, 'height': 15}  # TV stand
]
room_dimensions = (100, 100)

# Generate the room layout
layout = generate_room_layout(objects, room_dimensions)

# Print the room layout
print(layout)