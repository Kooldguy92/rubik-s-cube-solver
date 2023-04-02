from PIL import Image
from rubiks import RubiksCube

# Define the solve function
def solve(cube):
    # Your solving algorithm here
    # ...
    return "Solution"

# Define a function to generate an image of the Rubik's cube
def generate_image(cube, filename):
    # Create a blank image
    image = Image.new("RGB", (300, 300), (255, 255, 255))

    # Loop over each face of the cube
    for face, color in cube.colors.items():
        # Calculate the position of the face on the image
        x = 0
        y = 0
        if face == "U":
            x = 100
            y = 0
        elif face == "L":
            x = 0
            y = 100
        elif face == "F":
            x = 100
            y = 100
        elif face == "R":
            x = 200
            y = 100
        elif face == "B":
            x = 100
            y = 200
        elif face == "D":
            x = 100
            y = 400

        # Loop over each sticker on the face
        for row in range(3):
            for col in range(3):
                # Get the color of the sticker
                sticker_color = color[row][col]

                # Calculate the position of the sticker on the image
                sticker_x = x + col * 30
                sticker_y = y + row * 30

                # Draw the sticker on the image
                draw = ImageDraw.Draw(image)
                draw.rectangle((sticker_x, sticker_y, sticker_x + 30, sticker_y + 30), fill=sticker_color)

    # Save the image to a file with the given filename
    image.save(filename)

# Prompt the user to enter the colors of each face
front = input("Enter the colors for the front face, from left to right and top to bottom: ").split()
right = input("Enter the colors for the right face, from left to right and top to bottom: ").split()
back = input("Enter the colors for the back face, from left to right and top to bottom: ").split()
left = input("Enter the colors for the left face, from left to right and top to bottom: ").split()
up = input("Enter the colors for the up face, from left to right and top to bottom: ").split()
down = input("Enter the colors for the down face, from left to right and top to bottom: ").split()

# Construct the input cube from the user input
cube = RubiksCube(front, right, back, left, up, down)

# Call the generate_image function to save an image of the initial cube
generate_image(cube, "output0.png")

# Call the solve function and apply each move to the cube, generating an image of the cube after each move
solution = solve(cube)
moves = solution.split()
for i, move in enumerate(moves):
    cube.rotate(move)
    generate_image(cube, "output{}.png".format(i+1))

# Print the solution
print(solution)

#note you can't solve the wrong algorithm and you will receive a output.png of every move on rubik's cube
