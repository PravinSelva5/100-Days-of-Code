from turtle import Turtle, Screen

# Higher Order function is a function that can work with other functions. Python allows other functions to take
# functions as inputs.

'''
W: forward
S: backward
A: CCW
D: CW
C: clear
'''

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(5)

def move_backwards():
    tim.backward(5)

def move_ccw():
    new_direction = tim.heading() + 5
    tim.setheading(new_direction)
def move_cw():
    new_direction = tim.heading() + 5
    tim.setheading(new_direction)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkeypress(key="w", fun=move_forwards)
screen.onkeypress(key="s", fun=move_backwards)
screen.onkeypress(key="a", fun=move_ccw)
screen.onkeypress(key="d", fun=move_cw)
screen.onkeypress(key="c", fun=clear)

screen.exitonclick()