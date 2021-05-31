from turtle import Turtle, Screen
import random

# game start
game_over = False
# colors of the turtles
colors = ["yellow1", "SpringGreen", "SlateBlue3", "turquoise1", "red"]
# all turtle
turtles = []
# turtles positions
turtle_positions = [0, -30, -60, 30, 60]

screen = Screen()

# set up the size of the screen
screen.setup(width=500, height=400)

# the pop up window
user_input = screen.textinput(title="Guess The Turtle", prompt="Which turtle will win the race ? "
                                                               "Enter the turtle color : ")

for index in range(0, 5):
    turtle = Turtle(shape="turtle")
    # it will not print on the screen
    turtle.penup()
    # the color
    turtle.color(colors[index])
    # the position on the grid
    turtle.goto(x=-230, y=turtle_positions[index])
    # insert it to the turtles list
    turtles.append(turtle)

if user_input:
    game_over = True

while game_over:
    for single_turtle in turtles:

        # to go forward
        single_turtle.forward(random.random() * 3)

        if single_turtle.xcor() > 230:
            # to end the game
            game_over = False
            # store the turtle color
            winner = single_turtle.pencolor()
            # here the user guess the winning color
            if winner == user_input:
                print(f"You guessed {winner} which is correct, Bravo!!! 🤩 ")
            else:
                print(f"You guessed {user_input} which is incorrect, try again later looser !!! 😂")
                print(f"The winner is {winner}")

screen.exitonclick()
