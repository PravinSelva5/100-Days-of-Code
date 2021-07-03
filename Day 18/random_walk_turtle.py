from turtle import *
import random

tim = Turtle()
tim.shape("turtle")
tim.pensize(10)

direction = [0,90,180,270]

for _ in range(200):
    R = random.random()
    G = random.random()
    B = random.random()

    tim.color(R, G, B)
    tim.forward(30)
    tim.setheading(random.choice(direction))

screen = Screen()
screen.exitonclick()