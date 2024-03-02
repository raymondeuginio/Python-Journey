from turtle import Turtle, Screen
# import random

# timmy = Turtle()
# degree = 360

# Triangle - Hexagon
# timmy.forward(100)
# timmy.right(120)
# timmy.forward(100)
# timmy.right(120)
# timmy.forward(100)
# timmy.right(120)

# for i in range(8):
#     degree /= 4+i
#     for x in range(i+4):
#         timmy.forward(100)
#         timmy.right(degree)
#     degree = 360

#Random Walk
# color = ["pale green", "pale violet red", "sienna1", "slateblue2", "lemon chiffon", "darkorchid2"]
# wheretosee= [-90,90,180,270, -180, -270] # 5
# timmy.pensize(1)
# timmy.speed("fastest")
# while True:
#     timmy.forward(30)
#     angka = random.randint(0,5)
#     timmy.color(color[angka])
#     timmy.right(wheretosee[angka])

#circle many
# for i in range(0,280):
#     angka = random.randint(0,5)
#     timmy.color(color[angka])
#     timmy.right(i)
#     timmy.circle(60)
# screen = Screen()
# screen.exitonclick()

# hirst
# import colorgram
# colors = colorgram.extract('20_001.jpg',10)
# warna = []
# for i in colors:
#     r = i.rgb.r
#     g = i.rgb.g
#     b = i.rgb.b
#     new_color = (r,g,b)
#     warna.append(new_color)

# screen = Screen()
# screen.colormode(255)
# # print(warna)

# color_list = [(229, 228, 226), (225, 223, 224), 
# (199, 175, 117), (124, 36, 24), (210, 221, 213), 
# (168, 106, 57), (222, 224, 227), (186, 158, 53), 
# (6, 57, 83), (109, 67, 85)]

# timmy.pu()
# timmy.hideturtle()
# timmy.setheading(225)
# timmy.forward(250)
# timmy.setheading(0)
# for x in range(10):
#     timmy.setx(-175)
#     for i in range(10):
#         timmy.dot(20,color_list[random.randint(0,len(color_list)-1)])
#         timmy.forward(50)
#     timmy.sety(-125+50*x)


# screen.exitonclick()

#interact with keyboard input
# screen = Screen()

# def move_forwards():
#     timmy.forward(10)

# def move_backwards():
#     timmy.forward(-10)

# def rotateclock():
#     timmy.right(5)

# def rotatecounter():
#     timmy.left(5)

# def clear():
#     timmy.clear()
#     timmy.home()

# screen.listen()
# screen.onkey(key="w", fun=move_forwards)
# screen.onkey(key="a", fun=rotateclock)
# screen.onkey(key="d", fun=rotatecounter)
# screen.onkey(key="s", fun=move_backwards)
# screen.onkey(key="c", fun=clear)

# screen.exitonclick()

# Turtle race
# from turtle import Turtle, Screen
# import random

# is_race_on = False
# screen = Screen()
# screen.setup(width = 500, height = 400)
# user_bet = screen.textinput(title = "Make your bet", prompt="Which turtle will win the race? Enter a color: ")
# colors = ["red", "orange", "yellow", "green", "blue", "purple"]

# tim = Turtle(shape = "turtle")
# tim.color(colors[0])
# tim.pu()
# tim.goto(x=-230, y=-70)

# tom = Turtle(shape = "turtle")
# tom.color(colors[1])
# tom.pu()
# tom.goto(x=-230, y=-40)

# tam = Turtle(shape = "turtle")
# tam.color(colors[2])
# tam.pu()
# tam.goto(x=-230, y=-10)

# tem = Turtle(shape = "turtle")
# tem.color(colors[3])
# tem.pu()
# tem.goto(x=-230, y=20)

# tum = Turtle(shape = "turtle")
# tum.color(colors[4])
# tum.pu()
# tum.goto(x=-230, y=50)

# tym = Turtle(shape = "turtle")
# tym.color(colors[5])
# tym.pu()
# tym.goto(x=-230, y=80)

# if user_bet:
#     is_race_on = True

# while is_race_on:
#     if tim.xcor() > 230:
#         is_race_on = False
#         win = tim.pencolor()
#         if win == user_bet:
#             print(f"You've won! The {win} turtle is the winner!")
#         else:
#             print(f"You've lost! The {win} turtle is the winner!")
#     if tom.xcor() > 230:
#         is_race_on = False
#         win = tom.pencolor()
#         if win == user_bet:
#             print(f"You've won! The {win} turtle is the winner!")
#         else:
#             print(f"You've lost! The {win} turtle is the winner!")
#     if tam.xcor() > 230:
#         is_race_on = False
#         win = tam.pencolor()
#         if win == user_bet:
#             print(f"You've won! The {win} turtle is the winner!")
#         else:
#             print(f"You've lost! The {win} turtle is the winner!")
#     if tem.xcor() > 230:
#         is_race_on = False
#         win = tem.pencolor()
#         if win == user_bet:
#             print(f"You've won! The {win} turtle is the winner!")
#         else:
#             print(f"You've lost! The {win} turtle is the winner!")
#     if tum.xcor() > 230:
#         is_race_on = False
#         win = tum.pencolor()
#         if win == user_bet:
#             print(f"You've won! The {win} turtle is the winner!")
#         else:
#             print(f"You've lost! The {win} turtle is the winner!")
#     if tym.xcor() > 230:
#         is_race_on = False
#         win = tym.pencolor()
#         if win == user_bet:
#             print(f"You've won! The {win} turtle is the winner!")
#         else:
#             print(f"You've lost! The {win} turtle is the winner!")
    
#     tim.forward(random.randint(0,10))
#     tom.forward(random.randint(0,10))
#     tam.forward(random.randint(0,10))
#     tem.forward(random.randint(0,10)) 
#     tum.forward(random.randint(0,10))
#     tym.forward(random.randint(0,10))
# screen.exitonclick()
