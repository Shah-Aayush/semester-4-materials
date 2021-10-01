import tkinter as tk


class deleteAdmin:
    def __init__(self, top=None):
        top.geometry("411x117+504+268")
        top.minsize(120, 1)
        top.maxsize(1370, 749)
        top.resizable(0,0)
        top.title("Delete admin account")
        top.configure(background="#f2f3f4")

        self.Entry1 = tk.Entry(top)
        self.Entry1.place(relx=0.487, rely=0.092, height=20, relwidth=0.277)
        self.Entry1.configure(background="#cae4ff")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.219, rely=0.092, height=21, width=104)
        self.Label1.configure(background="#f2f3f4")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''Enter admin ID:''')

        self.Label2 = tk.Label(top)
        self.Label2.place(relx=0.209, rely=0.33, height=21, width=109)
        self.Label2.configure(background="#f2f3f4")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''Enter password:''')

        self.Entry1_1 = tk.Entry(top)
        self.Entry1_1.place(relx=0.487, rely=0.33, height=20, relwidth=0.277)
        self.Entry1_1.configure(background="#cae4ff")
        self.Entry1_1.configure(disabledforeground="#a3a3a3")
        self.Entry1_1.configure(font="TkFixedFont")
        self.Entry1_1.configure(foreground="#000000")
        self.Entry1_1.configure(highlightbackground="#d9d9d9")
        self.Entry1_1.configure(highlightcolor="black")
        self.Entry1_1.configure(insertbackground="black")
        self.Entry1_1.configure(selectbackground="blue")
        self.Entry1_1.configure(selectforeground="white")

        self.Button1 = tk.Button(top)
        self.Button1.place(relx=0.243, rely=0.642, height=24, width=67)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#004080")
        self.Button1.configure(borderwidth="0")
        self.Button1.configure(cursor="fleur")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#ffffff")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Back''')

        self.Button2 = tk.Button(top)
        self.Button2.place(relx=0.608, rely=0.642, height=24, width=67)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#004080")
        self.Button2.configure(borderwidth="0")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#ffffff")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''Proceed''')


root = tk.Tk()
top = deleteAdmin (root)
root.mainloop()




