from turtle import Turtle

FONT = ("Monserrat", 50, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.pu()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scorebard()

    def update_scorebard(self):
        self.clear()
        self.goto(-100, 210)
        self.write(self.l_score,align = "center", font = FONT)
        
        self.goto(100, 210)
        self.write(self.r_score,align = "center", font = FONT)

    def lpoint(self):
        self.l_score += 1
        self.update_scorebard()

    def rpoint(self):
        self.r_score += 1
        self.update_scorebard()