from tkinter import Tk,Label,Button,Entry

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500,height=300)
window.config(padx=100,pady=200)
#Label

mylabel = Label(text="I Am a Label", font = ("Arial",24,"bold"))
mylabel.grid(column=0 ,row=0)
mylabel.config(padx=30,pady=20)
#Button
def button_clicked():
    mylabel["text"] = input.get()

mybutton = Button(text="click me!", command=button_clicked) # command disini = nama fungsi bukan memanggil fungsinya
mybutton.grid(column= 1,row=1)

newbutton = Button(text="New Button", command=button_clicked)
newbutton.grid(column= 2,row=0)

#Entry
input = Entry(width=10)
input.grid(column= 3,row=2)
# inputstr = input.get()

window.mainloop()


