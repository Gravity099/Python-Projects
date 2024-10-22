
# Basic Report Card Generator 

from tkinter import *
from tkinter.messagebox import askokcancel

def get_data():
    """
    Evaluting the marks obtained by the students and displaying 
    in the message box 
    """
    name = name1.get()
    english = english_marks.get()
    maths = maths_marks.get()
    science = science_marks.get()
    computer = com_marks.get()
    history = history_marks.get()

    avg = round((english+maths+science+computer+history) / 5 )
    if avg > 85:
        grade = "A"
    elif avg > 70 and avg < 85:
        grade = "B"
    elif avg > 60 and avg < 70:
        grade = "C"
    else:
        grade = "FAIL"

    message = [name,avg,grade]
    printf_1 = f"""
                Name        : {message[0]}
                percentage  : {message[1]} %
                Grade       : {message[2]}
                """
    askokcancel(title=("Python School"),message=printf_1)



def center_allocation(width,height):
    """
    Allocation the window screen to appear at the center on the window
    """
    sys_width = win.winfo_screenwidth()
    sys_height = win.winfo_screenheight()

    corner_x = int(sys_width/2 - width/2)
    corner_y = int(sys_height/2 - height/2)

    win.geometry(f"{width}x{height}+{corner_x}+{corner_y}")
    
    return corner_x,corner_y

win = Tk()
win.config(bg="yellow")
win.title("REPORT CARD GENERATOR")
width = 600
height = 800
corner_x , corner_y = center_allocation(width,height)
win.geometry(f"{width}x{height}+{corner_x}+{corner_y}")
win.resizable(False,False)      # will not resize 

school_name =Label(win,text="Python School",font=("Arial",40,"bold"),bg="yellow")
school_name.place(x=100,y=20,height=60,width=400)

name1 = StringVar()

st_name = Label(win,text="Student Name",font=("Arial",20,"bold"),bg="yellow")
st_name.place(x=10,y=120,height=60,width=200)

st_name_entry = Entry(win,font=("Arial",18,"bold"),textvariable=name1)
st_name_entry.place(x=240,y=130,height=35,width=300)

#--------------------------------------------------------Title and Entry Box 

subject_name =Label(win,text="SUBJECTS",font=("Arial",25,"bold"),bg="yellow")
subject_name.place(x=100,y=185,height=60,width=400)


# Declaring the Tkinter Variable 
english_marks = IntVar()
maths_marks = IntVar()
science_marks = IntVar()
com_marks = IntVar()
history_marks = IntVar()

english = Label(win,text="English ",font=("Arial",20,"bold"),bg="yellow")
english.place(x=10,y=250,height=60,width=200)

english_entry = Entry(win,font=("Arial",18,"bold"),textvariable=english_marks)
english_entry.place(x=240,y=260,height=35,width=300)

#---------------------------------------------------------- English label and Entry box 

maths = Label(win,text="Maths",font=("Arial",20,"bold"),bg="yellow")
maths.place(x=10,y=330,height=60,width=200)

maths_entry = Entry(win,font=("Arial",18,"bold"),textvariable=maths_marks)
maths_entry.place(x=240,y=340,height=35,width=300)

#----------------------------------------------------------- Maths Label and Entry Box 

science = Label(win,text="Science",font=("Arial",20,"bold"),bg="yellow")
science.place(x=10,y=420,height=60,width=200)

science_entry = Entry(win,font=("Arial",18,"bold"),textvariable=science_marks)
science_entry.place(x=240,y=430,height=35,width=300)

#-----------------------------------------------------------Science Label and Entry Box 

com = Label(win,text="Computer",font=("Arial",20,"bold"),bg="yellow")
com.place(x=10,y=500,height=60,width=200)

com_entry = Entry(win,font=("Arial",18,"bold"),textvariable=com_marks)
com_entry.place(x=240,y=510,height=35,width=300)

#-----------------------------------------------------------Computer Label and Entry Box 

history = Label(win,text="History",font=("Arial",20,"bold"),bg="yellow")
history.place(x=10,y=580,height=60,width=200)

history_entry = Entry(win,font=("Arial",18,"bold"),textvariable=history_marks)
history_entry.place(x=240,y=590,height=35,width=300)

#-----------------------------------------------------------History Label and Entry Box 


done = Button(win,text="DONE",font=("Arial",20,"bold"),command=get_data)
done.place(x=280,y=700,height=40,width=120)
#------------------------------------------------------------Done Button


win.mainloop()
