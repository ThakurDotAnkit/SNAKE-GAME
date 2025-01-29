import random
from turtle import Turtle


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("yellow")
        self.speed("fastest")

    def reresh(self):
        self.random_x = random.randint(-288, 288)
        self.random_y = random.randint(-288, 288)
        self.goto(self.random_x, self.random_y)