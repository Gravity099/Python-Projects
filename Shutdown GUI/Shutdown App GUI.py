from tkinter import *
import os 

def shutdown():
    os.system("shutdown /s /t 0")

def restart():
    os.system("shutdown /r /t 0")

def logout():
    os.system("shutdown /l")

win = Tk()
win.title("Shutdown App")
win.geometry("800x280")
colour_code = "#9e9706"
win.config(bg=colour_code)
restart_image = PhotoImage(file="restart150.png")
logout_image = PhotoImage(file="logout150.png")
shutdown_image = PhotoImage(file="shutdown150.png")

shutdown_button = Button(win,image=shutdown_image,bg=colour_code,relief="groove",cursor="plus",command=shutdown)
shutdown_button.place(x=50,y=30)
logout_button = Button(win,image=logout_image,bg=colour_code,relief="groove",cursor="plus",command=logout)
logout_button.place(x=325,y=30)
restart_button = Button(win,image=restart_image,bg=colour_code,relief="groove",cursor="plus",command=restart)
restart_button.place(x=600,y=30)


shutdown_label = Label(win,text="Shutdown",font=("Arial",12,"bold"),bg=colour_code)
shutdown_label.place(x=95,y=200)
logout_label = Label(win,text="Logout",font=("Arial",12,"bold"),bg=colour_code)
logout_label.place(x=380,y=200)
restart_label = Label(win,text="Restart",font=("Arial",12,"bold"),bg=colour_code)
restart_label.place(x=655,y=200)
win.mainloop()