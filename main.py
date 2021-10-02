import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()

cars = CarManager()

scoreboard = Scoreboard()


screen.listen()
screen.onkey(player.go_up, 'Up')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    cars.create_car()
    cars.move_cars()

    # Detect the collision with the cars
    for car in cars.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Detect car successfully reach the other side
        if player.ycor() > 250:
            player.go_to_start()
            cars.speed_increment()
            scoreboard.score()

screen.exitonclick()
