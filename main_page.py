from tkinter import *
from PIL import ImageTk, Image
import math

#Set up the initial menu item dictionaries list
Menu_index=[{'Image_path': 'salmon-fish.jpg', 'Name': 'Grilled salmon fish', 'Price': '$12.99 ', 'Description': 'Tender, flavorful salmon fillet, grilled to perfection with secret herbs and spices.'},
{'Image_path': 'pancake.jpg', 'Name': 'Fluffy Pancake Stack', 'Price': '$9.99 ', 'Description': 'Indulgent pancakes, caramelized edges, topped with syrup, cream, and seasonal fruits.'},
{'Image_path': 'steak.jpg', 'Name': 'Juicy Sirloin Steak', 'Price': '$15.99 ', 'Description': 'Prime beef, seared crust, juicy tenderness, served with roasted vegetables and savory sauces.'}]

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

food_item1=Frame(middle_frame,bg='white')           
food_item1.grid(row=0,column=0,pady=(0,51),padx=0)

food_image1=Image.open(Menu_index[0]["Image_path"])
resized_image = food_image1.resize((150, 100),Image.ANTIALIAS)
food_image1 = ImageTk.PhotoImage(resized_image)
item1_image=Label(food_item1,image=food_image1,bg="white",height=100,width=150)
item1_image.grid(row=0,column=0,rowspan=4,sticky=NW)
item1_name=Label(food_item1,text=Menu_index[0]['Name'],bg="white",font=("Arial", 15, "bold"),width=15,anchor=W)
item1_name.grid(row=0,column=1,columnspan=3,sticky=NW,padx=(0,100))
item1_description=Label(food_item1,text=Menu_index[0]['Description'],justify="left",anchor=W,bg="white",wraplength=370,font=("Arial", 9),width=50)
item1_description.grid(row=1,column=1,columnspan=3,padx=0,sticky=NW)
item1_price=Label(food_item1,text=Menu_index[0]['Price'],justify="left",fg="red",wraplength=350,font=("Arial", 12),pady=7,width=10)
item1_price.grid(row=2,column=2,sticky=W,padx=15)
item1_quantity=Spinbox(food_item1,from_=1,to=10,width=5,bg="white",state="readonly")
item1_quantity.grid(row=2,column=1,sticky=W+E+N+S,padx=3)
item1_order=Button(food_item1,text="ORDER",fg="white",bg="red",width=9,font=("Arial", 11,"bold"))
item1_order.grid(row=2,column=3,sticky=W) 

food_item2=Frame(middle_frame,bg='white')           
food_item2.grid(row=1,column=0,pady=(0,51),padx=0)

food_image2=Image.open(Menu_index[1]["Image_path"])
resized_image2 = food_image2.resize((150, 100),Image.ANTIALIAS)
food_image2 = ImageTk.PhotoImage(resized_image2)
item2_image=Label(food_item2,image=food_image2,bg="white",height=100,width=150)
item2_image.grid(row=0,column=0,rowspan=4,sticky=NW)
item2_name=Label(food_item2,text=Menu_index[1]['Name'],bg="white",font=("Arial", 15, "bold"),width=15,anchor=W)
item2_name.grid(row=0,column=1,columnspan=3,sticky=NW,padx=(0,100))
item2_description=Label(food_item2,text=Menu_index[1]['Description'],justify="left",anchor=W,bg="white",wraplength=370,font=("Arial", 9),width=50)
item2_description.grid(row=1,column=1,columnspan=3,padx=0,sticky=NW)
item2_price=Label(food_item2,text=Menu_index[1]['Price'],justify="left",fg="red",wraplength=350,font=("Arial", 12),pady=7,width=10)
item2_price.grid(row=2,column=2,sticky=W,padx=15)
item2_quantity=Spinbox(food_item2,from_=1,to=10,width=5,bg="white",state="readonly")
item2_quantity.grid(row=2,column=1,sticky=W+E+N+S,padx=3)
item2_order=Button(food_item2,text="ORDER",fg="white",bg="red",width=9,font=("Arial", 11,"bold"))
item2_order.grid(row=2,column=3,sticky=W)

food_item3=Frame(middle_frame,bg='white')           
food_item3.grid(row=2,column=0,pady=(0,0),padx=0)

food_image3=Image.open(Menu_index[2]["Image_path"])
resized_image3 = food_image3.resize((150, 100),Image.ANTIALIAS)
food_image3 = ImageTk.PhotoImage(resized_image3)
item3_image=Label(food_item3,image=food_image3,bg="white",height=100,width=150)
item3_image.grid(row=0,column=0,rowspan=4,sticky=NW)
item3_name=Label(food_item3,text=Menu_index[2]['Name'],bg="white",font=("Arial", 15, "bold"),width=15,anchor=W)
item3_name.grid(row=0,column=1,columnspan=3,sticky=NW,padx=(0,100))
item3_description=Label(food_item3,text=Menu_index[2]['Description'],justify="left",anchor=W,bg="white",wraplength=370,font=("Arial", 9),width=50)
item3_description.grid(row=1,column=1,columnspan=3,padx=0,sticky=NW)
item3_price=Label(food_item3,text=Menu_index[2]['Price'],justify="left",fg="red",wraplength=350,font=("Arial", 12),pady=7,width=10)
item3_price.grid(row=2,column=2,sticky=W,padx=15)
item3_quantity=Spinbox(food_item3,from_=1,to=10,width=5,bg="white",state="readonly")
item3_quantity.grid(row=2,column=1,sticky=W+E+N+S,padx=3)
item3_order=Button(food_item3,text="ORDER",fg="white",bg="red",width=9,font=("Arial", 11,"bold"))
item3_order.grid(row=2,column=3,sticky=W)

page_change=Frame(window,bg='white')
page_change.grid(row=1,column=1)
page_displayed=Label(page_change,borderwidth=1,width=7,text=str(page_number)+'/'+str(total_page_number),bg="white",font=("Arial", 13),relief="solid")
page_displayed.grid(row=0,column=1,sticky=N,pady=(20))
icon_image1=Image.open("11.png")
resized_icon = icon_image1.resize((30, 20))
left_arrowicon = ImageTk.PhotoImage(resized_icon)
next_page=Button(page_change,image=left_arrowicon)
next_page.grid(row=0,column=2,padx=10)
icon_image2=Image.open("b033.png")
resized_icon = icon_image2.resize((30, 20))
right_arrowicon = ImageTk.PhotoImage(resized_icon)
last_page=Button(page_change,image=right_arrowicon)
last_page.grid(row=0,column=0,padx=(0,10))
window.mainloop()
