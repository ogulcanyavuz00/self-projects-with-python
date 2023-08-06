# from turtle import Turtle, Screen
# from get_turtle_colors import process_text
# import random
# screen = Screen()
# tim = Turtle()

# tim.shape("turtle")
# tim.fillcolor("red")
#
#
# def draw_square(radius):
#     tim.ht()
#     tim.penup()
#     tim.speed(0)
#     tim.setpos(radius / 2, radius / 2)
#     tim.pendown()
#     tim.st()
#     tim.speed(3)
#     for _ in range(4):
#         tim.right(90)
#         tim.fd(radius)
#
#
# def draw_dashed_line(meter):
#     for _ in range(15):
#         tim.forward(meter)
#         tim.penup()
#         tim.forward(meter)
#         tim.pendown()
#
#
# def draw_polygon():
#     side_of_polygon = 3
#     while side_of_polygon <= 10:
#         for _ in range(side_of_polygon):
#             tim.forward(100)
#             tim.right(360 / side_of_polygon)
#         side_of_polygon += 1
#
# draw_polygon()