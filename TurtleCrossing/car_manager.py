from turtle import Turtle
import random

COLORS = ["red", "green", "blue", "orange", "yellow", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            car = Turtle("square")
            car.penup()
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.color(random.choice(COLORS))
            # to the left side
            car.setheading(180)
            # position
            car.goto(300, random.randint(-250, 250))

            self.cars.append(car)

    def going_forwards(self):
        for car in self.cars:
            car.forward(self.car_speed)

    def car_speed_increment(self):
        self.car_speed += MOVE_INCREMENT
