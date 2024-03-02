from turtle import Turtle
FONT = ("Courier", 18, "bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-280,260)
        self.current_level = 1
        self.leveltext()
        

    def leveltext(self):
        self.clear()
        self.write(f"Level: {self.current_level}", align= "left" , font = FONT)


    def levelup(self):
        self.current_level += 1
        self.leveltext()

    def gameover(self):
        self.goto(0,0)
        self.write("Game Over.", align="center", font=("courier",15,"bold"))