###
# Module for drawing diffrent gemetric function using the module turtle
#
import turtle

def draw_square(length):
    for i in range(4):
        turtle.forward(length)
        turtle.right(90)


def draw_trangle(length):
    turtle.forward(length)
    turtle.left(90)
    turtle.forward(length)
    turtle.left(135)
    # calculating the length of hypothenus using pitagora's therum equasion
    turtle.forward(length * 2 ** 0.5)
    turtle.left(135)


def draw_rectangle(lenght_a, lenght_b):
    for i in range(2):
        turtle.forward(lenght_a)
        turtle.right(90)
        turtle.forward(lenght_b)
        turtle.right(90)

