# ---------------------------- imports ------------------------------- #
from tkinter import *
from tkinter import messagebox
import random
# the under to copy directly
# pip install pyperclip
import pyperclip
import json


def search():
    try:
        with open(f"./passwords.json", mode="r") as file:
            # reading the old json data
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showerror(title="WRONG", message=f"There is no file yet")
    else:
        if website_inp.get().title() in data:
            messagebox.showinfo(title=website_inp.get().title(),
                                message=f"Email:\n {data[website_inp.get().title()]['email']}\n"
                                        f"Password:\n {data[website_inp.get().title()]['password']}")
        else:
            messagebox.showerror(title="WRONG", message=f"There is no password for {website_inp.get().title()}")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate():
    # remove any value ine the field
    pass_inp.delete(0, END)

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    random_letters = random.randint(8, 10)
    random_symbols = random.randint(2, 4)
    random_numbers = random.randint(2, 4)

    letters_list = [random.choice(letters) for _ in range(random_letters)]
    symbols_list = [random.choice(symbols) for _ in range(random_symbols)]
    numbers_list = [random.choice(numbers) for _ in range(random_numbers)]
    password_list = letters_list + symbols_list + numbers_list

    random.shuffle(password_list)
    # to make the password
    password = "".join(password_list)
    # put it on the field
    pass_inp.insert(0, password)
    # to copy without click on copy on the interface
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def add_clicked():
    new_data = {
        website_inp.get().title(): {
            "email": email_inp.get(),
            "password": pass_inp.get()
        }
    }
    if (len(website_inp.get()) == 0) | (len(email_inp.get()) == 0) | (len(pass_inp.get()) == 0):
        messagebox.showerror(title="WRONG", message="Don't leave any empty fields")

    # for the pop up window
    else:
        try:
            with open(f"./passwords.json", mode="r") as file:
                # reading the old json data
                data = json.load(file)
        except FileNotFoundError:
            with open(f"./passwords.json", mode="w") as file:
                # saving the updated data
                json.dump(new_data, file, indent=4)
        else:
            # update it
            data.update(new_data)
            with open(f"./passwords.json", mode="w") as file:
                # saving the updated data
                json.dump(data, file, indent=4)
        finally:
            # delete the values after saving
            website_inp.delete(0, END)
            pass_inp.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")

# padding
window.config(padx=50, pady=50)

# for the pic
canvas = Canvas(width=200, height=200)
# the path of the image
bg_img = PhotoImage(file="logo.png")
# make the image in the bg
canvas.create_image(100, 100, image=bg_img)
canvas.grid(column=1, row=0)
# website label
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
# Email/ Username
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)
# password
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# generate button
generate_bt = Button(text="Generate Password", command=generate)
generate_bt.grid(column=2, row=3)

# Add button
add_bt = Button(text="Add", width=36, command=add_clicked)
add_bt.grid(column=1, row=4, columnspan=2)

# search button
search_bt = Button(text="Search", width=13, command=search)
search_bt.grid(column=2, row=1)

# all inputs

# website input
website_inp = Entry(width=21)
website_inp.grid(column=1, row=1)
website_inp.focus()

# email input
email_inp = Entry(width=35)
email_inp.grid(column=1, row=2, columnspan=2)
email_inp.insert(0, "a.ahmadbasha@hotmail.com")

# pass input
pass_inp = Entry(width=21)
pass_inp.grid(column=1, row=3)

window.mainloop()
