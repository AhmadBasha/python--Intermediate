from turtle import Turtle

FONT = ("Courier", 24, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1

        self.penup()
        self.hideturtle()
        self.goto(-290, 270)

        self.turtle_scoreboard()

    def turtle_scoreboard(self):
        self.clear()
        self.write(f"LEVEL: {self.level}", font=FONT, align="left")

    def level_up(self):
        self.level += 1
        self.turtle_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", font=FONT, align="center")
