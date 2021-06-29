from tkinter import *


def button_clicked():
    # change label
    value_label["text"] = "{:.2f}".format(float(input_.get()) * 1.609)


# create the window
window = Tk()

window.title("Mile To Km")

# size
# window.minsize(width=150, height=150)
# padding
window.config(padx=30, pady=30)

# input
input_ = Entry(width=8)
# input_.pack()
input_.grid(column=1, row=0)
input_.focus()

# label
miles_label = Label(text="Miles", font=22)
# show label
miles_label.grid(column=2, row=0)

# label
is_equal_label = Label(text="Is Equal To", font=22)
# show label
is_equal_label.grid(column=0, row=1)

# label
value_label = Label(text="0", font=22)
# show label
value_label.grid(column=1, row=1)

# label
km_label = Label(text="Km", font=22)
# show label
km_label.grid(column=2, row=1)

# button
button = Button(text="Calculate", command=button_clicked)
# button.pack()
button.grid(column=1, row=2)

# to let the screen open and always at the end.
window.mainloop()
