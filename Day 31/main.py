BACKGROUND_COLOR = "#B1DDC6"
import pandas
from tkinter import *
import random

to_learn = {}
current_card = {}
try:
    data = pandas.read_csv(r"D:\Python\Day 31\data\words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv(r"D:\Python\Day 31\data\french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")
# ---------------------------- REMOVE WORD ------------------------------- #
def remove_word():
    to_learn.remove(current_card)
    new_data = pandas.DataFrame(to_learn)
    new_data.to_csv("D:\Python\Day 31\data\words_to_learn.csv",index=False)
    next_card()
# ---------------------------- FLIP CARD ------------------------------- #
def flip_card():
    canvas.itemconfig(canvas_image,image = card_back_img)
    canvas.itemconfig(card_title,text = "English",fill = "white")
    canvas.itemconfig(card_word,text = current_card["English"],fill = "white")
# ---------------------------- CREATE FLASH CARD ------------------------------- #
def next_card():
    global current_card,flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title,text = "French",fill = "black")
    canvas.itemconfig(card_word,text = current_card["French"],fill = "black")
    canvas.itemconfig(canvas_image,image =card_front_img)
    flip_timer = window.after(3000,func=flip_card)
# # ---------------------------- UI SETUP ------------------------------- #
# Create Window
window = Tk()
window.title("Flashy")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)
flip_timer = window.after(3000,func=flip_card)
# Logo
canvas = Canvas(width=800,height=526)
card_front_img = PhotoImage(file=r"D:\Python\Day 31\images\card_front.png")
card_back_img = PhotoImage(file=r"D:\Python\Day 31\images\card_back.png")
canvas_image = canvas.create_image(400,263,image = card_front_img)
card_title = canvas.create_text(400,150,text="Title",font=("Arial",40,"italic"))
card_word = canvas.create_text(400,263,text="Word",font=("Ariel",60,"bold"))
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
canvas.grid(row=0,column=0,columnspan=2)
#Button
wrong_image = PhotoImage(file=r"D:\Python\Day 31\images\wrong.png")
wrong_button = Button(image=wrong_image,highlightthickness=0,command=next_card)
wrong_button.grid(row=1,column=0)
correct_image = PhotoImage(file=r"D:\Python\Day 31\images\right.png")
correct_button = Button(image=correct_image,highlightthickness=0,command=remove_word)
correct_button.grid(row=1,column=1)
next_card()
window.mainloop()