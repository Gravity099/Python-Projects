
from tkinter import *
from tkinter import messagebox
import pyshorteners

def center_allocation(width,height):
    """
    Allocation the window screen to appear at the center on the window
    """
    sys_width = win.winfo_screenwidth()
    sys_height = win.winfo_screenheight()

    corner_x = int(sys_width/2 - width/2)
    corner_y = int(sys_height/2 - height/2)

    
    return corner_x,corner_y


def flash():
    '''
    Create the flasing for the URL shortener label
    '''
    if display_label["fg"] == "red":
        display_label["fg"] = "green"
    else:
        display_label["fg"] = "red"
    win.after(500,flash)


def short_url():
    '''
    Checks for the url and displays it 
    '''
    min_url = url_entry.get().strip()
    if not min_url:
        messagebox.showinfo(title="URL NOT found",message="Please enter the url")
    actual_url = short.tinyurl.short(min_url)
    var = StringVar()
    var.set(actual_url)
    dis_label = Label(win,text="Shorten URL",font=("Arial",12,"bold"),bg="#c0d827")
    dis_label.place(x=300,y=275)

    second_entry = Entry(win,text="",width=85,textvariable=var)
    second_entry.place(x=85,y=300,height=25)


# Create a Shortener object
short = pyshorteners.Shortener()
win = Tk()

win.title("URL Shortener")

width = 700
height = 400
corner_x, corner_y = center_allocation(width, height)
win.geometry(f"{width}x{height}+{corner_x}+{corner_y}")
win.geometry("700x400")
win.resizable(False,False)
win.config(bg="#c0d827")

# Tkinter widgets Paramenters
display_label = Label(text="URL SHORTENER",font=("Arial",20,"bold"),bg="#c0d827")
display_label.place(x=235,y=20)
flash()

info_label = Label(win,text="Enter the url",font=("Arial",12,"bold"),bg="#c0d827")
info_label.place(x=300,y=110)

url_entry = Entry(win,width=85)
url_entry.place(x=85,y=135,height=25)

proceed_button = Button(win,text="Proceed",command=short_url,bg="#3a51a4",fg="white")
proceed_button.place(x=320,y=190,height=30,width=80)

win.mainloop()