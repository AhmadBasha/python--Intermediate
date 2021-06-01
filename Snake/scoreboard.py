from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()

        self.score = 0
        self.hideturtle()

        self.goto(0, 280)
        self.color("white")

        self.write(f"Score : {self.score}", align="center", font=("Arial", 18, "bold"))

    def increase_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score : {self.score}", align="center", font=("Arial", 18, "bold"))

    def gameover(self):
        self.goto(0, 0)
        self.write("GAME OVER.", align="center", font=("Arial", 18, "bold"))
