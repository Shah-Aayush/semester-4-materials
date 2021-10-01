import tkinter as tk

w = None


class closeAccountByAdmin:
    def __init__(self, top=None):
        top.geometry("411x117+498+261")
        top.minsize(120, 1)
        top.maxsize(1370, 749)
        top.resizable(1,  1)
        top.title("Close account")
        top.configure(background="#f2f3f4")

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.232, rely=0.220, height=20, width=120)
        self.Label1.configure(background="#f2f3f4")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(text='''Enter account number:''')

        self.Entry1 = tk.Entry(top)
        self.Entry1.place(relx=0.536, rely=0.220, height=20, relwidth=0.232)
        self.Entry1.configure(background="#cae4ff")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")

        self.Button1 = tk.Button(top)
        self.Button1.place(relx=0.230, rely=0.598, height=24, width=67)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(borderwidth="0")
        self.Button1.configure(background="#004080")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#ffffff")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text="Back")

        self.Button2 = tk.Button(top)
        self.Button2.place(relx=0.598, rely=0.598, height=24, width=67)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#004080")
        self.Button2.configure(borderwidth="0")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#ffffff")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text="Proceed")


root = tk.Tk()
top = closeAccountByAdmin(root)
root.mainloop()



