from turtle import Turtle, Screen
import random

'''
TURTLE RACE GAME
'''

is_game_on = False

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? "
                                                          "Enter a colour: "
                                                          "['red', 'orange', 'yellow', 'green', 'blue', 'purple']")
colour = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []

x = -225
y = -100

for turtle_colour in colour:
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(turtle_colour)
    new_turtle.goto(x, y)
    y += 40
    all_turtles.append(new_turtle)

if user_bet:
    is_game_on = True


while is_game_on:

    for turtle_id in range(6):
        rand_distance = random.randint(0, 10)
        all_turtles[turtle_id].forward(rand_distance)

        if round(all_turtles[turtle_id].xcor()) == 175:
            is_game_on = False

if user_bet == all_turtles[turtle_id].color():
    print("You won your bet!")
else:
    print("You lost your bet!")


screen.exitonclick()