import tkinter as tk
from tkinter import *


class Toplevel1:
    def __init__(self, top=None):
        top.geometry("411x111+505+223")
        top.minsize(120, 1)
        top.maxsize(1370, 749)
        top.resizable(1,  1)
        top.title("Change PIN")
        top.configure(background="#f2f3f4")

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.243, rely=0.144, height=21, width=93)
        self.Label1.configure(background="#f2f3f4")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''Enter new PIN:''')

        self.Label2 = tk.Label(top)
        self.Label2.place(relx=0.268, rely=0.414, height=21, width=82)
        self.Label2.configure(background="#f2f3f4")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''Confirm PIN:''')

        self.Entry1 = tk.Entry(top)
        self.Entry1.place(relx=0.528, rely=0.144, height=20, relwidth=0.229)
        self.Entry1.configure(background="#cae4ff")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")

        self.Entry2 = tk.Entry(top)
        self.Entry2.place(relx=0.528, rely=0.414, height=20, relwidth=0.229)
        self.Entry2.configure(background="#cae4ff")
        self.Entry2.configure(disabledforeground="#a3a3a3")
        self.Entry2.configure(font="TkFixedFont")
        self.Entry2.configure(foreground="#000000")
        self.Entry2.configure(insertbackground="black")

        self.Button1 = tk.Button(top)
        self.Button1.place(relx=0.414, rely=0.721, height=24, width=67)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#004080")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#ffffff")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Proceed''')


root = tk.Tk()
top = Toplevel1 (root)
root.mainloop()



