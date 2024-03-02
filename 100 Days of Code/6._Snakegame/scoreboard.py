from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Poppins", 13 ,"bold")
FONT2 = ("Courier", 13 ,"bold")
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.counter = 0
        with open(r".\6._Snakegame\data.txt") as file:
            self.highscore = int(file.read())
        self.hideturtle()
        self.pencolor("white")
        self.pu()
        self.goto(0,260)
        self.updatescore()

    def updatescore(self):
        self.clear()
        self.write(f"SCORE : {self.counter} HIGHSCORE : {self.highscore}", False, align = ALIGNMENT, font = FONT)

    def increasescore(self):
        self.counter += 1
        self.updatescore()
    
    def reset(self):
        if self.counter > self.highscore:
            self.highscore = self.counter
            with open(r".\6._Snakegame\data.txt", mode="w") as file:
                file.write(self.highscore)
        self.counter = 0
        self.updatescore()