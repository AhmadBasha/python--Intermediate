from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.snake_body_position = 0
        self.snake = []

        self.create_snake()
        self.head = self.snake[0]


    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_body_part(position)

    def move_snake(self):

        # for body_part in snake:
        #     body_part.forward(10)
        # range (start = 2 , stop = 0 , step = -1):
        for body_part in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[body_part - 1].xcor()
            new_y = self.snake[body_part - 1].ycor()
            self.snake[body_part].goto(new_x, new_y)
        self.head.forward(20)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def add_body_part(self, position):
        snake_body = Turtle(shape="square")
        # it will not print on the screen
        snake_body.penup()
        # the body color
        snake_body.color("white")
        # the position on the grid
        snake_body.goto(position)
        # here to put all the body part together
        self.snake.append(snake_body)

    def snake_bigger(self):
        self.add_body_part(self.snake[-1].position())

