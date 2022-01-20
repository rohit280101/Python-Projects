from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.goto(position)

    def go_up(self):
        y = self.ycor()+30
        self.goto(self.xcor(),y)

    def go_down(self):
        y = self.ycor() -30
        self.goto(self.xcor(), y)


