from turtle import Turtle
import turtle
ALIHNMENT = "center"
FONT = ("Arial", 24, "normal")
class Scoreboard (Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 240)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"SCORE = {self.score}", False, align=ALIHNMENT, font=FONT)

    def game_over(self):

        self.goto(0, 0)
        self.write("GAME OVER", False, align=ALIHNMENT, font=FONT)


    def write_score(self):
        self.score+=1
        self.clear()
        self.update_scoreboard()
