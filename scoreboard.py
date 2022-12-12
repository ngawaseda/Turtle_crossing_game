FONT = ("Courier", 24, "normal")

from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("black")
        self.level = 1
        self.hideturtle()
        self.goto(-200, 260)
        self.write(f"Level: {self.level}", align="center", font=("Courier", 20, "normal"))

    def update(self):
        self.clear()
        self.level += 1
        self.write(f"Level: {self.level}", align="center", font=("Courier", 20, "normal"))

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Courier", 40, "normal"))



