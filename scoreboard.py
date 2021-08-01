from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("highest_score.txt", mode="r") as highest_score:
            self.high_score = int(highest_score.read(1))
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}; High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def record(self):
        self.clear()
        if self.score > self.high_score:
            self.high_score = self.score
        with open("highest_score.txt", mode="w") as record:
            record.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()

