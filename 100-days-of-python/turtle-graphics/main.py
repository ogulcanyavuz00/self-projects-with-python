from turtle import Turtle, Screen
from utils import random_color_picker

screen = Screen()
screen.colormode(255)
turtle = Turtle()

screen.screensize(canvwidth=1000, canvheight=1000)


def hirst_painting():
    turtle.penup()
    print(turtle.position())
    while True:
        turtle.pencolor(random_color_picker())
        turtle.forward(30)
        turtle.dot(20)


hirst_painting()

screen.exitonclick()
