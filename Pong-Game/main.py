from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

import time
screen= Screen()
screen.bgcolor("black")
screen.title("PONG GAME")
screen.setup(width=800,height=600)
screen.tracer(0)

r_paddle =Paddle( (380,0) )
l_paddle = Paddle( (-380,0) )
ball = Ball()
score = Scoreboard()
screen.listen()
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")

screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
game_on =True
while game_on:
    screen.update()
    time.sleep(0.1)
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.y_bounce()

    if ball.xcor() >320 and ball.distance(r_paddle) <50 or ball.xcor() < -320  and ball.distance(l_paddle) < 50:

            ball.x_bounce()

    if ball.xcor() >380:
        ball.reset_position()
        score.l_point()
    if ball.xcor() < -380:
        ball.reset_position()
        score.r_point()



screen.exitonclick()