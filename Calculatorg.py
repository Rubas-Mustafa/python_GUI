# import tkinter
from tkinter import *
 
def button_press(num):
    
    global equation_text

    equation_text = equation_text + str(num)
    equation_label.set(equation_text) #equation label will be set to ()

def equals():
    global equation_text
#? Try and Except are like if and else statement but they are used to handle errors
    try: #to check a block of code for errors
        total = str(eval(equation_text))
        equation_label.set(total)
        equation_text = total #if we wanna reuse our total

    except SyntaxError: #to handle errors
        equation_label.set("Syntax Error")

        equation_text = ""
    
    except ZeroDivisionError: #to handle errors
        equation_label.set("Arithmtic Error")

        equation_text = ""
def clear():
     global equation_text

     equation_label.set("")
     equation_text = ""

window = Tk()
window.title("Calculator")
window.geometry("400x500")
window.resizable(False, False)
equation_text=""
equation_label = StringVar()

label = Label(window, textvariable=equation_label, font=("consolas", 20), bg="white", width=24, height=2)
label.pack() #This line of code will decidde the position of chosen variable, in this case we have label : 

frame = Frame(window)
frame.pack()

button1 = Button(frame, text=1, height=4, width=9, font=35, command=lambda: button_press(1)) #to call a Function
button1.grid(row=0, column=0)

button2 = Button(frame, text=2, height=4, width=9, font=35, command=lambda: button_press(2)) #to call a Function
button2.grid(row=0, column=1)

button3 = Button(frame, text=3, height=4, width=9, font=35, command=lambda: button_press(3)) #to call a Function
button3.grid(row=0, column=2)

button4 = Button(frame, text=4, height=4, width=9, font=35, command=lambda: button_press(4)) #to call a Function
button4.grid(row=1, column=0)

button5 = Button(frame, text=5, height=4, width=9, font=35, command=lambda: button_press(5)) #to call a Function
button5.grid(row=1, column=1)

button6 = Button(frame, text=6, height=4, width=9, font=35, command=lambda: button_press(6)) #to call a Function
button6.grid(row=1, column=2)

button7 = Button(frame, text=7, height=4, width=9, font=35, command=lambda: button_press(7)) #to call a Function
button7.grid(row=2, column=0)

button8 = Button(frame, text=8, height=4, width=9, font=35, command=lambda: button_press(8)) #to call a Function
button8.grid(row=2, column=1)

button9 = Button(frame, text=9, height=4, width=9, font=35, command=lambda: button_press(9)) #to call a Function
button9.grid(row=2, column=2)

button0 = Button(frame, text=0, height=4, width=9, font=35, command=lambda: button_press(0)) #to call a Function
button0.grid(row=3, column=0)

plus = Button(frame, text='+', height=4, width=9, font=35, command=lambda: button_press('+')) #to call a Function
plus.grid(row=0, column=3)

minus = Button(frame, text='-', height=4, width=9, font=35, command=lambda: button_press('-')) #to call a Function
minus.grid(row=1, column=3)

multiply= Button(frame, text='*', height=4, width=9, font=35, command=lambda: button_press('*')) #to call a Function
multiply.grid(row=2, column=3)

divide= Button(frame, text='/', height=4, width=9, font=35, command=lambda: button_press('/')) #to call a Function
divide.grid(row=3, column=3)

equal= Button(frame, text='=', height=4, width=9, font=35, command = equals) 
equal.grid(row=3, column=2)

decimal= Button(frame, text='.', height=4, width=9, font=35, command=lambda: button_press('.')) #to call a Function
decimal.grid(row=3, column=1)

clear= Button(window, text='clear', height=4, width=100  , font=35, command= clear) #to call a Function
clear.pack()


window.mainloop()