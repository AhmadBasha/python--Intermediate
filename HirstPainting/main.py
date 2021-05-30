# Using this package https://pypi.org/project/colorgram.py/
import colorgram
from turtle import Turtle, Screen, colormode
import random

# Extract 6 colors from an image.
colors = colorgram.extract('image.jpg', 40)
# colorgram.extract returns Color objects, which let you access
# RGB of the image was that color.
hirst_painting_colors = []

for color in colors:
    rgb = color.rgb  # e.g. (255, 151, 210)

    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_rgb = (r, g, b)

    hirst_painting_colors.append(new_rgb)

print(hirst_painting_colors)

# choosing a specific colors from the list to avoid the white
hirst_painting_colors = hirst_painting_colors[20:30]

colormode(255)


def random_color():
    random_tuple_color = random.choice(hirst_painting_colors)

    selected_color = (random_tuple_color[0], random_tuple_color[0], random_tuple_color[0])

    return selected_color


ahmed = Turtle()
ahmed.speed("fastest")
ahmed.penup()
ahmed.hideturtle()

ahmed.setheading(220)
ahmed.forward(500)
ahmed.setheading(0)

for _ in range(9):
    for _ in range(10):
        # drawing
        # ahmed.color(random_color())
        ahmed.dot(40, random_color())

        ahmed.forward(80)
        # moving back
    ahmed.setheading(90)
    ahmed.forward(80)
    ahmed.setheading(180)
    ahmed.forward(800)
    ahmed.setheading(0)

screen = Screen()
screen.exitonclick()
