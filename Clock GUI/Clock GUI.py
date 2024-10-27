from time import *
from tkinter import *

win = Tk()
def update():
    """
    Using the time module to get the time and relfecting in the 
    label 
    """
    time_string = strftime(" %I:%M:%S %p ")
    time_label.config(text=time_string)

    day_string = strftime("%A")
    day_label.config(text=day_string)
    date_string = strftime("%B %d, %Y")
    date_label.config(text=date_string)
    win.after(1000,update)
win.title("Clock UTC")
win.config(bg="#0ea98d")

time_label = Label(win,font=("Courier",50,"bold"),fg="#a73a20",bg="#0ea98d")
time_label.pack()
day_label = Label(win,font=("Ink Free",25),bg="#0ea98d")
day_label.pack()

date_label = Label(win,font=("Ink Free",25),bg="#0ea98d")
date_label.pack()
update()
win.mainloop()