from tkinter import Tk, Label, Button, Entry,Text

popwindow = Tk()
popwindow.minsize(width=300,height=100)
popwindow.config(padx=20,pady=20)
FONT=("Monserrat",15)
#Is equal to
iqt = Label(text="is equal to", font=FONT)
iqt.grid(column=0,row=1)

#entry miles
miles_input = Entry(width=10)
miles_input.grid(column=1,row=0)

msatuan = Label(text="Miles",font=FONT)
msatuan.grid(column=2,row=0)

#end result km

def milestokm():
    hasil = int(miles_input.get()) * 1.609
    km["text"] = hasil

km = Label(text="0", font=FONT)
km.grid(column=1,row=1)

kmsatuan = Label(text="Km",font=FONT)
kmsatuan.grid(column=2,row=1)

#calculate button
Calc = Button(text="Calculate", font = FONT, command=milestokm)
Calc.grid(column=1,row=2)



popwindow.mainloop()