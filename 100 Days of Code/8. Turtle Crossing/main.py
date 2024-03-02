import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car = CarManager()

screen.listen()
screen.onkey(player.up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.move(scoreboard.current_level)
    car.loopmobil()
    #Kalo nyampe ujung naik level
    if player.checklevel():
        scoreboard.levelup()
        car.createcar()

    #Kalo nyenggol mobil gameover
    for s in car.carlist:
        if s.xcor() < 20 and s.xcor() > -20:
            if s.distance(player) < 20:
                game_is_on = False
                scoreboard.gameover()
        else:
            pass
screen.exitonclick()