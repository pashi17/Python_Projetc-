#without GUI
'''#caffe name
print("VICKY caffe")

#menu items
print("\n Item in the menu List ")
menu_items=[
    '1. Pizza = 50 rup',
    '2. rice = 30 rup',
    '3. samosa = 10 rup',
    '3. paneer tikka = 60 rup',
    '4. paneer roll = 60 rup',
]

#display menu
for item in menu_items:
    print(item)

item1 = int(input("\n Enter the no. of Pizza ="))*50
item2 = int(input(" Enter the no. of Rice ="))*30
item3 = int(input(" Enter the no. of samosa ="))*10
item4 = int(input(" Enter the no. of paneer tikka ="))*60
item5 = int(input(" Enter the no. of paneer roll ="))*60

#calculate total amount
total =item1+item2+item3+item4+item5
print("\n Total amount is =", total)

#check for discount
if str(total).count("0")==2:
     discount = total*0.10
     total -= discount
     print(" you got a 10% discount!")
else:
     discount = 0
     print(" no discount applied. ")
print(" Final amount after discount =",total)     
'''
#with GUI
import tkinter as tk
from tkinter import messagebox

def calculate_total():
    try:
        item1 = int(pizza_entry.get()) * 50
        item2 = int(rice_entry.get()) * 30
        item3 = int(samosa_entry.get()) * 10
        item4 = int(tikka_entry.get()) * 60
        item5 = int(roll_entry.get()) * 60
        
        total = item1 + item2 + item3 + item4 + item5
        
        if str(total).count("0") == 2:
            discount = total * 0.10
            total -= discount
            messagebox.showinfo("Discount", "You got a 10% discount!")
        else:
            discount = 0
            messagebox.showinfo("Discount", "No discount applied.")
        
        total_label.config(text=f"Final amount after discount: {total} rup")
    except ValueError:
        messagebox.showerror("Input error", "Please enter valid numbers!")

# Initialize GUI window
root = tk.Tk()
root.title("VICKY Café")

# Menu labels
menu_label = tk.Label(root, text="Item in the menu List")
menu_label.pack()

pizza_label = tk.Label(root, text="Pizza = 50 rup")
pizza_label.pack()
pizza_entry = tk.Entry(root)
pizza_entry.pack()

rice_label = tk.Label(root, text="Rice = 30 rup")
rice_label.pack()
rice_entry = tk.Entry(root)
rice_entry.pack()

samosa_label = tk.Label(root, text="Samosa = 10 rup")
samosa_label.pack()
samosa_entry = tk.Entry(root)
samosa_entry.pack()

tikka_label = tk.Label(root, text="Paneer Tikka = 60 rup")
tikka_label.pack()
tikka_entry = tk.Entry(root)
tikka_entry.pack()

roll_label = tk.Label(root, text="Paneer Roll = 60 rup")
roll_label.pack()
roll_entry = tk.Entry(root)
roll_entry.pack()

# Calculate button
calculate_button = tk.Button(root, text="Calculate Total", command=calculate_total)
calculate_button.pack()

# Total label
total_label = tk.Label(root, text="Total amount will be shown here.")
total_label.pack()

# Run the application
root.mainloop()



'''import tkinter as tk
from tkinter import messagebox

# Initialize item quantities
pizza_qty = 0
rice_qty = 0
samosa_qty = 0
tikka_qty = 0
roll_qty = 0

# Functions to update item quantities
def update_qty(label, value):
    label.config(text=f"Quantity: {value}")

def increment_pizza():
    global pizza_qty
    pizza_qty += 1
    update_qty(pizza_qty_label, pizza_qty)

def decrement_pizza():
    global pizza_qty
    if pizza_qty > 0:
        pizza_qty -= 1
    update_qty(pizza_qty_label, pizza_qty)

def increment_rice():
    global rice_qty
    rice_qty += 1
    update_qty(rice_qty_label, rice_qty)

def decrement_rice():
    global rice_qty
    if rice_qty > 0:
        rice_qty -= 1
    update_qty(rice_qty_label, rice_qty)

def increment_samosa():
    global samosa_qty
    samosa_qty += 1
    update_qty(samosa_qty_label, samosa_qty)

def decrement_samosa():
    global samosa_qty
    if samosa_qty > 0:
        samosa_qty -= 1
    update_qty(samosa_qty_label, samosa_qty)

def increment_tikka():
    global tikka_qty
    tikka_qty += 1
    update_qty(tikka_qty_label, tikka_qty)

def decrement_tikka():
    global tikka_qty
    if tikka_qty > 0:
        tikka_qty -= 1
    update_qty(tikka_qty_label, tikka_qty)

def increment_roll():
    global roll_qty
    roll_qty += 1
    update_qty(roll_qty_label, roll_qty)

def decrement_roll():
    global roll_qty
    if roll_qty > 0:
        roll_qty -= 1
    update_qty(roll_qty_label, roll_qty)

# Function to calculate total amount
def calculate_total():
    total = (pizza_qty * 50) + (rice_qty * 30) + (samosa_qty * 10) + (tikka_qty * 60) + (roll_qty * 60)
    
    if str(total).count("0") == 2:
        discount = total * 0.10
        total -= discount
        messagebox.showinfo("Discount", "You got a 10% discount!")
    else:
        discount = 0
        messagebox.showinfo("Discount", "No discount applied.")
    
    total_label.config(text=f"Final amount after discount: {total} rup")

# Initialize GUI window
root = tk.Tk()
root.title("VICKY Café")

# Menu labels and buttons
menu_label = tk.Label(root, text="Item in the menu List")
menu_label.pack()

# Pizza
pizza_label = tk.Label(root, text="Pizza = 50 rup")
pizza_label.pack()

pizza_qty_label = tk.Label(root, text="Quantity: 0")
pizza_qty_label.pack()

pizza_inc_btn = tk.Button(root, text="+", command=increment_pizza)
pizza_inc_btn.pack()

pizza_dec_btn = tk.Button(root, text="-", command=decrement_pizza)
pizza_dec_btn.pack()

# Rice
rice_label = tk.Label(root, text="Rice = 30 rup")
rice_label.pack()

rice_qty_label = tk.Label(root, text="Quantity: 0")
rice_qty_label.pack()

rice_inc_btn = tk.Button(root, text="+", command=increment_rice)
rice_inc_btn.pack()

rice_dec_btn = tk.Button(root, text="-", command=decrement_rice)
rice_dec_btn.pack()

# Samosa
samosa_label = tk.Label(root, text="Samosa = 10 rup")
samosa_label.pack()

samosa_qty_label = tk.Label(root, text="Quantity: 0")
samosa_qty_label.pack()

samosa_inc_btn = tk.Button(root, text="+", command=increment_samosa)
samosa_inc_btn.pack()

samosa_dec_btn = tk.Button(root, text="-", command=decrement_samosa)
samosa_dec_btn.pack()

# Paneer Tikka
tikka_label = tk.Label(root, text="Paneer Tikka = 60 rup")
tikka_label.pack()

tikka_qty_label = tk.Label(root, text="Quantity: 0")
tikka_qty_label.pack()

tikka_inc_btn = tk.Button(root, text="+", command=increment_tikka)
tikka_inc_btn.pack()

tikka_dec_btn = tk.Button(root, text="-", command=decrement_tikka)
tikka_dec_btn.pack()

# Paneer Roll
roll_label = tk.Label(root, text="Paneer Roll = 60 rup")
roll_label.pack()

roll_qty_label = tk.Label(root, text="Quantity: 0")
roll_qty_label.pack()

roll_inc_btn = tk.Button(root, text="+", command=increment_roll)
roll_inc_btn.pack()

roll_dec_btn = tk.Button(root, text="-", command=decrement_roll)
roll_dec_btn.pack()

# Calculate button
calculate_button = tk.Button(root, text="Calculate Total", command=calculate_total)
calculate_button.pack()

# Total label
total_label = tk.Label(root, text="Total amount will be shown here.")
total_label.pack()

# Run the application
root.mainloop()
'''

    
