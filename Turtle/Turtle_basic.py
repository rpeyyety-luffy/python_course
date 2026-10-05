import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")

# Create the turtle
pen = turtle.Turtle()
pen.color("cyan")
pen.pensize(3)
pen.speed(3)

# Draw a square
for _ in range(4):
    pen.forward(100)  # Move forward 100 pixels
    pen.left(90)      # Turn left 90 degrees

# Keep the window open until clicked
screen.exitonclick()