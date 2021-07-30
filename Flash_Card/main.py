# ---------------------------- IMPORTS ------------------------------- #
from tkinter import *
import pandas as pd
import random

# ---------------------------- CONSTANTS ------------------------------- #
BACKGROUND_COLOR = "#B1DDC6"
current_word = {}

# ---------------------------- Data ------------------------------- #
try:
    df = pd.read_csv("data/new_words_to_me.csv")
except FileNotFoundError:
    df = pd.read_csv("data/arabic_english.csv")
    # delete the first column
    df = df.drop(["Delete"], axis=1)
    data_list = df.to_dict(orient="records")
else:
    data_list = df.to_dict(orient="records")



# ---------------------------- FUNCTIONS ------------------------------- #
def pick_word():
    global current_word, timer
    window.after_cancel(timer)
    current_word = random.choice(data_list)
    arabic_word = current_word["Arabic"]

    canvas.itemconfig(word, text=arabic_word, fill="black")
    canvas.itemconfig(title, text="ARABIC", fill="black")

    canvas.itemconfig(card_bg, image=front_card_img)

    timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(title, text="ENGLISH", fill="white")
    canvas.itemconfig(word, text=current_word["English"], fill="white")
    canvas.itemconfig(card_bg, image=back_card_img)


def remove_card():
    data_list.remove(current_word)
    pick_word()
    new_data = pd.DataFrame(data_list)
    new_data.to_csv("data/new_words_to_me.csv", index=False)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Flash Card")

# padding
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# time
timer = window.after(3000, func=flip_card)

# for the pic
canvas = Canvas(width=800, height=526)
# the path of the image
front_card_img = PhotoImage(file="images/card_front.png")
back_card_img = PhotoImage(file="images/card_back.png")
# make the image in the bg
card_bg = canvas.create_image(400, 263, image=front_card_img)
canvas.grid(column=0, row=0, columnspan=2)
# change the canvas background
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
# texts inside the canvas
title = canvas.create_text(400, 150, text="-", font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 263, text="-", font=("Ariel", 60, "bold"))

# buttons
wrong_img = PhotoImage(file="images/wrong.png")
correct_img = PhotoImage(file="images/right.png")

wrong_bt = Button(image=wrong_img, highlightthickness=0, command=pick_word)
wrong_bt.grid(row=1, column=0)

correct_bt = Button(image=correct_img, highlightthickness=0, command=remove_card)
correct_bt.grid(row=1, column=1)

# call the function
pick_word()

window.mainloop()
