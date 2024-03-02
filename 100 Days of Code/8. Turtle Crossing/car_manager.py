from turtle import Turtle
import random
COLORS = ["brown1", "coral1", "orange2", "PaleGreen3", "DodgerBlue2", "purple3"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10



class CarManager:
    def __init__(self):
        self.carlist = []
        self.startcar()
        self.xiao = 0

    def startcar(self):
        for _ in range(9):
            objecar = Turtle("square")
            objecar.penup()
            objecar.shapesize(stretch_wid=1,stretch_len=2)
            objecar.color(random.choice(COLORS))
            randx = random.randint(-300,300)
            randy = random.randint(-250,260)
            objecar.goto(randx,randy)
            self.carlist.append(objecar)

    def createcar(self):
        objecar = Turtle("square")
        objecar.penup()
        objecar.shapesize(stretch_wid=1,stretch_len=2)
        objecar.color(random.choice(COLORS))
        randx = random.randint(300,800)
        randy = random.randint(-250,260)
        objecar.goto(randx,randy)
        self.carlist.append(objecar)

    def loopmobil (self):
        for mobil in self.carlist:
            if mobil.xcor() < -490:
                refreshx = random.randint(310,800)
                refreshy = random.randint(-250,260)
                mobil.goto(refreshx,refreshy)
                self.xiao += 0.2
                if self.xiao == 1.0:
                    self.createcar()
                    self.xiao = 0
            else:
                pass

    def move(self,level):
        for car in self.carlist:
            car.backward(0.7*level + MOVE_INCREMENT)