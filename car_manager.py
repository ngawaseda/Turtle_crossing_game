COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5

from turtle import Turtle
import random

class CarManager(Turtle):

    def __init__(self):
        self.all_cars = []
        self.move_speed = STARTING_MOVE_DISTANCE
        
    def new_car(self):
        random_number = random.randint(0, 6)
        if random_number == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.y_cor = random.randint(-240, 240)
            new_car.goto(300, new_car.y_cor)
            self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            car.backward(self.move_speed)
        
    def new_level(self):
        self.move_speed += MOVE_INCREMENT




