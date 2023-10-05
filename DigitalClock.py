from tkinter import *
import time 

root = Tk()
root.title("Sister Of Syntax | Digital Clock")
root.resizable(False,False) 

font = ("Boulder", 68 , "bold")
Label = Label(root, font=font , bg='black' , fg='white' , bd=10)
Label.grid(row=0, column=1)

def function():
    current_time = time.strftime("%H:%M:%S")
    Label.config(text=current_time)
    Label.after(200, function)
function()

root.mainloop() 