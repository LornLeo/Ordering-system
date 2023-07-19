from tkinter import *
from PIL import ImageTk, Image
import math
Menu_index=[{'Image_path': 'salmon-518032_1280.jpg', 'Name': 'Pizza', 'Price': '$12.99 ', 'Description': 'Savor the taste of our delectable pizza topped with the finest ingredients. Perfectly baked for your enjoyment.'},{'Image_path': 'pancake-1984716_1280.jpg', 'Name': 'Burger', 'Price': '$9.99 ', 'Description': 'Indulge in our mouth-watering burger made with premium ingredients. Juicy, flavorful, and satisfying.'},{'Image_path': 'asparagus-2169305_1280.jpg', 'Name': 'Steak', 'Price': '$153.99 ', 'Description': 'Experience culinary perfection with our prime steak. Tender, flavorful, and cooked to perfection.'},{'Image_path': 'salmon-518032_1280.jpg','Name': 'Sushi','Price': '$14.99','Description': 'Made with the finest seafood and expertly crafted for an unforgettable dinner'}]
page_number=1
total_page_number=math.ceil(len(Menu_index)/3)
window = Tk()

window.geometry('1000x550')
window.title("Menu")
window.resizable(0, 0)
window.configure(bg="white")

left_frame = Frame(window,bg="white")
left_frame.grid(row=0,column=0,rowspan=3,sticky=N)

middle_frame=Frame(window,bg="white")
middle_frame.grid(row=0, column=1,padx=(20,0),pady=(62,0),sticky=N)

menu_title = Label(left_frame,text="Our Menu",font=('Rockwell 21'),bg='#fcc302',fg="white",width=9,padx=30,pady=2)
menu_title.grid(row=0,column=0)

category_1=Button(left_frame,text="Category_1",font=('serif 15'),bg="white",width=18,activebackground="#FBFF3C",activeforeground="black",padx=5)
category_1.grid(row=1,column=0,pady=(25,0))
category_2=Button(left_frame,text="Category_2",font=('serif 15'),bg="white",width=18,activebackground="#FBFF3C",activeforeground="black",padx=5)
category_2.grid(row=2,column=0,pady=(13,0))
category_3=Button(left_frame,text="Category_3",font=('serif 15'),bg="white",width=18,activebackground="#FBFF3C",activeforeground="black",padx=5)
category_3.grid(row=3,column=0,pady=(13,0))
category_4=Button(left_frame,text="Category_4",font=('serif 15'),bg="white",width=18,activebackground="#FBFF3C",activeforeground="black",padx=5)
category_4.grid(row=4,column=0,pady=(13,0))
category_5=Button(left_frame,text="Category_5",font=('serif 15'),bg="white",width=18,activebackground="#FBFF3C",activeforeground="black",padx=5)
category_5.grid(row=5,column=0,pady=(13,0))
category_6=Button(left_frame,text="Category_6",font=('serif 15'),bg="white",width=18,activebackground="#FBFF3C",activeforeground="black",padx=5)
category_6.grid(row=6,column=0,pady=(13,0))
category_7=Button(left_frame,text="Category_7",font=('serif 15'),bg="white",width=18,activebackground="#FBFF3C",activeforeground="black",padx=5)
category_7.grid(row=7,column=0,pady=(13,0))
category_8=Button(left_frame,text="Category_8",font=('serif 15'),bg="white",width=18,activebackground="#FBFF3C",activeforeground="black",padx=5)
category_8.grid(row=8,column=0,pady=(13,0))
