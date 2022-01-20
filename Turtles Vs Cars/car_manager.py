from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 65


class CarManager():
    def __init__(self):
        self.all_cars=[]
        self.car_speed = STARTING_MOVE_DISTANCE






    def generate_cars(self):
        x = random.randint(1,6)
        if x == 6:
            z = random.randint(-220, 250)
            new_car = Turtle()
            new_car.shape("square")
            new_car.penup()
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.setheading(180)
            new_car.color(random.choice(COLORS))
            self.all_cars.append(new_car)
            new_car.goto(275, z)



    def move_car(self):
        for cars in self.all_cars:
            cars.forward(STARTING_MOVE_DISTANCE)


    def level_up(self):
        self.car_speed += MOVE_INCREMENT
