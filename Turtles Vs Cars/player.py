from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
     def __init__(self):
         super().__init__()
         self.shape("turtle")
         self.color("green")
         self.penup()
         self.shapesize(1,1)
         self.left(90)
         self.goto(STARTING_POSITION)

     def move_up(self):
         y = self.ycor() + MOVE_DISTANCE
         self.goto(self.xcor(), y)

     def restart(self):
         self.goto(STARTING_POSITION)



