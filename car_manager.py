from turtle import Turtle
from random import choice, randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
current_speed = 1


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(1, 2)
        self.color(str(choice(COLORS)))
        self.penup()
        self.goto(300, randint(-300, 300))
        # self.backward(10)
        # self.speed()
        # global n
        # n = STARTING_MOVE_DISTANCE
    def move(self):
        self.backward(STARTING_MOVE_DISTANCE)

    def level_up(self):
        global STARTING_MOVE_DISTANCE
        STARTING_MOVE_DISTANCE += MOVE_INCREMENT

    def distance(self, object):
        self.distance(object)
