from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.font = ("Courier", 50, "bold")
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-250, 200)
        self.write(arg=self.l_score, align="center", font=self.font)
        self.goto(250, 200)
        self.write(arg=self.r_score, align="center", font=self.font)

    def lpoint(self):
        self.l_score += 1
        self.update_scoreboard()

    def rpoint(self):
        self.r_score += 1
        self.update_scoreboard()


