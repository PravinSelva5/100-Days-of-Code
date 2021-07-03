from turtle import *
import random

tim = Turtle()

def draw_shape(num_sides):
    R = random.random()
    G = random.random()
    B = random.random()
    angle = 360/num_sides

    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)
        tim.color(R, G, B)


for shape_side in range(3, 11):
    draw_shape(shape_side)

screen = Screen()
screen.exitonclick()