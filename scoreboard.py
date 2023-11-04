import turtle as t
FONT = ("Courier", 24, "normal")


class Scoreboard(t.Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-250,250)
        self.level = 1

    def write_score(self):
        self.clear()
        self.write(f"Level:{self.level}", False, "left", FONT)

    def level_up(self):
        self.level += 1
        self.write_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, "center", FONT)