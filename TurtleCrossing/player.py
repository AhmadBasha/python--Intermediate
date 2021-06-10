from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 200


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.start_position()

    def up(self):
        # y_position = self.ycor() + MOVE_DISTANCE
        # self.goto(self.xcor(), y_position)
        self.forward(MOVE_DISTANCE)

    def down(self):
        # y_position = self.ycor() - MOVE_DISTANCE
        # self.goto(self.xcor(), y_position)
        self.backward(MOVE_DISTANCE)

    def finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False

    def start_position(self):
        self.goto(STARTING_POSITION)
