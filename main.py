# Choose colours: https://colorhunt.co/

import tkinter as tk
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
CHECK_MARK = "✔"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    tittle_label.config(text="Timer")
    check_marks.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_brake_sec = SHORT_BREAK_MIN * 60
    long_brake_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_brake_sec)
        tittle_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_brake_sec)
        tittle_label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        tittle_label.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):

    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += CHECK_MARK
        check_marks.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Pomodoro Counter")
window.config(padx=100, pady=50, bg=YELLOW)

tittle_label = tk.Label(text="Timer", fg=GREEN, bg=YELLOW, highlightthickness=0, font=(FONT_NAME, 45, "bold"))
tittle_label.grid(column=1,row=0)

canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomate_img = tk.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomate_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = tk.Button(text="Start", highlightthickness=0, font=(FONT_NAME, 15), command=start_timer)
start_button.grid(column=0, row=2)

reset_button = tk.Button(text="Reset", highlightthickness=0, font=(FONT_NAME, 15), command=reset_timer)
reset_button.grid(column=2, row=2)

check_marks = tk.Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20))
check_marks.grid(column=1, row=3)


window.mainloop()