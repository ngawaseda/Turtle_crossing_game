import time
from turtle import Screen, Turtle
from scoreboard import Scoreboard
from player import Player
from car_manager import CarManager

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

street = Turtle()
street.pensize(width=5)
street.color("grey")
street.penup()
street.goto(300, 245)
street.pendown()
street.goto(-300, 245)
street.penup()
street.goto(-300, -245)
street.pendown()
street.goto(300, -245)


player = Player()
car_manager = CarManager()
score = Scoreboard()

screen.listen()
screen.onkey(player.up, "Up")
screen.onkey(player.right, "Right")
screen.onkey(player.left, "Left")

game_is_on = True



while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.new_car()
    car_manager.move()
    # Detect player's collision with car:
    for car in car_manager.all_cars:
        if player.distance(car) <= 15:
            score.game_over()
            game_is_on = False

    #Detect passing street:
    if player.reach_finish_line():
        score.update()
        player.restart()
        car_manager.new_level()

screen.exitonclick()





