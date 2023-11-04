import random
import time
from turtle import Screen

from car_manager import CarManager
from player import Player
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

cars = []
list = [1, 2, 3, 4]

player = Player()

player.start_pos()
game_is_on = True

scoreboard = Scoreboard()

while game_is_on:
    time.sleep(0.1)

    screen.listen()
    screen.onkeypress(player.up, "Up")

    # adds new cars
    if random.choice(list) == 3:
        new_car = CarManager()
        cars.append(new_car)
    else:
        pass

    if player.ycor() < 280:
        scoreboard.write_score()
        for p in cars:
            p.move()
            dist = player.dist(p)
            if dist < 20:
                game_is_on = False
                scoreboard.game_over()

    else:
        scoreboard.level_up()
        new_car.level_up()
        for n in cars:
            n.move()
        player.start_pos()

    screen.update()
screen.exitonclick()