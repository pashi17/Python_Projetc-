import tkinter as tk
from time import strftime
root=tk.Tk()
root.title("Digital clock")

def time():
    string=strftime('%H:%M: %S %p \n %D \n %d -%m -%y')
    Label.config(text=string)
    Label.after(1000,time)
Label =tk.Label(root,font=('Algerian',50,'bold'),background='black',foreground='red')
Label.pack(anchor='center')
time()

root.mainloop()
