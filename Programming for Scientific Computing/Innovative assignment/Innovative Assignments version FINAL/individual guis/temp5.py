import tkinter as tk
from tkinter import *


class Toplevel1:
    def __init__(self, top=None):
        top.geometry("411x117+519+278")
        top.minsize(120, 1)
        top.maxsize(1370, 749)
        top.resizable(1, 1)
        top.title("Deposit money")
        p1 = PhotoImage(file='deposit_icon.png')
        top.iconphoto(True, p1)
        top.configure(borderwidth="2")
        top.configure(background="#f2f3f4")

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.146, rely=0.171, height=21, width=164)
        self.Label1.configure(background="#f2f3f4")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font="-family {Segoe UI} -size 9")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''Enter amount to deposit :''')

        self.Entry1 = tk.Entry(top)
        self.Entry1.place(relx=0.535, rely=0.171, height=20, relwidth=0.253)
        self.Entry1.configure(background="#cae4ff")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(selectforeground="#ffffffffffff")

        self.Button1 = tk.Button(top)
        self.Button1.place(relx=0.56, rely=0.598, height=24, width=67)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#004080")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#ffffff")
        self.Button1.configure(highlightbackground="#000000")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Proceed''')

        self.Button2 = tk.Button(top)
        self.Button2.place(relx=0.268, rely=0.598, height=24, width=67)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#004080")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(font="-family {Segoe UI} -size 9")
        self.Button2.configure(foreground="#ffffff")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''Back''')


root = tk.Tk()
top = Toplevel1(root)
root.mainloop()
