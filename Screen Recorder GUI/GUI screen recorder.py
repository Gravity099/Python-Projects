# Note : That canbe more customized , adding the notification along with status indicator , Basic utility
from tkinter import *
from tkinter import filedialog
from pyscreenrec import ScreenRecorder
import os


# Creating a Recorder Instance
recorder = ScreenRecorder()
def start_rec():
    """
    Function used to start the recording and disbale the start button
    and enabling the pause and stop button
    Same to reflect on the bottom status Bar
    """
    status_label["text"] = "Recording Started"
    win.after(500,win.iconify)
    recorder.start_recording()
    start_button["state"] = "disabled"
    pause_button["state"] = "normal"
    stop_button["state"] = "normal"

def pause_rec():
        """
        Contion check to pause and resume the recording and reflecting 
        on the status bar
        """
        if pause_button["text"] == "PAUSE":
            recorder.pause_recording()
            pause_button["text"] = "RESUME"
            status_label["text"] = "Recording Resume"
            print("Recording Paused")
        else:
            recorder.resume_recording()
            pause_button["text"] = "PAUSE"
            status_label["text"] = "Recording Continue"
            print("Recording Continued.")


def stop_rec():
    """
    Stoping the recording and moving the file from current dir 
    to desired location 
    """
    recorder.stop_recording()

    # Open the save dialog and get the file path
    saved_video = filedialog.asksaveasfilename(defaultextension=".mp4",
                                           filetypes=[("MP4 files", "*.mp4"), ("All files", "*.*")],
                                           title="Save the recorded video")
    if saved_video:
        loc = saved_video  
        temp_file = "Recording.mp4"  # This should be the original recorded file name
        os.rename(temp_file, loc)
    
    start_button["state"] = "normal"
    status_label["text"] = "Recording Stopped"

def center_allocation(width,height):
    """
    Allocation the window screen to appear at the center on the window
    """
    sys_width = win.winfo_screenwidth()
    sys_height = win.winfo_screenheight()

    corner_x = int(sys_width/2 - width/2)
    corner_y = int(sys_height/2 - height/2)

    
    return corner_x,corner_y

    
win = Tk()
width = 700
height = 500
corner_x, corner_y = center_allocation(width, height)
win.geometry(f"{width}x{height}+{corner_x}+{corner_y}")
win.geometry("700x500")
win.title("Screen Recorder")
win.resizable(False,False)
image_set= PhotoImage(file="beach0031.png")

set_back = Label(win,image=image_set)
set_back.pack(expand=True)

Lab = Label(text="Screen Recorder",fg="red",font=("Arial",25,"bold"),bg="#c5f4ec")
Lab.place(x=235,y=50)

status_label = Label(win,text="Status",bg="black",fg="white",font=("Arial",10,"bold"))
status_label.place(x=250,y=482,height=16,width=250)

start_button  = Button(win,text="START",font=("Arial",10,"bold"),activeforeground="#612047",activebackground="#c1adb9",command=start_rec)
start_button.place(x=50,y=300,height=50,width=75)
pause_button = Button(win,text="PAUSE",font=("Arial",10,"bold"),activeforeground="#612047",activebackground="#c1adb9",command=pause_rec)
pause_button.place(x=335,y=300,height=50,width=75)
pause_button["state"] = "disabled"
stop_button  = Button(win,text="STOP",font=("Arial",10,"bold"),activeforeground="#612047",activebackground="#c1adb9",command=stop_rec)
stop_button.place(x=600,y=300,height=50,width=75)
stop_button["state"] = "disabled"

win.mainloop()