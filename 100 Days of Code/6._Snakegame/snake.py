from turtle import Turtle
START_POSITION = [(0,0), (-20,0), (-40,0)]
MOVEDISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:
    def __init__(self):
        self.snakebody = []
        self.createsnake()
        self.head = self.snakebody[0]

    def createsnake(self):
        for position in START_POSITION:
            self.add_snake(position)

    def add_snake(self, position):
        tim = Turtle("square")
        tim.color("white")
        tim.pu()
        tim.goto(position)
        self.snakebody.append(tim)
        
    def extend(self):
        self.add_snake(self.snakebody[-1].position())


    def reset(self):
        for seg in self.snakebody:
            seg.goto(1000,1000)
        self.snakebody.clear()
        self.createsnake()
        self.head = self.snakebody[0]


    def move(self):
        for seq_num in range(len(self.snakebody)- 1, 0, -1):
            new_x = self.snakebody[seq_num-1].xcor()
            new_y = self.snakebody[seq_num-1].ycor()
            self.snakebody[seq_num].goto(new_x,new_y)
        
        self.head.forward(MOVEDISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)