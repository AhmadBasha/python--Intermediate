from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

game_on = True
screen = Screen()
screen.bgcolor("black")
screen.title("PONG GAME")
screen.setup(width=800, height=600)
# to stop the screen
screen.tracer(0)

paddle_one = Paddle(360)
paddle_two = Paddle(-360)

ball = Ball()
scoreboard = ScoreBoard()


# make the listen to the keys
screen.listen()
screen.update()
screen.onkey(paddle_one.up, "Up")
screen.onkey(paddle_one.down, "Down")
screen.onkeypress(paddle_two.up, "w")
screen.onkey(paddle_two.down, "s")

while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # check if the ball will hit the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect if the ball will hit the paddle
    if ball.distance(paddle_one) < 50 and ball.xcor() > 330:
        ball.bounce_x()
    elif ball.distance(paddle_two) < 50 and ball.xcor() < -330:
        ball.bounce_x()

    # if first paddle could not catch the ball
    if ball.xcor() > 390:
        ball.reset_position()
        scoreboard.increase_l_score()

    # if second paddle could not catch the ball
    if ball.xcor() < -390:
        ball.reset_position()
        scoreboard.increase_r_score()

screen.exitonclick()
