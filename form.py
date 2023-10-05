import tkinter 
from tkinter import ttk #themes 
from tkinter import messagebox
def enter_data():
    # ? Acceptance
    accepted = accept_var.get()

    if accepted  == "Accepted":
        #? User Info\
        firstname = first_name_entry.get()
        lastname = last_name_entry.get()
        if firstname and lastname:
            title = title_comobobox.get()
            age = age_spinbox.get()
            nationality = nationality_combobox.get()

            # ?Courses Info
            registration_status = reg_status_var.get()
            numcourses = numcourses_spinbox.get()
            numsemesters = numsemesters_spinbox.get()

            print("First Name:", firstname, "Last Name:", lastname)    
            print("Title:", title, "Age:", age, "Nationality: ", nationality)   
            print("Registration Status: ", registration_status) 
            print("Number of Courses:", numcourses, ", Number of Semesters:", numsemesters)
            print("----------------------***------------------------")
        else:
            messagebox.showwarning(title="Error", message= "You have not filled the Name")
    else:
        messagebox.showwarning(title="Error", message= "You have not accepted the terms and condition")


window = tkinter.Tk()
window.title("Form")


frame = tkinter.Frame(window) #like a div 
frame.pack()#pack place or grid..... You have to follow anyone from them


#3 labels inside the frame(div) 3 rows one column 
# labels are like section inside the frame, cpntaining parameter frame and
# ! FIRST SECTION
user_info_frame = tkinter.LabelFrame(frame, text="User Informaion")
user_info_frame.grid(row=0, column=0, padx=20, pady=10)

first_name_label = tkinter.Label(user_info_frame, text="First Name")
first_name_label.grid(row=0, column=0)
last_name_label = tkinter.Label(user_info_frame, text="Last Name")
last_name_label.grid(row=0, column=1)

first_name_entry = tkinter.Entry(user_info_frame)
last_name_entry = tkinter.Entry(user_info_frame)
first_name_entry.grid(row=1, column=0)
last_name_entry.grid(row=1, column=1)


title_label = tkinter.Label(user_info_frame, text="Title")
title_comobobox = ttk.Combobox(user_info_frame, values=["Mr.", "Ms.", "Dr.", "Prefer not to say"])
title_label.grid(row=0, column=2)
title_comobobox.grid(row=1, column=2)

age_label = tkinter.Label(user_info_frame, text="Age")
age_spinbox = tkinter.Spinbox(user_info_frame, from_=18, to=110)
age_label.grid(row=2, column=0)
age_spinbox.grid(row=3, column=0)

nationality_label = tkinter.Label(user_info_frame, text="Nationalty")
nationality_combobox = ttk.Combobox(user_info_frame, values=["Pakistani", "Indian"])
nationality_label.grid(row=2, column=1)
nationality_combobox.grid(row=3, column=1)

for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)


# ! SECOND SECTION
courses_frame = tkinter.LabelFrame(frame)
courses_frame.grid(row=1, column=0, sticky="news", padx=20, pady=10)

registered_label = tkinter.Label(courses_frame, text="Registration Status")

reg_status_var = tkinter.StringVar(value="Nopss")
registered_check = tkinter.Checkbutton(courses_frame, text="Currently Registered", 
                                       variable= reg_status_var, onvalue="Registetred", offvalue=" Not Registetred")
registered_label.grid(row=0, column=0)
registered_check.grid(row=1, column=0)

numcourses_label = tkinter.Label(courses_frame, text="# Completed Xourses")
numcourses_spinbox = tkinter.Spinbox(courses_frame, from_=0, to="infinity")
numcourses_label.grid(row=0 ,column=1)
numcourses_spinbox .grid(row=1 ,column=1)

numsemesters_label = tkinter.Label(courses_frame, text="# Completed Semesters")
numsemesters_spinbox = tkinter.Spinbox(courses_frame, from_=0, to="infinity")
numsemesters_label.grid(row=0 ,column=2)
numsemesters_spinbox .grid(row=1 ,column=2)

for widget in courses_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# ! THIRD SECTION
terms_frame = tkinter.LabelFrame(frame, text="Terms and Conditions")
terms_frame.grid(row=2, column=0, sticky="news", padx=20, pady=10)

accept_var = tkinter.StringVar(value="Not Accepted")
terms_check = tkinter.Checkbutton(terms_frame, text="I accept thge terms and conditions", 
                                  variable=accept_var, onvalue="Accepted", offvalue="Not Accepted")
terms_check.grid(row=0, column=0)

# ! BUTTONS
button = tkinter.Button(frame, text="Enter Data", command= enter_data)
button.grid(row=3, column=0,sticky="news", padx=20, pady=10)


window.mainloop() #run until we exit the application.it will end when we cross

