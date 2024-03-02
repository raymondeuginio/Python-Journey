from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.pu()
        self.color("white")
        self.goto(position,0)
        self.shapesize(stretch_wid=5,stretch_len=1)
    
    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(),new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(),new_y)

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("sky blue")
        self.pu()
        self.xmove = 10
        self.ymove = 10
        self.movespeed = 0.1

    def move(self):
        new_x = self.xcor() + self.xmove
        new_y = self.ycor() + self.ymove
        self.goto(new_x,new_y)

    def bounce_y(self):
        self.ymove *= -1

    def bounce_x(self):
        self.xmove *= -1
        self.movespeed *= 0.9
    
      
    
