from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()

        self.score = 0

        with open("data.txt") as file:
            self.high_score = int(file.read())

        self.hideturtle()

        self.goto(0, 280)
        self.color("white")

        # self.write(f"Score : {self.score}", align="center", font=("Arial", 18, "bold"))
        self.update_scoreboard()

    def increase_score(self):
        # self.clear()
        self.score += 1
        # self.write(f"Score : {self.score}", align="center", font=("Arial", 18, "bold"))
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score : {self.score} High Score: {self.high_score}", align="center", font=("Arial", 18, "bold"))

    # def gameover(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER.", align="center", font=("Arial", 18, "bold"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.store_high_score()
        self.score = 0
        self.update_scoreboard()

    def store_high_score(self):
        with open("data.txt", mode="w") as file:
            file.write(str(self.high_score))
