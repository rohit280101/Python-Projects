from turtle import Turtle, Screen
screen =Screen()
import random


colours =["red","green","yellow","blue","purple","orange"]
ye =[-70,-40,-10,20,50,80]
screen.setup(500,400)
user_bet=screen.textinput("make your bet","which  color will win the race?")
all_turtles=[]
is_race_on = False
for i in range(6):
    new_turtle = Turtle("turtle")
    new_turtle.penup()
    new_turtle.color(colours[i])
    new_turtle.goto(x =-230, y=ye[i])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on =True
while is_race_on:
    for race in all_turtles:
        if race.xcor()>230:
            is_race_on=False
            winning_color = race.pencolor()
            if winning_color == user_bet:
                print("you won")
                break
            else:
                print(f"you lost , {winning_color} turtle has won")
                break
        x = random.randint(0,10)
        race.forward(x)





screen.exitonclick()