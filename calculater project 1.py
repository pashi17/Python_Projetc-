import tkinter as tk

# Function to update the display when a button is clicked
def button_click(value):
    current_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current_text + str(value))

# Function to clear the display
def clear_display():
    entry.delete(0, tk.END)

# Function to evaluate the expression entered by the user
def calculate():
    try:
        result = eval(entry.get())  # Evaluate the expression in the entry box
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

root = tk.Tk()
root.title("Calculator")

# Entry widget for displaying the calculator input/output
entry = tk.Entry(root, font=("Arial", 20), width=16, borderwidth=5, justify='right')
entry.grid(row=0, column=0, columnspan=4)

# Button layout
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

# Create the calculator buttons
for i, button in enumerate(buttons):
    if button == "C":
        tk.Button(root, text=button, font=("Arial", 20), width=4, height=2, command=clear_display).grid(row=i//4 + 1, column=i%4)
    elif button == "=":
        tk.Button(root, text=button, font=("Arial", 20), width=4, height=2, command=calculate).grid(row=i//4 + 1, column=i%4)
    else:
        tk.Button(root, text=button, font=("Arial", 20), width=4, height=2, command=lambda b=button: button_click(b)).grid(row=i//4 + 1, column=i%4)

root.mainloop()
