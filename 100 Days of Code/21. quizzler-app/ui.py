THEME_COLOR = "#375362"

from tkinter import *
from quiz_brain import QuizBrain

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain) -> None:
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20,pady=20,bg = THEME_COLOR)

        self.scorelabel = Label(text=f"Score: {self.quiz.score}", font=("Montserrat",10,"bold"), fg="white", bg=THEME_COLOR)
        self.scorelabel.grid(column=1,row=0)

        self.canvas = Canvas(bg="white", width=300,height=250)
        self.question = self.canvas.create_text(
            150, 
            125,
            width=285,
            text="", 
            fill= THEME_COLOR, 
            font=("Arial",16,"italic"))
        self.canvas.grid(column=0,row=1,columnspan=2, pady=50) 

        correctbutton = PhotoImage(file="./21. quizzler-app/images/true.png")
        wrongbutton = PhotoImage(file="./21. quizzler-app/images/false.png")
       
        self.true = Button(image=correctbutton, highlightthickness=0, command=self.buttontrue)
        self.true.grid(column=0,row=2)
        self.false = Button(image=wrongbutton, highlightthickness=0, command=self.buttonfalse)
        self.false.grid(column=1,row=2)


        self.get_next_question()
        self.window.mainloop()
    
    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.scorelabel.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text=q_text)
        else:
            self.canvas.itemconfig(self.question,text="You've reached the end of the quiz.")
            self.true.config(state="disabled")
            self.false.config(state="disabled")
            
    def buttontrue(self):
        self.give_feedback(self.quiz.check_answer("True"))
       
    def buttonfalse(self):
        self.give_feedback(self.quiz.check_answer("False"))
    
    def give_feedback(self, isright):
        if isright:
            self.canvas.config(bg="Green")
        else:
            self.canvas.config(bg="Red")
        self.window.after(2000, self.get_next_question())
