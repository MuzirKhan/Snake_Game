from turtle import Screen
import time

from food import Food
from scoreboard import ScoreBoard
from snake import Snake

screen = Screen()
screen.bgcolor('black')
screen.title("Snake Game")
screen.tracer(0)
game_is_on = True

screen.setup(width=600, height=600)
snake = Snake()
food = Food()
scoreboard = ScoreBoard()
screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")

while game_is_on:
    time.sleep(0.1)
    screen.update()
    snake.move()

    if snake.head.distance(food) < 15:
        scoreboard.increase_score()
        food.refresh()
        snake.extend()
        scoreboard.clear()
        scoreboard.show_score()
    if snake.head.xcor() > 290 or snake.head.ycor() > 290 or snake.head.xcor() < -280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset_snake()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            print(scoreboard.highscore)
            scoreboard.reset()
            snake.reset_snake()

screen.exitonclick()
