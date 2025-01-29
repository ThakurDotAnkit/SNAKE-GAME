import time
import turtle

from food import Food
from turtle import Screen

from scoreboard import Scoreboard
from snake import Snake

snake = Snake()
food = Food()
score = Scoreboard()
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Danger Snake")
screen.tracer(0)
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #collegen of food
    if snake.head.distance(food) < 15:
        food.reresh()
        snake.extend()
        score.write_score()
    if snake.head.xcor() > 300 or snake.head.xcor()<-300 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
        is_game_on =False
        score.game_over()
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            is_game_on = False
            score.game_over()
screen.exitonclick()
