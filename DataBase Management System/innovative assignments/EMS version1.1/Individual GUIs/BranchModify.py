import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True


class BranchModify:
    def __init__(self, top=None):

        top.geometry("327x253+556+102")
        top.minsize(120, 1)
        top.maxsize(1370, 749)
        top.resizable(0,0)
        top.title("Modify")
        top.configure(background="#CED4DA")

        self.menubar = tk.Menu(top,font="TkMenuFont",bg="#d9d9d9",fg="#000000")

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.275, rely=0.036, height=24, width=149)
        self.Label1.configure(background="#CED4DA")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font="-family {Segoe UI} -size 13 -weight bold")
        self.Label1.configure(foreground="#212529")
        self.Label1.configure(text='''PRESENT DATA''')

        self.Label2 = tk.Label(top)
        self.Label2.place(relx=0.214, rely=0.158, height=16, width=74)
        self.Label2.configure(background="#CED4DA")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''Branch id :''')

        self.Entry1 = tk.Entry(top)
        self.Entry1.place(relx=0.459, rely=0.158, height=20, relwidth=0.318)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")

        self.Label3 = tk.Label(top)
        self.Label3.place(relx=0.183, rely=0.277, height=16, width=74)
        self.Label3.configure(background="#CED4DA")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(text='''Branch name :''')

        self.Entry2 = tk.Entry(top)
        self.Entry2.place(relx=0.459, rely=0.277, height=20, relwidth=0.318)
        self.Entry2.configure(background="white")
        self.Entry2.configure(disabledforeground="#a3a3a3")
        self.Entry2.configure(font="TkFixedFont")
        self.Entry2.configure(foreground="#000000")
        self.Entry2.configure(insertbackground="black")

        self.Label4 = tk.Label(top)
        self.Label4.place(relx=0.336, rely=0.407, height=27, width=105)
        self.Label4.configure(background="#CED4DA")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(font="-family {Segoe UI} -size 13 -weight bold")
        self.Label4.configure(foreground="#212529")
        self.Label4.configure(text='''NEW DATA''')

        self.Label5 = tk.Label(top)
        self.Label5.place(relx=0.141, rely=0.672, height=17, width=94)
        self.Label5.configure(background="#CED4DA")
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(foreground="#000000")
        self.Label5.configure(text='''Branch name :''')

        self.Label6 = tk.Label(top)
        self.Label6.place(relx=0.22, rely=0.553, height=17, width=62)
        self.Label6.configure(background="#CED4DA")
        self.Label6.configure(disabledforeground="#a3a3a3")
        self.Label6.configure(foreground="#000000")
        self.Label6.configure(text='''Branch id :''')

        self.back_button = tk.Button(top)
        self.back_button.place(relx=0.153, rely=0.83, height=24, width=77)
        self.back_button.configure(activebackground="#ececec")
        self.back_button.configure(activeforeground="#000000")
        self.back_button.configure(background="#E9ECEF")
        self.back_button.configure(disabledforeground="#a3a3a3")
        self.back_button.configure(foreground="#000000")
        self.back_button.configure(highlightbackground="#d9d9d9")
        self.back_button.configure(highlightcolor="black")
        self.back_button.configure(pady="0")
        self.back_button.configure(text='''Back''')

        self.modify_button = tk.Button(top)
        self.modify_button.place(relx=0.612, rely=0.83, height=24, width=77)
        self.modify_button.configure(activebackground="#ececec")
        self.modify_button.configure(activeforeground="#000000")
        self.modify_button.configure(background="#E9ECEF")
        self.modify_button.configure(disabledforeground="#a3a3a3")
        self.modify_button.configure(foreground="#000000")
        self.modify_button.configure(highlightbackground="#d9d9d9")
        self.modify_button.configure(highlightcolor="black")
        self.modify_button.configure(pady="0")
        self.modify_button.configure(text='''Modify''')

        self.Entry1_1 = tk.Entry(top)
        self.Entry1_1.place(relx=0.459, rely=0.553, height=20, relwidth=0.318)
        self.Entry1_1.configure(background="white")
        self.Entry1_1.configure(cursor="fleur")
        self.Entry1_1.configure(disabledforeground="#a3a3a3")
        self.Entry1_1.configure(font="TkFixedFont")
        self.Entry1_1.configure(foreground="#000000")
        self.Entry1_1.configure(highlightbackground="#d9d9d9")
        self.Entry1_1.configure(highlightcolor="black")
        self.Entry1_1.configure(insertbackground="black")
        self.Entry1_1.configure(selectbackground="blue")
        self.Entry1_1.configure(selectforeground="white")

        self.Entry1_2 = tk.Entry(top)
        self.Entry1_2.place(relx=0.459, rely=0.672, height=20, relwidth=0.318)
        self.Entry1_2.configure(background="white")
        self.Entry1_2.configure(disabledforeground="#a3a3a3")
        self.Entry1_2.configure(font="TkFixedFont")
        self.Entry1_2.configure(foreground="#000000")
        self.Entry1_2.configure(highlightbackground="#d9d9d9")
        self.Entry1_2.configure(highlightcolor="black")
        self.Entry1_2.configure(insertbackground="black")
        self.Entry1_2.configure(selectbackground="blue")
        self.Entry1_2.configure(selectforeground="white")

root = tk.Tk()
top = BranchModify(root)
root.mainloop()
