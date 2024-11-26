import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("lightblue")  # Set background color

# Create a turtle object
my_turtle = turtle.Turtle()
my_turtle.pensize(3)  # Set the thickness of the pen
my_turtle.speed(5)  # Set the drawing speed

# Function to draw a square
def draw_square(size):
    for _ in range(4):  # Loop 4 times for 4 sides
        my_turtle.forward(size)  # Move forward
        my_turtle.right(90)  # Turn 90 degrees to the right

# Draw the square
draw_square(100)  # Draw a square of size 100

# Finish
turtle.done()
