from tkinter import *
import pandas as pd
from random import randint,choice

BGCOLOR = "#B1DDC6"
# ------------------------ Data -------------------------
try:
    data = pd.read_csv("./17. Flash Card/data/words_to_learn.csv")
except FileNotFoundError:
    data = pd.read_csv("./17. Flash Card/data/french_words.csv")
to_learn = data.to_dict(orient="records")
current_card = {}

# ------------------------ Button Function --------------------
def nextcard():
    global current_card, fliptimer
    window.after_cancel(fliptimer)

    current_card = choice(to_learn)
    canvas.itemconfig(card_title, text='French', fill="black")
    canvas.itemconfig(canvas_image, image=cardfront)
    canvas.itemconfig(card_word, text=current_card['French'], fill="black")
    fliptimer = window.after(3000,flipcard)

def flipcard():
    canvas.itemconfig(canvas_image, image=cardback)
    canvas.itemconfig(card_title, text='English',fill ="white")
    canvas.itemconfig(card_word, text=current_card['English'], fill="white")
    # print(current_card['English'])

def knewcard():
    to_learn.remove(current_card)
    data = pd.DataFrame(to_learn)
    data.to_csv("./17. Flash Card/data/words_to_learn.csv",index=False)
    nextcard()
# ------------------------ UI -----------------------------------
window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BGCOLOR)

fliptimer = window.after(3000,flipcard)

cardback = PhotoImage(file="./17. Flash Card/images/card_back.png")
cardfront = PhotoImage(file="./17. Flash Card/images/card_front.png")
right = PhotoImage(file="./17. Flash Card/images/right.png")
wrong = PhotoImage(file="./17. Flash Card/images/wrong.png")


canvas = Canvas(width=800, 
                height=526, 
                bg=BGCOLOR, 
                highlightthickness=0)
canvas_image = canvas.create_image(400,263,image=cardfront)
card_title = canvas.create_text(400,150, text="", font=("Arial",40,"italic"))
card_word = canvas.create_text(400,263, text="", font=("Arial",60,"bold"))
canvas.grid(column=0,row=0, columnspan=2)



wrongbutton = Button(image=wrong, highlightthickness=0, command=nextcard)
wrongbutton.grid(column=0,row= 1)

rightbutton = Button(image=right, highlightthickness=0, command=knewcard)
rightbutton.grid(column=1,row=1)

nextcard()

window.mainloop()
