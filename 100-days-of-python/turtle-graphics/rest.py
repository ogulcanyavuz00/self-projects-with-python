import random
from turtle import Turtle, Screen
from utils import get_turtle_color_or_colors, random_color_picker

screen = Screen()
screen.colormode(255)
turtle = Turtle()

screen.screensize(canvwidth=1000, canvheight=1000)


def draw_square(radius):
    turtle.ht()
    turtle.penup()
    turtle.speed(0)
    turtle.setpos(radius / 2, radius / 2)
    turtle.pendown()
    turtle.st()
    turtle.speed(3)
    for _ in range(4):
        turtle.right(90)
        turtle.fd(radius)


def draw_dashed_line(meter):
    for _ in range(15):
        turtle.forward(meter)
        turtle.penup()
        turtle.forward(meter)
        turtle.pendown()


def draw_polygon():
    side_of_polygon = 3
    turtle.pensize(5)
    while side_of_polygon <= 10:
        try:
            turtle.pencolor(get_turtle_color_or_colors("color"))
        except:
            turtle.pencolor(get_turtle_color_or_colors("color"))
        for _ in range(side_of_polygon):
            turtle.forward(100)
            turtle.right(360 / side_of_polygon)
        side_of_polygon += 1





def draw_a_random_walk():
    directions = [0, 90, 180, 270]
    turtle.speed(3)
    turtle.pensize(5)
    for _ in range(1000):
        color = random_color_picker()
        turtle.color(color)
        turtle.forward(random.randrange(0, 40, 5))
        turtle.setheading(random.choice(directions))


def spinograph():
    turtle.speed(3)
    for _ in range(360):
        turtle.color(random_color_picker())
        turtle.circle(120)
        turtle.right(3)
    turtle.hideturtle()



