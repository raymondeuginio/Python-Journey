from tkinter import *
from tkinter import messagebox #ini beda file dengan tkinter
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def makepass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for char in range(nr_letters):
        password_list.append(random.choice(letters))

    for char in range(nr_symbols):
        password_list += random.choice(symbols)

    for char in range(nr_numbers):
        password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = "".join(password_list)

    passwordentry.insert(0,password)
    pyperclip.copy(password)
# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    try:
        with open("./16. Password-Manager/data.json", mode="r") as file:
            # Reading Old data
            data = json.load(file)
            theapp = data[webentry.get()]
            messagebox.showinfo(title=f"{webentry.get()}", message=f"Email: {theapp['email']}\nPassword: {theapp['password']}")
    except KeyError:  
        messagebox.showinfo(title=f"{webentry.get()}", message="No details for the website exist")
    except FileNotFoundError:
        messagebox.showinfo(title="Oops", message="No Data File Found.")

    

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    new_dict = {
        webentry.get():{
            "email": emailentry.get(),
            "password": passwordentry.get()
        }
    }
    if len(webentry.get()) == 0 or len(passwordentry.get()) == 0 or len(emailentry.get()) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=webentry.get(), message=f"These are the details entered: \nEmail: {emailentry.get()}" 
                            f"\nPassword: {passwordentry.get()} \nIs it oke to save?")
        if is_ok:
            # with open("./16. Password-Manager/data.txt", mode="a") as file:
                # dang = file.write(f"{webentry.get()} | {emailentry.get()} | {passwordentry.get()}\n")
            try:
                with open("./16. Password-Manager/data.json", mode="r") as file:
                    # Reading Old data
                    data = json.load(file)
                    
            except:
                with open("./16. Password-Manager/data.json", mode="w") as file:
                    json.dump(new_dict, file, indent=4)
            
            else:
                # Update data
                data.update(new_dict)

                with open("./16. Password-Manager/data.json", mode="w") as file:
                    # Saving updated data
                    json.dump(data, file, indent=4)

            finally:
                webentry.delete(0,END)
                passwordentry.delete(0,END) 

# ---------------------------- UI SETUP ------------------------------- #
FONT_NAME = ("Arial", 15)

window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

canvas = Canvas(width=200,height=200)
locklogo = PhotoImage(file="./16. Password-Manager/logo.png")
canvas.create_image(100,110,image=locklogo)
canvas.grid(column=1,row=0)

# label
weblabel =Label(text="Website:")
weblabel.grid(column=0, row=1)

emaillabel = Label(text="Email/Username:")
emaillabel.grid(column=0, row=2)

passwordlabel = Label(text="Password:", width=21)
passwordlabel.grid(column=0, row=3)

# Entry
webentry = Entry(width=21)
webentry.focus()
webentry.grid(column=1, row=1, sticky="EW")

emailentry= Entry(width=40)
emailentry.insert(0,"johanneskarl50@gmail.com")
emailentry.grid(column=1, row=2, columnspan=2, sticky="EW")

passwordentry = Entry(width=21)
passwordentry.grid(column=1, row=3, sticky="EW")

# Button
generatebutton = Button(text="Generate Password",command=makepass)
generatebutton.grid(column=2,row=3,sticky="EW")

searchbutton = Button(text="Search", width=14, command=find_password)
searchbutton.grid(column=2,row=1, sticky="EW")

addbutton = Button(text="Add",  command=save)
addbutton.grid(column=1,row=4, columnspan=2, sticky="EW")

window.mainloop()