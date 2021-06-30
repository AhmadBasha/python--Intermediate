# ----------- IMPORTS
from tkinter import *
import math

# ----------- CONSTANTS
FIRST_COLOR = "#FFEAC9"
SECOND_COLOR = "#66DE93"
THIRD_COLOR = "#FF616D"
FOURTH_COLOR = "#D83A56"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ----------- GLOBAL VARIABLE
reps = 0
timer = None


# ----------- TIMER RESET
def reset_timer():
    # stop the timer
    window.after_cancel(timer)
    # change timer label back
    timer_label.config(text="Timer")
    canvas.itemconfig(timer_value, text="00:00")
    # check marks
    checkmark_label.config(text="")

    global reps
    reps = 0


# ----------- TIMER MECHANISM
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # for work time
    # long break
    if reps % 8 == 0:
        countdown(long_break_sec)
        timer_label.config(text="BREAK", fg=FOURTH_COLOR)
    # short break
    elif reps % 2 == 0:
        countdown(short_break_sec)
        timer_label.config(text="BREAK", fg=THIRD_COLOR)
    # work
    else:
        countdown(work_sec)
        timer_label.config(text="WORK", fg=SECOND_COLOR)


# ----------- COUNTDOWN MECHANISM
def countdown(count):
    # number of minutes
    count_min = math.floor(count / 60)
    # number of seconds
    count_sec = count % 60
    # display the second with two zeros instead of one
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_value, text=f"{count_min}:{count_sec}")
    # after waiting time , 1000 => 1s
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += "✔"
        checkmark_label.config(text=marks)


# ----------- UI SETUP
# window & canvas
window = Tk()
window.title("Pomodoro Timer")
# padding
window.config(padx=100, pady=50, bg=FIRST_COLOR)

# for the pic
canvas = Canvas(width=200, height=223, bg=FIRST_COLOR, highlightthickness=0)
# the path of the image
bg_img = PhotoImage(file="tomato.png")
# make the image in the bg
canvas.create_image(100, 112, image=bg_img)
# for the text
timer_value = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# labels
# timer
timer_label = Label(text="Timer", fg=SECOND_COLOR, bg=FIRST_COLOR, font=(FONT_NAME, 50))
timer_label.grid(column=1, row=0)

# checkmark
checkmark_label = Label(fg=SECOND_COLOR, bg=FIRST_COLOR, font=(FONT_NAME, 35, "bold"))
checkmark_label.grid(column=1, row=3)

# buttons
start_bt = Button(text="Start", highlightthickness=0, command=start_timer)
start_bt.grid(column=0, row=2)

reset_bt = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_bt.grid(column=2, row=2)

window.mainloop()
