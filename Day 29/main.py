from tkinter import *
from tkinter import messagebox
from random import choice,randint,shuffle
import pyperclip
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
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops",message="Please don't leave empty space!")
    else:
        is_ok = messagebox.askokcancel(title=website,message=f"These are the details entered: \nEmail: {email} \nPassword: {password} \nIs it ok to save?")
        if is_ok:
            with open(r"D:\Python\Day 29\data.txt",mode="a") as file:
                file.write(f"{website}|{email}|{password}\n")
                entry_website.delete(0,END)
                entry_pass.delete(0,END)
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
label_website.grid(column=0, row=1, sticky="W")

# Entry Website
entry_website = Entry(width=35)
entry_website.grid(row=1, column=1, columnspan=2, sticky="W")
entry_website.focus()
# Label Email/Username
label_user = Label(text="Email/Username:")
label_user.grid(column=0, row=2, sticky="W")

# Entry Email/Username
entry_user = Entry(width=35)
entry_user.grid(column=1, columnspan=2, row=2, sticky="W")
entry_user.insert(END,string="trancaoanhkiet@gmail.com")
# Label Password
label_pass = Label(text="Password:")
label_pass.grid(column=0, row=3, sticky="W")

# Frame hold Entry + Button of Password
frame_pass = Frame(window)
frame_pass.grid(column=1, row=3, columnspan=2, sticky="W")

# Entry Password in frame
entry_pass = Entry(frame_pass, width=21)
entry_pass.grid(column=0, row=0)

# Button Generate Password trong frame
button_pass = Button(frame_pass, text="Generate Password",command=generate_password)
button_pass.grid(column=1, row=0, padx=5)

# Button Add
button_add = Button(text="Add", width=36,command=save)
button_add.grid(column=1, columnspan=2, row=4, sticky="W")

window.mainloop()
