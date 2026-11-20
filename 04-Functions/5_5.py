###
# Draws each of the figures (square, triangle, rectangle) twice,
# in different locations
#
import turtle
import figures

# Set up the screen
window = turtle.Screen()
window.bgcolor("lightgreen")

# Create the object of the default turtle
pen = turtle.getturtle()
pen.speed(5)

# Draw first square
pen.penup()
pen.goto(-250, 150)
pen.pendown()
figures.draw_square(100)

# Draw second square
pen.penup()
pen.goto(-100, 150)
pen.pendown()
figures.draw_square(50)

# Draw first triangle
pen.penup()
pen.goto(50, 50)
pen.pendown()
figures.draw_trangle(100)

# Draw second triangle
pen.penup()
pen.goto(200, 50)
pen.pendown()
figures.draw_trangle(60)

# Draw first rectangle
pen.penup()
pen.goto(-250, -100)
pen.pendown()
figures.draw_rectangle(120, 60)

# Draw second rectangle
pen.penup()
pen.goto(50, -100)
pen.pendown()
figures.draw_rectangle(150, 80)

# Hide the turtle and finish
pen.hideturtle()
window.mainloop() #keeps the window open