from turtle import Turtle, Screen, colormode
import random

colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


ahmed = Turtle()
screen = Screen()


def mov_forwards():
    ahmed.forward(10)


def mov_backwards():
    ahmed.backward(10)


def change_color():
    ahmed.color(random_color())


def turn_left():
    ahmed.left(10)
    # ahmed.setheading(ahmed.heading() + 10)


def turn_right():
    ahmed.right(10)
    # ahmed.setheading(ahmed.heading() - 10)


def clear():
    ahmed.clear()
    ahmed.color('black')
    ahmed.penup()
    ahmed.home()
    ahmed.pendown()


screen.listen()
screen.onkey(key="w", fun=mov_forwards)
screen.onkey(key="s", fun=mov_backwards)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=change_color)
screen.onkey(key="e", fun=clear)
screen.exitonclick()
