# import tkinter as tk
# from tkinter import ttk
# root = tk.Tk()
#?  Question NO 1
# * . Write a Python GUI program to import Tkinter package and create a window and set its title
# root.title("-Welcome to Python tkinter Basic exercises-")
# root .mainloop()

# ? Question No 2
# * Write a Python GUI program to import Tkinter package and create a window. Set its title and add a label to the window.
# root.title("Exercise")
# name = tk.Label(root, text="UserName", width=15)
# name.grid(column=0, row=0)
# root.mainloop()

#? Question No 3
#*  Write a Python GUI program to create a label and change the label font style (font name, bold, size) using tkinter module.
# Label = tk.Label(root,  text="Rubas",  font=("Arial Bold", 37))
# Label.grid(column=0, row=0)
# root.mainloop()

#? Question No 4
#* Write a Python GUI program to create a window and set the default window size using tkinter module.
# root.geometry("600x300")
# root.mainloop()

#? Question 5
#*  Write a Python GUI program to create a window and disable to resize the window using tkinter module.
# root.resizable(False, False)
# root.mainloop()

#? Question 6
#* Write a Python GUI program to add a button in your application using tkinter module.
# root.title("Exercise")
# button = tk.Button(text="Submit", width=25, height=3)
# button.pack()
# root.mainloop()

#? Question 7
#* Write a Python GUI program to add a canvas in your application using tkinter module
# canvas = tk.Canvas(root, bg="white", width=100, height=500)
# canvas.pack()
# root.mainloop()

#? Question 8
#* Write a Python GUI program to create two buttons exit and hello using tkinter module.
# def write():
#     print("Tkinter is easy to create GUI")
# exit_button = tk.Button(root, text="Exit",)
# exit_button.grid(row=0, column=0)

# hello_button = tk.Button(root, text="Hello", command=write)
# hello_button.grid(row=0, column=1)
# root.mainloop()

#? Question 9
#* Write a Python GUI program to create a Combobox with three options using tkinter module.
# Combobox = ttk.Combobox(root, values=["Rubas", "Sanabil", "Hebba"], text="Choose One")
# Combobox.pack()
# root.mainloop()

#? Question 10
#* Write a Python GUI program to create a Checkbutton widget using tkinter module.
# ck1 = tk.Checkbutton(root, text="Yes", onvalue=1, offvalue=0)
# ck2 = tk.Checkbutton(root, text="No", onvalue=1, offvalue=0)
# ck1.pack()
# ck2.pack()
# root.mainloop()

#? Question 11
#* Write a Python GUI program to create a Spinbox widget using tkinter module.
# spinbox = tk.Spinbox(root, from_=0, to=10)
# spinbox.pack()
# root.mainloop()

#? Question 12
#* Write a Python GUI program to create a Text widget using tkinter module. Insert a string at the beginning then insert a string into the current text. Delete the first and last character of the text.



#? Question 13
#*  Write a Python GUI program to create three single line text-box to accept a value from the user using tkinter module.
# name = tk.Label(root, text = "Name").place(x = 10, y = 50)
# email = tk.Label(root, text = "User ID").place(x = 10, y = 90)
# password =  tk.Label(root, text = "Password").place(x = 10, y = 130)
# sbmitbtn = tk.Button(root, text = "Submit", activebackground = "green", activeforeground = "blue").place(x = 120, y = 170)
# entry1 = tk.Entry(root).place(x = 85, y = 50)
# entry2 = tk.Entry(root).place(x = 85, y = 90)
# entry3 = tk.Entry(root).place(x = 90, y = 130)
# root.mainloop()


