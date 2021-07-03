from turtle import *
import random

tim = Turtle()
tim.shape("turtle")
tim.pensize(3)
tim.speed(15)
i = 0

for _ in range(200):
    R = random.random()
    G = random.random()
    B = random.random()

    tim.color(R, G, B)
    tim.circle(100)
    i += 30 % 360
    tim.setheading(i)



screen = Screen()
screen.exitonclick()