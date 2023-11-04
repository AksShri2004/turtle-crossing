from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.hideturtle()
        self.setheading(90)
        self.penup()

    def start_pos(self):
        self.goto(STARTING_POSITION)
        self.showturtle()

    def up(self):
        self.forward(MOVE_DISTANCE)

    def dist(self, object):
        return self.distance(object)
