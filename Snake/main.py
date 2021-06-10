import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

game_started = True

screen = Screen()
# the size of the screen
screen.setup(width=600, height=600)
# the background color
screen.bgcolor("black")
# title of the screen
screen.title("SNAKE GAME")
# to stop the screen
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

# make the listen to the keys
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# speed = 0.1

while game_started:
    # to update the graphics when all body part moved forward
    screen.update()
    time.sleep(0.07)

    snake.move_snake()
    # when the snake hit the food
    if snake.head.distance(food) < 15:
        food.random_location()
        scoreboard.increase_score()
        snake.snake_bigger()
        # speed -= 0.003

    # when the snake hit the wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        # game_started = False
        # scoreboard.gameover()
        scoreboard.reset()
        snake.reset()

    # collision with the tail
    for snake_body_part in snake.snake[1:]:
        if snake_body_part == snake.head:
            pass
        if snake.head.distance(snake_body_part) < 10:
            # game_started = False
            # scoreboard.gameover()
            scoreboard.reset()
            snake.reset()

screen.exitonclick()
