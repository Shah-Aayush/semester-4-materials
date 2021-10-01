import tkinter as tk


class createAdmin:
    def __init__(self, top=None):
        top.geometry("411x150+512+237")
        top.minsize(120, 1)
        top.maxsize(1370, 749)
        top.resizable(1,  1)
        top.title("Create admin account")
        top.configure(background="#f2f3f4")

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.219, rely=0.067, height=27, width=104)
        self.Label1.configure(background="#f2f3f4")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''Enter admin ID:''')

        self.Label2 = tk.Label(top)
        self.Label2.place(relx=0.219, rely=0.267, height=27, width=104)
        self.Label2.configure(background="#f2f3f4")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''Enter password:''')

        self.Entry1 = tk.Entry(top)
        self.Entry1.place(relx=0.487, rely=0.087, height=20, relwidth=0.326)
        self.Entry1.configure(background="#cae4ff")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")

        self.Entry2 = tk.Entry(top)
        self.Entry2.place(relx=0.487, rely=0.287, height=20, relwidth=0.326)
        self.Entry2.configure(background="#cae4ff")
        self.Entry2.configure(disabledforeground="#a3a3a3")
        self.Entry2.configure(font="TkFixedFont")
        self.Entry2.configure(foreground="#000000")
        self.Entry2.configure(insertbackground="black")

        self.Label3 = tk.Label(top)
        self.Label3.place(relx=0.195, rely=0.467, height=27, width=104)
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(activeforeground="black")
        self.Label3.configure(background="#f2f3f4")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(highlightbackground="#d9d9d9")
        self.Label3.configure(highlightcolor="black")
        self.Label3.configure(text='''Confirm password:''')

        self.Entry3 = tk.Entry(top)
        self.Entry3.place(relx=0.487, rely=0.487, height=20, relwidth=0.326)
        self.Entry3.configure(background="#cae4ff")
        self.Entry3.configure(disabledforeground="#a3a3a3")
        self.Entry3.configure(font="TkFixedFont")
        self.Entry3.configure(foreground="#000000")
        self.Entry3.configure(insertbackground="black")

        self.Button1 = tk.Button(top)
        self.Button1.place(relx=0.598, rely=0.733, height=24, width=67)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#004080")
        self.Button1.configure(borderwidth="0")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#ffffff")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text="Proceed")

        self.Button2 = tk.Button(top)
        self.Button2.place(relx=0.230, rely=0.733, height=24, width=67)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#004080")
        self.Button2.configure(borderwidth="0")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#ffffff")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text="Back")


root = tk.Tk()
top = createAdmin(root)
root.mainloop()



