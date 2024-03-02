from turtle import Screen
from paddle import Paddle, Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.title("~Pong Game~")
screen.bgcolor("black")
screen.tracer(0)


rpaddle = Paddle(350)
lpaddle = Paddle(-350)

ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(rpaddle.up,"Up")
screen.onkey(rpaddle.down,"Down")
screen.onkey(lpaddle.up,"w")
screen.onkey(lpaddle.down,"s")

game_is_on = True
while game_is_on:
    time.sleep(ball.movespeed)
    screen.update()
    ball.move()

    #Detect top and bottom wall
    if ball.ycor() > 287 or ball.ycor() < -287:
        ball.bounce_y()

    #Detect collision with paddle
    #tidak bisa menggunakan distance because (distance menghitung dari pusat ke pusat)
    #sebagai gantinya kita bisa menggunakan dua syarat yaitu jika ball melewati x tertentu dan distancenya < 50
    if ball.distance(rpaddle) < 50 and ball.xcor() > 320 or ball.distance(lpaddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()  


    #Detect right and left wall
    if ball.xcor() > 380:
        ball.home()
        ball.bounce_x()
        ball.movespeed = 0.1
        scoreboard.lpoint()

    if ball.xcor() < -380:
        ball.home()
        ball.bounce_x()
        ball.movespeed = 0.1
        scoreboard.rpoint()
        
    

screen.exitonclick()