from tkinter import *
from PIL import ImageTk, Image
import math
from tkinter import ttk

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

#Set up the page number and calculate the total page based on the item in each current menu
page_number=1
total_page_number=math.ceil(len(Menu_index)/3)

#To disable the button selected
disable_list=[None]

#set up the cart list to store the cart_item
cart_list=[]
#set up the total cost list to calculate the total cost of the food item stored in cart  
Totalcost=[]
#set up the cart item dictionary to store the properties of the cart item
cart_item={"Name":"","Quantity":"","Price":""}

#Create the function for the category button when clicking
#When clicking the button, it will change the current menu item to the correspond category
def selected_button(button_name,button_press):
    global Menu_index
    Menu_index=category_list[button_press]
    global total_page_number
    total_page_number=math.ceil(len(Menu_index)/3)
    global page_number
    page_number=1
    page_displayed.configure(text="1"+"/"+str(total_page_number))
    if disable_list[0]!=None:
        disable_list[0].configure(state="normal",bg="white")
    else:
        category_1.configure(state="normal",bg="white")
    disable_list[0]=button_name
    
    food_item_1 = FoodItem(Menu_index[0]['Image_path'], Menu_index[0]['Name'], Menu_index[0]['Price'], Menu_index[0]['Description'],remove_frame=False)
    food_item_1.configure(item1_image, item1_name, item1_price, item1_description,item1_order,item1_quantity)
    if len(category_list[button_press]) > 1:
        food_item2 = FoodItem(Menu_index[1]['Image_path'], Menu_index[1]['Name'], Menu_index[1]['Price'], Menu_index[1]['Description'],remove_frame=False)
        food_item2.grid(item2_image, item2_name, item2_price, item2_description,item2_order,item2_quantity)
        food_item2.configure(item2_image, item2_name, item2_price, item2_description,item2_order,item2_quantity)
    else:
        food_item2 = FoodItem('', '','', '',remove_frame=True)
        
        food_item2.configure(item2_image, item2_name, item2_price, item2_description,item2_order,item2_quantity)
    if len(category_list[button_press]) > 2:
        food_item3 = FoodItem(Menu_index[2]['Image_path'], Menu_index[2]['Name'], Menu_index[2]['Price'], Menu_index[2]['Description'],remove_frame=False)
        food_item3.grid(item3_image, item3_name, item3_price, item3_description,item3_order,item3_quantity)
        food_item3.configure(item3_image, item3_name, item3_price, item3_description,item3_order,item3_quantity)
    else:
        food_item3 = FoodItem('', '','', '',remove_frame=True)
        food_item3.configure(item3_image, item3_name, item3_price, item3_description,item3_order,item3_quantity)
    button_name.configure(state="disabled")
    button_name.configure(bg="yellow")

#create the function for order button when clicking
#When clicking, the food item will add to the cart
def add_order(item_name,item_quantity,item_price):
    cart_item["Name"] = item_name
    cart_item["Quantity"] = item_quantity
    cart_item["Price"] = item_price
    cart_list.append(cart_item)
    price=float(cart_item["Price"].replace('$',""))
    quantity=int(cart_item['Quantity'])
    item_cost=price*quantity
    Totalcost.append(item_cost)
    Total=0
    for item in Totalcost:
        Total=Total+item
    Total_2dp="%.2f" %Total
    Total_cost.configure(text="Total cost: ${}".format(Total_2dp))
    cart_table.insert('', 'end',values=(item_name,item_quantity,item_price))

#When clicking the next page button or last page button, the page will change and show another set of food item
def next_page():
    global page_number   
    if page_number==total_page_number:
        page_number=1
    else:
        page_number=page_number+1
    display=str(page_number)+'/'+str(total_page_number)
    page_displayed.configure(text=display)
    page_displayed.text=display
    food_item_1 = FoodItem(Menu_index[(page_number-1)*3]['Image_path'], Menu_index[(page_number-1)*3]['Name'], Menu_index[(page_number-1)*3]['Price'], Menu_index[(page_number-1)*3]['Description'],remove_frame=False)
    food_item_1.configure(item1_image, item1_name, item1_price, item1_description,item1_order,item1_quantity)
    if ((page_number-1)*3+1)<len(Menu_index):
        food_item2 = FoodItem(Menu_index[(page_number-1)*3+1]['Image_path'], Menu_index[(page_number-1)*3+1]['Name'], Menu_index[(page_number-1)*3+1]['Price'], Menu_index[(page_number-1)*3+1]['Description'],remove_frame=False)
        food_item2.grid(item2_image, item2_name, item2_price, item2_description,item2_order,item2_quantity)
        food_item2.configure(item2_image, item2_name, item2_price, item2_description,item2_order,item2_quantity)
    else:
        food_item2 = FoodItem('', '','', '',remove_frame=True)
        
        food_item2.configure(item2_image, item2_name, item2_price, item2_description,item2_order,item2_quantity)
    if ((page_number-1)*3+2)<len(Menu_index):
        food_item3 = FoodItem(Menu_index[(page_number-1)*3+2]['Image_path'], Menu_index[(page_number-1)*3+2]['Name'], Menu_index[(page_number-1)*3+2]['Price'], Menu_index[(page_number-1)*3+2]['Description'],remove_frame=False)
        food_item3.grid(item3_image, item3_name, item3_price, item3_description,item3_order,item3_quantity)
        food_item3.configure(item3_image, item3_name, item3_price, item3_description,item3_order,item3_quantity)
    else:
        food_item3 = FoodItem('', '','', '',remove_frame=True)
        food_item3.configure(item3_image, item3_name, item3_price, item3_description,item3_order,item3_quantity)
        
def last_page():
    global page_number   
    if page_number==1:
        page_number=total_page_number
    else:
        page_number=page_number-1
    display=str(page_number)+'/'+str(total_page_number)
    page_displayed.configure(text=display)
    page_displayed.text=display
    food_item_1 = FoodItem(Menu_index[(page_number-1)*3]['Image_path'], Menu_index[(page_number-1)*3]['Name'], Menu_index[(page_number-1)*3]['Price'], Menu_index[(page_number-1)*3]['Description'],remove_frame=False)
    food_item_1.configure(item1_image, item1_name, item1_price, item1_description,item1_order,item1_quantity)
    if ((page_number-1)*3+1)<len(Menu_index):
        food_item2 = FoodItem(Menu_index[(page_number-1)*3+1]['Image_path'], Menu_index[(page_number-1)*3+1]['Name'], Menu_index[(page_number-1)*3+1]['Price'], Menu_index[(page_number-1)*3+1]['Description'],remove_frame=False)
        food_item2.grid(item2_image, item2_name, item2_price, item2_description,item2_order,item2_quantity)
        food_item2.configure(item2_image, item2_name, item2_price, item2_description,item2_order,item2_quantity)
    else:
        food_item2 = FoodItem('', '','', '',remove_frame=True)
        
        food_item2.configure(item2_image, item2_name, item2_price, item2_description,item2_order,item2_quantity)
    if ((page_number-1)*3+2)<len(Menu_index):
        food_item3 = FoodItem(Menu_index[(page_number-1)*3+2]['Image_path'], Menu_index[(page_number-1)*3+2]['Name'], Menu_index[(page_number-1)*3+2]['Price'], Menu_index[(page_number-1)*3+2]['Description'],remove_frame=False)
        food_item3.grid(item3_image, item3_name, item3_price, item3_description,item3_order,item3_quantity)
        food_item3.configure(item3_image, item3_name, item3_price, item3_description,item3_order,item3_quantity)
    else:
        food_item3 = FoodItem('', '','', '',remove_frame=True)
        food_item3.configure(item3_image, item3_name, item3_price, item3_description,item3_order,item3_quantity)

#when clicking the button, delete the selected item from cart
def delete_item():
    try:
        selected_item = cart_table.selection()[0]
        current_idx=cart_table.index(selected_item)
        cart_list.remove(cart_list[current_idx])
        Totalcost.remove(Totalcost[current_idx])
        cart_table.delete(selected_item)
        Total=0
        for item in Totalcost:
            Total=Total+item
        Total_2dp="%.2f" %Total
        Total_cost.configure(text="Total cost: ${}".format(Total_2dp))
    except:
        pass
        
#Set up the window 
window = Tk()
window.geometry('1020x550')
window.title("Menu")
window.resizable(0, 0)
window.configure(bg="white")

#Set up the left frame for category button
left_frame = Frame(window,bg="white")
left_frame.grid(row=0,column=0,rowspan=3,sticky=N)

#Set up the middle frame for food item
middle_frame=Frame(window,bg="white",height=400)
middle_frame.grid(row=0, column=1,rowspan=3,padx=(20,0),pady=(62,0),sticky=N)

#Set up the right frame for cart
right_frame=Frame(window,bg="white",width=100)
right_frame.grid(row=0, column=2,rowspan=3,sticky=N)

#Set up all the category buttons and menu title
menu_title = Label(left_frame,text="Our Menu",font=('Rockwell 21'),bg='#fcc302',fg="white",width=9,padx=30,pady=2)
menu_title.grid(row=0,column=0)
category_1=Button(left_frame,text=category_name[0],font=('serif 13'),bg="yellow",width=22,activebackground="#FBFF3C",activeforeground="black",padx=5,pady=5,state="disabled",command=lambda:selected_button(category_1,0))
category_1.grid(row=1,column=0,pady=(25,0),sticky=W)
category_2=Button(left_frame,text=category_name[1],font=('serif 13'),bg="white",width=22,activebackground="#FBFF3C",activeforeground="black",padx=5,pady=5,command=lambda:selected_button(category_2,1))
category_2.grid(row=2,column=0,pady=(12,0),sticky=W)
category_3=Button(left_frame,text=category_name[2],font=('serif 13'),bg="white",width=22,activebackground="#FBFF3C",activeforeground="black",padx=5,pady=5,command=lambda:selected_button(category_3,2))
category_3.grid(row=3,column=0,pady=(12,0),sticky=W)
category_4=Button(left_frame,text=category_name[3],font=('serif 13'),bg="white",width=22,activebackground="#FBFF3C",activeforeground="black",padx=5,pady=5,command=lambda:selected_button(category_4,3))
category_4.grid(row=4,column=0,pady=(12,0),sticky=W)
category_5=Button(left_frame,text=category_name[4],font=('serif 13'),bg="white",width=22,activebackground="#FBFF3C",activeforeground="black",padx=5,pady=5,command=lambda:selected_button(category_5,4))
category_5.grid(row=5,column=0,pady=(12,0),sticky=W)
category_6=Button(left_frame,text=category_name[5],font=('serif 13'),bg="white",width=22,activebackground="#FBFF3C",activeforeground="black",padx=5,pady=5,command=lambda:selected_button(category_6,5))
category_6.grid(row=6,column=0,pady=(12,0),sticky=W)
category_7=Button(left_frame,text=category_name[6],font=('serif 13'),bg="white",width=22,activebackground="#FBFF3C",activeforeground="black",padx=5,pady=5,command=lambda:selected_button(category_7,6))
category_7.grid(row=7,column=0,pady=(12,0),sticky=W)
category_8=Button(left_frame,text=category_name[7],font=('serif 13'),bg="white",width=22,activebackground="#FBFF3C",activeforeground="black",padx=5,pady=5,command=lambda:selected_button(category_8,7))
category_8.grid(row=8,column=0,pady=(12,0),sticky=W)

#Set up GUI for each food items' image, name, price and description.
food_item1=Frame(middle_frame,bg='white')           
food_item1.grid(row=0,column=0,pady=(0,51),padx=0)

food_image1=Image.open(Menu_index[0]["Image_path"])
resized_image = food_image1.resize((150, 100),Image.ANTIALIAS)
food_image1 = ImageTk.PhotoImage(resized_image)
item1_image=Label(food_item1,image='',bg="white",height=100,width=150)
item1_image.grid(row=0,column=0,rowspan=4,sticky=NW)
item1_name=Label(food_item1,text=Menu_index[0]['Name'],bg="white",font=("Arial", 15, "bold"),width=20,anchor=W)
item1_name.grid(row=0,column=1,columnspan=3,sticky=NW,padx=(0,100))
item1_description=Label(food_item1,text=Menu_index[0]['Description'],justify="left",anchor=W,bg="white",wraplength=330,font=("Arial", 9),width=50)
item1_description.grid(row=1,column=1,columnspan=3,padx=0,sticky=NW)
item1_price=Label(food_item1,text=Menu_index[0]['Price'],justify="left",fg="red",wraplength=350,font=("Arial", 12),pady=7,width=10)
item1_price.grid(row=2,column=2,sticky=W,padx=15)
item1_quantity=Spinbox(food_item1,from_=1,to=10,width=5,bg="white",state="readonly")
item1_quantity.grid(row=2,column=1,sticky=W+E+N+S,padx=3)
item1_order=Button(food_item1,text="ORDER",fg="white",bg="red",width=9,font=("Arial", 11,"bold"),command=lambda: add_order(item1_name.cget('text'),item1_quantity.get(),item1_price.cget('text')))
item1_order.grid(row=2,column=3,sticky=W) 

food_item2=Frame(middle_frame,bg='white')           
food_item2.grid(row=1,column=0,pady=(0,51),padx=0)

food_image2=Image.open(Menu_index[0]["Image_path"])
resized_image2 = food_image2.resize((150, 100),Image.ANTIALIAS)
food_image2 = ImageTk.PhotoImage(resized_image)
item2_image=Label(food_item2,image=food_image2,bg="white",height=100,width=150)
item2_image.grid(row=0,column=0,rowspan=4,sticky=NW)
item2_name=Label(food_item2,text=Menu_index[0]['Name'],bg="white",font=("Arial", 15, "bold"),width=20,anchor=W)
item2_name.grid(row=0,column=1,columnspan=3,sticky=NW,padx=(0,100))
item2_description=Label(food_item2,text=Menu_index[0]['Description'],justify="left",anchor=W,bg="white",wraplength=330,font=("Arial", 9),width=50)
item2_description.grid(row=1,column=1,columnspan=3,padx=0,sticky=NW)
item2_price=Label(food_item2,text=Menu_index[0]['Price'],justify="left",fg="red",wraplength=350,font=("Arial", 12),pady=7,width=10)
item2_price.grid(row=2,column=2,sticky=W,padx=15)
item2_quantity=Spinbox(food_item2,from_=1,to=10,width=5,bg="white",state="readonly")
item2_quantity.grid(row=2,column=1,sticky=W+E+N+S,padx=3)
item2_order=Button(food_item2,text="ORDER",fg="white",bg="red",width=9,font=("Arial", 11,"bold"),command=lambda: add_order(item2_name.cget('text'),item2_quantity.get(),item2_price.cget('text')))
item2_order.grid(row=2,column=3,sticky=W)

food_item3=Frame(middle_frame,bg='white')           
food_item3.grid(row=2,column=0,pady=(0,0),padx=0)

food_image3=Image.open(Menu_index[0]["Image_path"])
resized_image3 = food_image3.resize((150, 100),Image.ANTIALIAS)
food_image3 = ImageTk.PhotoImage(resized_image3)
item3_image=Label(food_item3,image=food_image3,bg="white",height=100,width=150)
item3_image.grid(row=0,column=0,rowspan=4,sticky=NW)
item3_name=Label(food_item3,text=Menu_index[0]['Name'],bg="white",font=("Arial", 15, "bold"),width=20,anchor=W)
item3_name.grid(row=0,column=1,columnspan=3,sticky=NW,padx=(0,100))
item3_description=Label(food_item3,text=Menu_index[0]['Description'],justify="left",anchor=W,bg="white",wraplength=330,font=("Arial", 9),width=50)
item3_description.grid(row=1,column=1,columnspan=3,padx=0,sticky=NW)
item3_price=Label(food_item3,text=Menu_index[0]['Price'],justify="left",fg="red",wraplength=350,font=("Arial", 12),pady=7,width=10)
item3_price.grid(row=2,column=2,sticky=W,padx=15)
item3_quantity=Spinbox(food_item3,from_=1,to=10,width=5,bg="white",state="readonly")
item3_quantity.grid(row=2,column=1,sticky=W+E+N+S,padx=3)
item3_order=Button(food_item3,text="ORDER",fg="white",bg="red",width=9,font=("Arial", 11,"bold"),command=lambda: add_order(item3_name.cget('text'),item3_quantity.get(),item3_price.cget('text')))
item3_order.grid(row=2,column=3,sticky=W)

#Set up the page change button and page displayed label
page_change=Frame(window,bg='white')
page_change.place(x=400,y=480)
page_displayed=Label(page_change,borderwidth=1,width=7,text=str(page_number)+'/'+str(total_page_number),bg="white",font=("Arial", 13),relief="solid")
page_displayed.grid(row=0,column=1,sticky=N,pady=(20))
icon_image1=Image.open("11.png")
resized_icon = icon_image1.resize((30, 20))
left_arrowicon = ImageTk.PhotoImage(resized_icon)
next_page=Button(page_change,image=left_arrowicon,command=next_page)
next_page.grid(row=0,column=2,padx=10)
icon_image2=Image.open("b033.png")
resized_icon = icon_image2.resize((30, 20))
right_arrowicon = ImageTk.PhotoImage(resized_icon)
last_page=Button(page_change,image=right_arrowicon,command=last_page)
last_page.grid(row=0,column=0,padx=(0,10))

#Set up the cart
cart_title = Label(right_frame,text="Your Cart",font=('Rockwell 21'),bg='#fcc302',fg="white",width=11,padx=30,pady=3)
cart_title.grid(row=0,column=0)
cart_table=ttk.Treeview(right_frame, column=("Name", "Quantity","Price"), show='headings', height=17)
style=ttk.Style()
style.theme_use('clam')

cart_table.column("# 1",anchor=CENTER,width=120)
cart_table.heading("# 1", text="Name")
cart_table.column("# 2", anchor=CENTER,width=57)
cart_table.heading("# 2", text="Quantity")
cart_table.column("# 3", anchor=CENTER,width=70)
cart_table.heading("# 3", text="Price")
cart_table.grid(row=1,column=0,pady=(25,0))
Total_cost=Label(right_frame,text="Total cost: ",bg="white",font=('Arial 19'),width=15,anchor=W)
Total_cost.grid(row=2,column=0,sticky=W,pady=10)
delete_button=Button(right_frame,text="Delete",width=9,command=delete_item)
delete_button.grid(row=3,column=0,sticky=N,pady=9)


#class the food item
#use init method to set the attribute for each food item,including image, name, price,description
#use grid method to locate each component 
#use configure method to configure each component
class FoodItem:
    def __init__(self,image_path,name,price,description,remove_frame=False):
        self.image_path=image_path
        self.name=name
        self.price=price
        self.description=description
        self.quantity=1
        self.remove_frame=remove_frame
    def grid(self, item_image, item_name, item_price, item_description,item_order,item_quantity):
            item_image.grid(row=0,column=0,rowspan=4,sticky=NW)
            item_name.grid(row=0,column=1,columnspan=3,sticky=NW,padx=(0,100))
            item_description.grid(row=1,column=1,columnspan=3,padx=0,sticky=NW)
            item_price.grid(row=2,column=2,sticky=W,padx=15)
            item_quantity.grid(row=2,column=1,sticky=W+E+N+S,padx=3)
            item_order.grid(row=2,column=3,sticky=W) 

    def configure(self, item_image, item_name, item_price, item_description,item_order,item_quantity):
        if self.remove_frame:
            item_image.grid_remove()
            item_name.grid_remove()
            item_price.grid_remove()
            item_description.grid_remove()
            item_order.grid_remove()
            item_quantity.grid_remove()
        else:
            food_image = Image.open(self.image_path)
            resized_image = food_image.resize((150, 100), Image.ANTIALIAS)
            self.image = ImageTk.PhotoImage(resized_image)
            item_image.image = self.image 
            item_image.configure(image=self.image)
            item_name.configure(text=self.name)
            item_price.configure(text=self.price)
            item_description.configure(text=self.description)
            integer_var = IntVar()
            integer_var.set(self.quantity)
            item_quantity.configure(textvariable=integer_var)
            
#Set the value of each attribute for each food item
food_item1 = FoodItem(Menu_index[0]['Image_path'], Menu_index[0]['Name'], Menu_index[0]['Price'], Menu_index[0]['Description'],remove_frame=False)
food_item1.configure(item1_image, item1_name, item1_price, item1_description,item1_order,item1_quantity)

food_item2 = FoodItem(Menu_index[1]['Image_path'], Menu_index[1]['Name'], Menu_index[1]['Price'], Menu_index[1]['Description'],remove_frame=False)
food_item2.configure(item2_image, item2_name, item2_price, item2_description,item2_order,item2_quantity)

food_item3 = FoodItem(Menu_index[2]['Image_path'], Menu_index[2]['Name'], Menu_index[2]['Price'], Menu_index[2]['Description'],remove_frame=False)
food_item3.configure(item3_image, item3_name, item3_price, item3_description,item3_order,item3_quantity)

window.mainloop()
