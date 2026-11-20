###
# Draw a square using custom module. Modified code from draw_figures.py
#
import turtle
import figures

# Set up the screen
window = turtle.Screen()
window.bgcolor("lightgreen")

# Set turtle speed
turtle.speed(5)

# Side length
side_length = 100

# Draw a square
figures.draw_square(side_length)

# Hide the turtle and finish
turtle.hideturtle()
window.mainloop() # keep the window open