STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 260
from turtle import Turtle


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def up(self):
        self.forward(MOVE_DISTANCE)

    def right(self):
        new_x = self.xcor() + MOVE_DISTANCE
        y_cor = self.ycor()
        self.goto(new_x, y_cor)

    def left(self):
        new_x = self.xcor() - MOVE_DISTANCE
        y_cor = self.ycor()
        self.goto(new_x, y_cor)

    def reach_finish_line(self):
        if self.ycor() >= FINISH_LINE_Y:
            return True
        else:
            return False

    def restart(self):
        self.goto(STARTING_POSITION)
