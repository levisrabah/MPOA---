import turtle
import math
import time

# Set up the screen
screen = turtle.Screen()
screen.setup(width=800, height=700)
screen.bgcolor("black")
screen.title("Heart Animation")

# Create the turtle for drawing the heart
heart_turtle = turtle.Turtle()
heart_turtle.speed(0)  # Fastest speed
heart_turtle.width(2)
heart_turtle.hideturtle()

# Create a separate turtle for text
text_turtle = turtle.Turtle()
text_turtle.hideturtle()
text_turtle.penup()
text_turtle.color("white")

# Define the gradient color function
def gradient_color(t, iteration):
    """Create a smooth glowing color gradient."""
    r = int(abs(math.sin(iteration * 0.1)) * 255)
    g = int(abs(math.sin(iteration * 0.2)) * 128)
    b = int(abs(math.cos(iteration * 0.3)) * 255)
    t.color((r, g, b)) 

# Heart shape formula
def heart_curve(n):
    """Mathematical formula to create a heart-shaped curve."""
    x = 16 * math.sin(n)**3
    y = 13 * math.cos(n) - 5 * math.cos(2*n) - 2 * math.cos(3*n) - math.cos(4*n)
    return x, y

# Draw the animated heart
def draw_heart():
    """Draw multiple glowing hearts."""
    heart_turtle.penup()
    heart_turtle.goto(0, -50)  # Position the heart slightly lower
    heart_turtle.setheading(0)

    for i in range(15):  # Create a glowing effect
        heart_turtle.penup()
        heart_turtle.goto(0, -50)
        heart_turtle.pendown()
        gradient_color(heart_turtle, i)

        for n in range(0, 628, 2):
            x, y = heart_curve(n / 100)
            heart_turtle.goto(x * i * 0.5, y * i * 0.5)

# Add romantic text with animation
def write_message():
    # Write "I" at the top
    text_turtle.goto(0, 250)
    text_turtle.write("I", align="center", font=("Courier New", 60, "bold"))

    # Wait for a moment
    time.sleep(1)

    # Draw the heart in the middle
    heart_turtle.penup()
    heart_turtle.goto(0, 50) 
    heart_turtle.pendown()
    draw_heart()

    # Write text below the heart
    text_turtle.goto(0, -250)
    text_turtle.color("white")
    text_turtle.write("XYZ...", align="center", font=("Courier New", 70))

# Main function
def main():
    turtle.colormode(255)  # Enable RGB color mode
    write_message()
    screen.mainloop()

# Run the animation
main()
