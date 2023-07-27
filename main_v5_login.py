from tkinter import *
from PIL import ImageTk, Image
from csv import writer
from tkinter import messagebox
import csv
import subprocess

def login():
    # Function to handle the login process.
    if Username_ent.get() and Password_ent.get():
        with open("user_database.csv", 'r', newline='') as file:
            csvreader = csv.reader(file)
            rows = list(csvreader)
            a = -1
            error = True
            for row in rows:
                a = a + 1
                if row != []:
                    if row[1] == Username_ent.get():
                        error = False
                        if row[2] == Password_ent.get():
                            window.destroy()
                            update_value("user_database.csv", a, "Status", "online")
                            subprocess.run(['python', 'main_page_v5.py'])
                        else:
                            messagebox.showerror("showerror", "Wrong password")
                            break        
            if error == True:
                messagebox.showerror("showerror", "Invalid username")          
    else:
        if Username_ent.get():
            messagebox.showerror("Error", "Please enter the password")
        else:
            messagebox.showerror("Error", "Please enter the Username")
            
def sign_up():
    # Function to handle the sign-up process by opening the signup window.
    subprocess.run(['python', 'main_v5_signup.py'])

def update_value(csv_file, row_index, column_name, new_value):
    # Function to update the value of a specific cell in the CSV file.
    with open(csv_file, 'r', newline='') as file:
        csv_reader = csv.reader(file)
        rows = list(csv_reader)
        column_index = rows[0].index(column_name)
        rows[row_index][column_index] = new_value

        with open(csv_file, 'w', newline='') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerows(rows)

window = Tk()
window.geometry('850x525')
window.title("Login")
window.resizable(0, 0)
window.configure(bg="white")

Entry_frame = Frame(window,width=400,bg="white")
Entry_frame.place(x=180,y=300)

image_path = "logo.png"
food_image = Image.open(image_path)
resized_image = food_image.resize((200, 200), Image.ANTIALIAS)
image = ImageTk.PhotoImage(resized_image)
Logo = Label(window, image=image, bg="white")
Logo.place(x=325, y=30)


Name_lbl=Label(window,text="Food Shop",bg="white",font=('Rockwell 22'),fg="#fcc302",width=10)
Name_lbl.place(x=343,y=240)
Username_lbl=Label(Entry_frame,text="Username: ",bg="white",font=('Arial 17'))
Username_lbl.grid(row=1,column=0,sticky=W)
Username_ent= Entry(Entry_frame,bd=3,width=25,font=('Arial 19'))
Username_ent.grid(row=1, column=1,columnspan=2,sticky=W)
Password_lbl=Label(Entry_frame,text="Password: ",bg="white",font=('Arial 17'))
Password_lbl.grid(row=2,column=0,sticky=W,pady=(23,0))
Password_ent= Entry(Entry_frame,show="*",bd=3,width=25,font=('Arial 19'))
Password_ent.grid(row=2, column=1,columnspan=2,sticky=W,pady=(23,0))
signup_button = Button(Entry_frame, text="Sign up", command=sign_up,width=18,font=('serif 13'),fg="white",bg="black")
signup_button.grid(row=4,column=1,pady=5)
Login_button = Button(Entry_frame, text="Login", command=login,width=18,font=('serif 13'),fg="white",bg="black")
Login_button.grid(row=4,column=2,pady=5)
try:
    with open("user_database.csv", 'r') as file:
        csvreader = csv.reader(file)
        b=0
        for row in csvreader:
            b=b+1
            if b==1:
                pass
            else:
                update_value("user_database.csv", (b-1), "Status", "offline")
except:
    pass
window.mainloop()
