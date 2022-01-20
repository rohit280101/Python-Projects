import time
from turtle import Screen

from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
player = Player()
cars = CarManager()
score = Scoreboard()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
screen.onkey(player.move_up,"w")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.generate_cars()
    cars.move_car()
    for i in cars.all_cars:
        if i.distance(player) < 20:
            game_is_on = False
            score.game_over()

    if player.ycor() > 280:

        player.restart()
        cars.level_up()
        score.increase_level()
screen.exitonclick()