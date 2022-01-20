import turtle as t
from turtle import Screen
import random
screen = Screen()
tim = t.Turtle()
tim.penup()
tim.hideturtle()
tim.speed("fastest")
tim.setheading(225)
tim.forward(300)
tim.right(225)
number_of_dots = 100
colors =["green","red","blue","purple","orange","black"]
for dot_count in range(1,number_of_dots +1):
    tim.dot(20,random.choice(colors) )
    tim.forward(50)

    if dot_count %10 ==0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)









screen.exitonclick()