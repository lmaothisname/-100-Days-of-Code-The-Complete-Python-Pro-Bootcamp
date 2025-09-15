from tkinter import *
from tkinter import messagebox
from random import choice,randint,shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for char in range(randint(8,10))]
    password_numbers = [choice(numbers) for char in range(randint(2,4))]
    password_symbols = [choice(symbols) for char in range(randint(2,4))]
    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)
    password = "".join(password_list)
    entry_pass.insert(0,password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = entry_website.get()
    email = entry_user.get()
    password = entry_pass.get()
    new_data = {
        website : {
            "email" : email,
            "password" : password,
        }
    }
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops",message="Please don't leave empty space!")
    else:
        try:
            with open(r"D:\Python\Day 29\data.json",mode="r") as file:
                #Reading old data
                data = json.load(file)
        except FileNotFoundError:
            with open(r"D:\Python\Day 29\data.json",mode="w") as file:
                json.dump(new_data,file,indent=4)
        else:
            #Updating old data with new data
            data.update(new_data)
            with open(r"D:\Python\Day 29\data.json",mode="w") as file:
                #Saving updated data
                json.dump(data,file,indent=4)
        finally:
            entry_website.delete(0,END)
            entry_pass.delete(0,END)
# ---------------------------- FIND PASSWORD  ------------------------------- #
def find_password():
    website = entry_website.get()
    try:
        with open(r"D:\Python\Day 29\data.json") as file:
            data = json.load(file)
    except FileNotFoundError:
            messagebox.showinfo(title="Error",message="No Data File Found.")
    else:
        if website in data:
            messagebox.showinfo(title=website,message=f"Email: {data[website]["email"]}\nPassword: {data[website]["password"]}")
        else:
                messagebox.showinfo(title="Error",message=f"No Detail for {website} exists.")
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

# Logo
canvas = Canvas(width=200, height=200, highlightthickness=0)
password_img = PhotoImage(file=r"D:\Python\Day 29\logo.png")
canvas.create_image(100, 100, image=password_img)
canvas.grid(column=1, row=0)

# Label Website
label_website = Label(text="Website:")
label_website.grid(column=0, row=1, sticky="E")

# Entry Website
entry_website = Entry(width=35)
entry_website.grid(row=1, column=1, sticky="EW")
entry_website.focus()
# Search Button
search_button = Button(text="Search",command=find_password)
search_button.grid(column=2,row=1,sticky="EW")
# Label Email/Username
label_user = Label(text="Email/Username:")
label_user.grid(column=0, row=2, sticky="E")

# Entry Email/Username
entry_user = Entry(width=35)
entry_user.grid(column=1, columnspan=2, row=2, sticky="EW")
entry_user.insert(END,string="trancaoanhkiet@gmail.com")
# Label Password
label_pass = Label(text="Password:")
label_pass.grid(column=0, row=3, sticky="E")

# Entry Password in frame
entry_pass = Entry(width=21)
entry_pass.grid(column=1, row=3,sticky="EW")

# Button Generate Password
button_pass = Button(text="Generate Password",command=generate_password)
button_pass.grid(column=2, row=3, sticky="EW")

# Button Add
button_add = Button(text="Add",command=save)
button_add.grid(column=1, columnspan=2, row=4, sticky="EW")

window.mainloop()
