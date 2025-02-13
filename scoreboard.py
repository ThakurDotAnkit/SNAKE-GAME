from turtle import Turtle
ALIHNMENT = "center"
FONT = ("Arial", 24, "normal")



class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("high_score.txt", mode="r") as high_score:
            self.high_score = int(high_score.read())
        self.color("white")
        self.penup()
        self.goto(0, 250)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score = {self.score} High_Score = {self.high_score}", False, align=ALIHNMENT, font=FONT)

    def reset(self):
        if self.score > int(self.high_score):
            self.high_score = self.score
            with open("high_score.txt", mode="w") as high_score:
                high_score.write(f"{self.score}")
        self.score = 0
        self.update_scoreboard()

    def write_score(self):
        self.score += 1
        self.update_scoreboard()
