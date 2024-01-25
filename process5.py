import tkinter
from tkinter import ttk
from tkinter import messagebox
import sqlite3
from matplotlib import pyplot as plt

def enter_data():

    accepted = accept_var.get()

    if accepted=="Accepted":
         
         #User info
         firstname = first_name_entry.get()
         lastname = last_name_entry.get()

         if firstname and lastname:
             title  = title_combobox.get()
             age = age_spinbox.get()
             state = state_combobox.get()
             dob = Dob_entry.get()
             ten = class10_combobox.get()
             tweleve = class12_combobox.get()
             branch = branch_combobox.get()
             contactNo = contactno_entry.get()


             print("Title :", title, "First Name :", firstname, "Last Name :", lastname)
             print("Age :", age, "State :", state, "DOB :", dob, "Class 10 :", ten,)
             print("Class 12 :", tweleve, "Branch :", branch, "Contact No. :", contactNo)
             print("-------------------------------")


               #Create Table
             #Here we are creating a connection with sqlite3 .connect conn--> connect
             #naming database with name data but should have .db extension
             #conn.close() necessary

            # CREATE TABLE IF NOT EXISTS --> Syntax in mysql(a query)
            # we are saying if the table doesnt exist so create it
            # firstname TEXT (coloum and data type)
            # saved in a variabe called table_create_query

             conn = sqlite3.connect('data3.db')
             table_create_query = '''CREATE TABLE IF NOT EXISTS student_Data3
                     (title TEXT, firstname TEXT, lastname TEXT, age INT, state TEXT,
                     dob INT, ten INT, tweleve INT, branch TEXT, contactNo INT)
             '''

             conn.execute(table_create_query)

              #insert Data 
             data_insert_query = '''INSERT INTO student_Data3 (title, firstname, lastname,
             age, state, dob, ten, tweleve, branch, contactNo) VALUES
             (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''
             data_insert_tuple = (title, firstname, lastname,
                                  age, state, dob, ten, tweleve, branch, contactNo)
             cursor = conn.cursor()
             cursor.execute(data_insert_query, data_insert_tuple)
             conn.commit()
             conn.close()

             

         else:
            tkinter.messagebox.showwarning(title="Error", message="First name and Last name is Required")
          
            show_pie_chart()
    else:
        tkinter.messagebox.showwarning(title="Error", message="You Have Not Aceepted The Terms and Conditions")

def show_pie_chart():
     conn = sqlite3.connect('data3.db')
     cursor = conn.cursor()

    # Selecting data for branches from the database
     query = "SELECT branch, COUNT(*) FROM student_Data3 GROUP BY branch"
     cursor.execute(query)
     data = cursor.fetchall()
     conn.close()

     if data:
        branches, counts = zip(*data)

        # Plotting the pie chart
        plt.pie(counts, labels=branches, autopct='%1.1f%%', startangle=90)
        plt.title("Distribution of Students Across Branches")
        plt.show()
     else:
        tkinter.messagebox.showwarning(title="Error", message="No data available to create a pie chart.")


window  = tkinter.Tk()
window.title("Student Application form for GCET")

frame = tkinter.Frame(window)
frame.pack()

#Saving User Info and using it for further use

user_info_frame = tkinter.LabelFrame(frame, text="User Information")
user_info_frame.grid(row = 0, column = 0, padx = 20, pady = 10)

first_name_label =  tkinter.Label(user_info_frame, text="First Name")
first_name_label.grid(row = 0, column = 1 )
last_name_label= tkinter.Label(user_info_frame, text="Last Name")
last_name_label.grid(row = 0, column  = 2)

first_name_entry = tkinter.Entry(user_info_frame)
last_name_entry =  tkinter.Entry(user_info_frame)

first_name_entry.grid(row = 1, column = 1)
last_name_entry.grid(row = 1, column = 2)

title_label  = tkinter.Label(user_info_frame, text= "Title")
title_combobox  = ttk.Combobox(user_info_frame, values =["", "Mr.", "Mrs. "])
title_label.grid(row = 0, column = 0)
title_combobox.grid(row = 1, column = 0)

age_label = tkinter.Label(user_info_frame, text="Age")
age_spinbox =  tkinter.Spinbox(user_info_frame, from_ = 18, to = 100)
age_label.grid(row = 2, column = 0)
age_spinbox.grid(row = 3, column = 0)

state_label =  tkinter.Label(user_info_frame, text="State")
state_combobox = ttk.Combobox(user_info_frame, values = ["Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", 
                                                               "Chhattisgarh","Delhi", "Goa","Gujarat", "Haryana", "Himachal Pradesh",
                                                               "Jharkhand", "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra",
                                                               "Manipur", "Meghalaya", "Mizoram", "Nagaland", "Odisha","Punjab",
                                                               "Rajasthan", "Sikkim","Tamil Nadu", "Telengana", "Tripura", "Uttar Pradesh",
                                                               "Uttrakhand", "West Bengal"
                                                               ])
state_label.grid(row =  2, column  = 1)
state_combobox.grid(row = 3, column = 1)


Dob_label = tkinter.Label(user_info_frame, text="DOB(DD/MM/YYYY)")
Dob_entry = tkinter.Entry(user_info_frame)
Dob_label.grid(row =2, column=2)
Dob_entry.grid(row = 3, column=2)



for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx  = 10, pady  = 5)

# Saving Courses Info
    

courses_frame  = tkinter.LabelFrame(frame,text="Academic & Courses Info")
courses_frame.grid(row = 1, column =  0, sticky  = "news", padx = 20, pady = 10 )

class10_label =  tkinter.Label(courses_frame, text="Class 10 %")
class10_combobox = ttk.Combobox(courses_frame, values = [">90", "80-90", "70-80", "60-70", "<60"])
class10_label.grid(row =  2, column  = 0)
class10_combobox.grid(row = 3, column = 0)

class12_label =  tkinter.Label(courses_frame, text="class 12 %")
class12_combobox = ttk.Combobox(courses_frame, values = [">90", "80-90", "70-80", "60-70", "<60"])
class12_label.grid(row =  2, column  = 1)
class12_combobox.grid(row = 3, column = 1)

jee_label = tkinter.Label(courses_frame, text="JEE %ile")
jee_combobox = ttk.Combobox(courses_frame, values=[">95", "90-95", "85-80", "75-80","<75"])
jee_label.grid(row=2, column=2)
jee_combobox.grid(row=3,column=2)


branch_label = tkinter.Label(courses_frame, text="Branch")
branch_combobox = ttk.Combobox(courses_frame, values=["CSE", "CE", "ME", "EEE", "ECE", "CS-DS", "CS-AI", "CS-ML"])
branch_label.grid(row=4, column=0)
branch_combobox.grid(row=5, column=0)

contactno_label = tkinter.Label(courses_frame, text="Contact No.")
contactno_label.grid(row =4,column=1)
contactno_entry = tkinter.Entry(courses_frame)
contactno_entry.grid(row=5, column=1)



for widget in courses_frame.winfo_children():
    widget.grid_configure(padx = 10, pady = 5)

# Accept The Terms And Conditions 

terms_frame = tkinter.LabelFrame(frame, text="Terms and Conditions")
terms_frame.grid(row =2 , column = 0, sticky = "news", padx = 20, pady = 10)

accept_var = tkinter.StringVar(value="Not Accepted")

terms_check = tkinter.Checkbutton(terms_frame, text="I Accept The Terms And Conditions", variable =accept_var, onvalue="Accepted", offvalue="Not Accepted")

terms_check.grid(row = 0, column = 0)



#Button
button  = tkinter.Button(frame, text="Enter Data", command= enter_data)
button.grid(row = 3, column = 0, sticky= "news", padx = 20, pady = 10)

showPieChart = tkinter.Button(frame,text="Show Pie",command=show_pie_chart)
showPieChart.grid(row=4, column=0,sticky="news", padx=20, pady=15)


window.mainloop()