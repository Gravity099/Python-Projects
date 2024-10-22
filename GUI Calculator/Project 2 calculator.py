
# Creating a Calculator 
from tkinter import *


data = ""
def get_data(value):
    global data

    data = data+str(value)
    var.set(data)

def clear():
    global data
    data=""
    var.set("0")

def equal_data():
    global data 
    try:
        total = str(eval(data))
        var.set(total)
        data = str(total)
    except Exception:
        var.set("Cannot Divide By 0")


def center_allocation(width,height):
    sys_width = win.winfo_screenwidth()
    sys_height = win.winfo_screenheight()

    corner_x = int(sys_width/2 - width/2)
    corner_y = int(sys_height/2 - height/2)

    
    return corner_x,corner_y
    

win = Tk()
win.title("Calculator")
win.config(bg="grey")
width = 500
height = 500
corner_x, corner_y = center_allocation(width, height)
win.geometry(f"{width}x{height}+{corner_x}+{corner_y}")

win.resizable(False,False)

Title = Label(win,text="CALCULATOR",font=("Arial",25,"bold","italic","underline"),bg="grey")
Title.place(x=125,y=20)

var = StringVar()
entry = Entry(win,relief="sunken",font=("Times New Roman",30,"bold"),bd=4,textvariable=var)
entry.place(x=25,y=95,height=55,width=450)


# ------------------------------ Single Lane 
button_1 = Button(win,text="1",font=("Arial",25,"bold"),command=lambda:get_data("1"))
button_1.place(x=20,y=170,height=60,width=115)

button_2 = Button(win,text="2",font=("Arial",25,"bold"),command=lambda:get_data("2"))
button_2.place(x=135,y=170,height=60,width=115)

button_3 = Button(win,text="3",font=("Arial",25,"bold"),command=lambda:get_data("3"))
button_3.place(x=250,y=170,height=60,width=115)

button_4 = Button(win,text="+",font=("Arial",25,"bold"),command=lambda:get_data("+"))
button_4.place(x=365,y=170,height=60,width=115)

# --------------------------------- Second Lane 
button_5 = Button(win,text="4",font=("Arial",25,"bold"),command=lambda:get_data("4"))
button_5.place(x=20,y=230,height=60,width=115)

button_6 = Button(win,text="5",font=("Arial",25,"bold"),command=lambda:get_data("5"))
button_6.place(x=135,y=230,height=60,width=115)

button_7 = Button(win,text="6",font=("Arial",25,"bold"),command=lambda:get_data("6"))
button_7.place(x=250,y=230,height=60,width=115)

button_8 = Button(win,text="-",font=("Arial",25,"bold"),command=lambda:get_data("-"))
button_8.place(x=365,y=230,height=60,width=115)

# ------------------------------------- Third Lane

button_9 = Button(win,text="7",font=("Arial",25,"bold"),command=lambda:get_data("7"))
button_9.place(x=20,y=290,height=60,width=115)

button_A = Button(win,text="8",font=("Arial",25,"bold"),command=lambda:get_data("8"))
button_A.place(x=135,y=290,height=60,width=115)

button_B = Button(win,text="9",font=("Arial",25,"bold"),command=lambda:get_data("9"))
button_B.place(x=250,y=290,height=60,width=115)

button_C = Button(win,text="x",font=("Arial",25,"bold"),command=lambda:get_data("*"))
button_C.place(x=365,y=290,height=60,width=115)


#--------------------------------------------- Fourth Lane 

button_D = Button(win,text=".",font=("Arial",25,"bold"),command=lambda:get_data("."))
button_D.place(x=20,y=350,height=60,width=115)

button_E = Button(win,text="0",font=("Arial",25,"bold"),command=lambda:get_data("0"))
button_E.place(x=135,y=350,height=60,width=115)

button_F = Button(win,text="C",font=("Arial",25,"bold"),command=clear)
button_F.place(x=250,y=350,height=60,width=115)

button_G = Button(win,text="/",font=("Arial",25,"bold"),command=lambda:get_data("/"))
button_G.place(x=365,y=350,height=60,width=115)

#-------------------------------------------------- Fifth Lane

last_button = Button(win,text="=",font=("Arial",25,"bold"),command=equal_data)
last_button.place(x=20,y=410,height=60,width=460)

win.mainloop()


