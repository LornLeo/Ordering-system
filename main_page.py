from tkinter import *
from PIL import ImageTk, Image
import math

#Set up the initial menu item dictionaries list
Menu_index=[{'Image_path': 'salmon-fish.jpg', 'Name': 'Grilled salmon fish', 'Price': '$12.99 ', 'Description': 'Tender, flavorful salmon fillet, grilled to perfection with secret herbs and spices.'},
{'Image_path': 'pancake.jpg', 'Name': 'Fluffy Pancake Stack', 'Price': '$9.99 ', 'Description': 'Indulgent pancakes, caramelized edges, topped with syrup, cream, and seasonal fruits.'},
{'Image_path': 'steak.jpg', 'Name': 'Juicy Sirloin Steak', 'Price': '$15.99 ', 'Description': 'Prime beef, seared crust, juicy tenderness, served with roasted vegetables and savory sauces.'}]

#Set up list to store the food item for each category 
category_1_dict=[{'Image_path': 'salmon-fish.jpg', 'Name': 'Grilled salmon fish', 'Price': '$12.99 ', 'Description': 'Tender, flavorful salmon fillet, grilled to perfection with secret herbs and spices.'},
{'Image_path': 'pancake.jpg', 'Name': 'Fluffy Pancake Stack', 'Price': '$9.99 ', 'Description': 'Indulgent pancakes, caramelized edges, topped with syrup, cream, and seasonal fruits.'},
{'Image_path': 'steak.jpg', 'Name': 'Juicy Sirloin Steak', 'Price': '$15.99 ', 'Description': 'Prime beef, seared crust, juicy tenderness, served with roasted vegetables and savory sauces.'}]
category_2_dict=[{'Image_path': 'classic-beef-burger.jpg', 'Name': 'Classic Beef Burger', 'Price': '$12.99 ', 'Description': 
'Beef patty, cheese, sesame seed bun, lettuce, tomato, onions, pickles, ketchup, mustard, and mayo.'},       
{'Image_path': 'chicken-burger.jpg', 'Name': 'Chicken burger', 'Price': '$13.99 ', 'Description': 'Grilled chicken breast, sesame seed bun, lettuce, tomato, onions, pickles, and choice of sauces.'},
{'Image_path': 'fish-sandwich.jpg', 'Name': 'Fish sandwich', 'Price': '$10.99 ', 'Description': 'Crispy fish fillet, soft bun, lettuce, tomato, tartar sauce.'},
{'Image_path': 'pork-roll.jpg', 'Name': 'Pork roll', 'Price': '$11.99 ', 'Description': 'Sliced and seasoned pork roll.'}]
category_3_dict=[{'Image_path': 'terriyaki-chicken.jpg', 'Name': 'Teriyaki chicken', 'Price': '$8.99 ', 'Description': 'Chicken breast, teriyaki sauce (made with soy sauce, mirin, sugar, ginger, and garlic), and optional sesame seeds.'},
{'Image_path': 'beef-broccoli.webp', 'Name': 'Beef broccoli ', 'Price': '$6.99 ', 'Description': 'Beef strips, broccoli florets, soy sauce, garlic, ginger, and optional oyster sauce.'},
{'Image_path': 'tempura-sushi-roll.jpg', 'Name': 'Tempura sushi roll ', 'Price': '$7.99 ', 'Description': 'Sushi rice, nori (seaweed sheet), tempura-fried ingredients, soy sauce, and optional wasabi and pickled ginger.'},
{'Image_path': 'spring-roll.webp', 'Name': 'Spring roll', 'Price': '$13.99 ', 'Description': 'Rice paper wrappers, vermicelli noodles, vegetables, and optional protein, served with dipping sauce.'},
{'Image_path': 'pad-thai.jpg', 'Name': 'Pad thai', 'Price': '$14.99 ', 'Description': 'Rice noodles, tofu or choice of protein, eggs, bean sprouts, green onions, peanuts, tamarind sauce.'}]
category_4_dict=[{'Image_path': 'vegan-pizza.jpg', 'Name': 'Vegan pizza', 'Price': '$12.99 ', 'Description': 'Vegan pizza dough, tomato sauce, vegan cheese, and assorted plant-based toppings.'},
{'Image_path': 'ham-cheese-pizza.jpg', 'Name': 'Ham cheese pizza', 'Price': '$7.99 ', 'Description': 'Pizza dough, tomato sauce, mozzarella cheese, ham slices.'},
{'Image_path': 'chicken-pizza.jpg', 'Name': 'Chicken pizza', 'Price': '$8.99 ', 'Description': 'Pizza dough, tomato sauce, mozzarella cheese, grilled chicken, and choice of additional toppings.'},
{'Image_path': 'pepperoni-pizza.jpg', 'Name': 'Pepperoni pizza', 'Price': '$9.99 ', 'Description': 'Pizza dough, tomato sauce, mozzarella cheese, pepperoni slices.'}]
category_5_dict=[{'Image_path': 'crispy-fried-chicken.jpg', 'Name': 'Crispy fired chicken', 'Price': '$10.99 ', 'Description': 'Chicken pieces, seasoned flour or batter, oil for frying.'},
{'Image_path': 'onion-rings.jpg', 'Name': 'Onion rings', 'Price': '$11.99 ', 'Description': 'Sliced onions, batter, oil for frying.'},
{'Image_path': 'chicken-wings.jpg', 'Name': 'Chicken wings', 'Price': '$13.99 ', 'Description': 'Chicken wings, choice of seasoning or sauce.'},
{'Image_path': 'tempura-vegetables.jpg', 'Name': 'Tempura vegetables', 'Price': '$13.99 ', 'Description': 'Assorted vegetables coated in tempura batter and fried.'}]
category_6_dict=[{'Image_path': 'caesar-salad.jpg', 'Name': 'Caesar salad', 'Price': '$7.99 ', 'Description': 'Romaine lettuce, croutons, Parmesan cheese, garlic, lemon juice, Dijon mustard, egg yolks, olive oil.'},
{'Image_path': 'vegan-wrap.jpg', 'Name': 'Vegan wrap', 'Price': '$8.99 ', 'Description': 'Wrap (e.g., tortilla), choice of vegan protein, assorted vegetables, and vegan sauce or dressing.'}]
category_7_dict=[{'Image_path': 'coke.jpg', 'Name': 'Coke', 'Price': '$9.99 ', 'Description': 'Carbonated water, high fructose corn syrup, caramel color, phosphoric acid, natural flavors, caffeine.'},
{'Image_path': 'iced-tea.jpg', 'Name': 'Iced-tea', 'Price': '$5.99 ', 'Description': 'Black tea or green tea, water, sugar or sweetener, lemon.'},
{'Image_path': 'lemonade.jpg', 'Name': 'Lemonade', 'Price': '$6.99 ', 'Description': 'Freshly squeezed lemons, water, sugar or sweetener.'},
{'Image_path': 'coffee.jpg', 'Name': 'Coffee', 'Price': '$5.99 ', 'Description': 'Coffee beans, hot water.'}]
category_8_dict=[{'Image_path': 'pappardelle-pasta.jpg', 'Name': 'Pappardelee pasta', 'Price': '$13.99 ', 'Description': 'Wide and flat ribbons of egg-based pasta, made with flour and eggs.'},
{'Image_path': 'linguine-pasta.jpg', 'Name': 'Linguine pasta', 'Price': '$12.99 ', 'Description': 'Long, thin, and flat pasta similar to spaghetti, made with durum wheat semolina.'},
{'Image_path': 'farfalle-pasta.jpg', 'Name': 'fafalle pasta', 'Price': '$11.99 ', 'Description': 'Bowtie-shaped pasta made with durum wheat semolina and water.'}]

#set up the category list and category name list to direct the correspond category and its name
category_list=[category_1_dict,category_2_dict,category_3_dict,category_4_dict,category_5_dict,category_6_dict,category_7_dict,category_8_dict]
category_name=["Special","Burgers and Sandwiches","Asian Cuisine","Pizza","Fried Foods","Salads and Wraps","Drinks","Pasta"]

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
