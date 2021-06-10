from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import ScoreBoard
import time

# to check the game
game_over = False

# for the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

turtle = Player()

car = CarManager()

scoreboard = ScoreBoard()

# when u click up arrow the turtle will move forwards
screen.listen()
screen.onkey(turtle.up, "Up")
screen.onkey(turtle.down, "Down")

# while the game is not over
while not game_over:
    time.sleep(0.1)
    screen.update()
    # for the car
    car.create_car()
    car.going_forwards()
    # if the car crash
    for single_car in car.cars:
        if single_car.distance(turtle) < 20:
            game_over = True
            scoreboard.game_over()

    # if the player done from the round
    if turtle.finish_line():
        turtle.start_position()
        # speed the cars up
        car.car_speed_increment()
        scoreboard.level_up()

# the screen will exit when i click
screen.exitonclick()
