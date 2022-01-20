from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("SNAKE GAME")
screen.tracer(0)


snake = Snake()
food = Food()
score = Scoreboard()
screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.2)
    snake.move()

    if snake.head.distance(food) < 15:
        food.change_food()
        snake.extend()
        score.increase_score()

    if snake.head.xcor() >280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() <-280:
        score.reset_game()
        snake.reset_snake()

## We can also use slice properties instead of this
    for i in snake.segments:
        if snake.head == i:
            pass
        elif snake.head.distance(i) < 10:
            is_game_on =False
            score.reset_game()
            snake.reset_snake()
    # for i in snake.segments[1:]:
    #     if snake.head.distance(i) < 10:
    #         is_game_on =False
    #         score.gameover()
##



screen.exitonclick()








