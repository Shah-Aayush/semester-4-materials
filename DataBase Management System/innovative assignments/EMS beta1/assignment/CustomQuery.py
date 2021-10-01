import tkinter as tk


class CustomQuery:
    def __init__(self, top=None):
        top.geometry("705x450+352+143")
        top.minsize(120, 1)
        top.maxsize(1370, 749)
        top.resizable(0,0)
        top.title("Custom Query")
        top.configure(background="#212529")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.014, rely=0.067, height=19, width=53)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#212529")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#ffffff")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''Query :''')

        self.Query = tk.Entry(top)
        self.Query.place(relx=0.085, rely=0.067, height=20, relwidth=0.743)
        self.Query.configure(background="white")
        self.Query.configure(disabledforeground="#a3a3a3")
        self.Query.configure(font="TkFixedFont")
        self.Query.configure(foreground="#000000")
        self.Query.configure(highlightbackground="#d9d9d9")
        self.Query.configure(highlightcolor="black")
        self.Query.configure(insertbackground="black")
        self.Query.configure(selectbackground="blue")
        self.Query.configure(selectforeground="white")

        self.execute_button = tk.Button(top)
        self.execute_button.place(relx=0.837, rely=0.067, height=24, width=87)
        self.execute_button.configure(activebackground="#ececec")
        self.execute_button.configure(activeforeground="#000000")
        self.execute_button.configure(background="#CED4DA")
        self.execute_button.configure(disabledforeground="#a3a3a3")
        self.execute_button.configure(foreground="#000000")
        self.execute_button.configure(highlightbackground="#d9d9d9")
        self.execute_button.configure(highlightcolor="black")
        self.execute_button.configure(pady="0")
        self.execute_button.configure(text='''Execute''')

        self.cancel_button = tk.Button(top)
        self.cancel_button.place(relx=0.837, rely=0.889, height=24, width=87)
        self.cancel_button.configure(activebackground="#ececec")
        self.cancel_button.configure(activeforeground="#000000")
        self.cancel_button.configure(background="#CED4DA")
        self.cancel_button.configure(disabledforeground="#a3a3a3")
        self.cancel_button.configure(foreground="#000000")
        self.cancel_button.configure(highlightbackground="#d9d9d9")
        self.cancel_button.configure(highlightcolor="black")
        self.cancel_button.configure(pady="0")
        self.cancel_button.configure(text='''Cancel''')

        self.Frame = tk.Frame(top)
        self.Frame.place(relx=0.0, rely=0.178, relheight=0.678, relwidth=1.0)
        self.Frame.configure(relief="groove")
        self.Frame.configure(background="#ffffff")


root = tk.Tk()
top = CustomQuery (root)
root.mainloop()




