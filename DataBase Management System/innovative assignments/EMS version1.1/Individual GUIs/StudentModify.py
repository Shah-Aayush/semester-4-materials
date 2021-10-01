import tkinter as tk


class StudentModify:
    def __init__(self, top=None):
        top.geometry("327x430+589+46")
        top.minsize(120, 1)
        top.maxsize(1370, 749)
        top.resizable(0,0)
        top.title("Modify")
        top.configure(background="#CED4DA")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.245, rely=0.023, height=14, width=154)
        self.Label1.configure(activebackground="#CED4DA")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#CED4DA")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font="-family {Segoe UI} -size 13 -weight bold")
        self.Label1.configure(foreground="#212529")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''PRESENT DATA''')

        self.Label1_1 = tk.Label(top)
        self.Label1_1.place(relx=0.306, rely=0.465, height=14, width=114)
        self.Label1_1.configure(activebackground="#f9f9f9")
        self.Label1_1.configure(activeforeground="black")
        self.Label1_1.configure(background="#CED4DA")
        self.Label1_1.configure(disabledforeground="#a3a3a3")
        self.Label1_1.configure(font="-family {Segoe UI} -size 13 -weight bold")
        self.Label1_1.configure(foreground="#212529")
        self.Label1_1.configure(highlightbackground="#d9d9d9")
        self.Label1_1.configure(highlightcolor="black")
        self.Label1_1.configure(text='''NEW DATA''')

        self.roll_no_label1 = tk.Label(top)
        self.roll_no_label1.place(relx=0.248, rely=0.167, height=12, width=55)
        self.roll_no_label1.configure(activebackground="#f9f9f9")
        self.roll_no_label1.configure(activeforeground="black")
        self.roll_no_label1.configure(background="#CED4DA")
        self.roll_no_label1.configure(disabledforeground="#a3a3a3")
        self.roll_no_label1.configure(foreground="#000000")
        self.roll_no_label1.configure(highlightbackground="#d9d9d9")
        self.roll_no_label1.configure(highlightcolor="black")
        self.roll_no_label1.configure(text='''Roll no. :''')

        self.email_label1 = tk.Label(top)
        self.email_label1.place(relx=0.275, rely=0.24, height=13, width=46)
        self.email_label1.configure(activebackground="#f9f9f9")
        self.email_label1.configure(activeforeground="black")
        self.email_label1.configure(background="#CED4DA")
        self.email_label1.configure(disabledforeground="#a3a3a3")
        self.email_label1.configure(foreground="#000000")
        self.email_label1.configure(highlightbackground="#d9d9d9")
        self.email_label1.configure(highlightcolor="black")
        self.email_label1.configure(text='''Email :''')

        self.student_id_label1 = tk.Label(top)
        self.student_id_label1.place(relx=0.214, rely=0.098, height=14, width=65)

        self.student_id_label1.configure(activebackground="#f9f9f9")
        self.student_id_label1.configure(activeforeground="black")
        self.student_id_label1.configure(background="#CED4DA")
        self.student_id_label1.configure(disabledforeground="#a3a3a3")
        self.student_id_label1.configure(foreground="#000000")
        self.student_id_label1.configure(highlightbackground="#d9d9d9")
        self.student_id_label1.configure(highlightcolor="black")
        self.student_id_label1.configure(text='''Student id :''')

        self.branch_id_label = tk.Label(top)
        self.branch_id_label.place(relx=0.217, rely=0.381, height=13, width=60)
        self.branch_id_label.configure(activebackground="#f9f9f9")
        self.branch_id_label.configure(activeforeground="black")
        self.branch_id_label.configure(background="#CED4DA")
        self.branch_id_label.configure(disabledforeground="#a3a3a3")
        self.branch_id_label.configure(foreground="#000000")
        self.branch_id_label.configure(highlightbackground="#d9d9d9")
        self.branch_id_label.configure(highlightcolor="black")
        self.branch_id_label.configure(text='''Branch id :''')

        self.password_label1 = tk.Label(top)
        self.password_label1.place(relx=0.214, rely=0.312, height=13, width=64)
        self.password_label1.configure(activebackground="#f9f9f9")
        self.password_label1.configure(activeforeground="black")
        self.password_label1.configure(background="#CED4DA")
        self.password_label1.configure(disabledforeground="#a3a3a3")
        self.password_label1.configure(foreground="#000000")
        self.password_label1.configure(highlightbackground="#d9d9d9")
        self.password_label1.configure(highlightcolor="black")
        self.password_label1.configure(text='''Password :''')

        self.student_id_entry1 = tk.Entry(top)
        self.student_id_entry1.place(relx=0.459, rely=0.093, height=20
                , relwidth=0.318)
        self.student_id_entry1.configure(background="white")
        self.student_id_entry1.configure(disabledforeground="#a3a3a3")
        self.student_id_entry1.configure(font="TkFixedFont")
        self.student_id_entry1.configure(foreground="#000000")
        self.student_id_entry1.configure(highlightbackground="#d9d9d9")
        self.student_id_entry1.configure(highlightcolor="black")
        self.student_id_entry1.configure(insertbackground="black")
        self.student_id_entry1.configure(selectbackground="blue")
        self.student_id_entry1.configure(selectforeground="white")

        self.roll_no_entry1 = tk.Entry(top)
        self.roll_no_entry1.place(relx=0.459, rely=0.163, height=20
                , relwidth=0.318)
        self.roll_no_entry1.configure(background="white")
        self.roll_no_entry1.configure(disabledforeground="#a3a3a3")
        self.roll_no_entry1.configure(font="TkFixedFont")
        self.roll_no_entry1.configure(foreground="#000000")
        self.roll_no_entry1.configure(highlightbackground="#d9d9d9")
        self.roll_no_entry1.configure(highlightcolor="black")
        self.roll_no_entry1.configure(insertbackground="black")
        self.roll_no_entry1.configure(selectbackground="blue")
        self.roll_no_entry1.configure(selectforeground="white")

        self.email_entry1 = tk.Entry(top)
        self.email_entry1.place(relx=0.459, rely=0.233, height=20
                , relwidth=0.318)
        self.email_entry1.configure(background="white")
        self.email_entry1.configure(disabledforeground="#a3a3a3")
        self.email_entry1.configure(font="TkFixedFont")
        self.email_entry1.configure(foreground="#000000")
        self.email_entry1.configure(highlightbackground="#d9d9d9")
        self.email_entry1.configure(highlightcolor="black")
        self.email_entry1.configure(insertbackground="black")
        self.email_entry1.configure(selectbackground="blue")
        self.email_entry1.configure(selectforeground="white")

        self.password_entry1 = tk.Entry(top)
        self.password_entry1.place(relx=0.459, rely=0.302, height=20
                , relwidth=0.318)
        self.password_entry1.configure(background="white")
        self.password_entry1.configure(disabledforeground="#a3a3a3")
        self.password_entry1.configure(font="TkFixedFont")
        self.password_entry1.configure(foreground="#000000")
        self.password_entry1.configure(highlightbackground="#d9d9d9")
        self.password_entry1.configure(highlightcolor="black")
        self.password_entry1.configure(insertbackground="black")
        self.password_entry1.configure(selectbackground="blue")
        self.password_entry1.configure(selectforeground="white")

        self.branch_id_entry1 = tk.Entry(top)
        self.branch_id_entry1.place(relx=0.459, rely=0.372, height=20
                , relwidth=0.318)
        self.branch_id_entry1.configure(background="white")
        self.branch_id_entry1.configure(disabledforeground="#a3a3a3")
        self.branch_id_entry1.configure(font="TkFixedFont")
        self.branch_id_entry1.configure(foreground="#000000")
        self.branch_id_entry1.configure(highlightbackground="#d9d9d9")
        self.branch_id_entry1.configure(highlightcolor="black")
        self.branch_id_entry1.configure(insertbackground="black")
        self.branch_id_entry1.configure(selectbackground="blue")
        self.branch_id_entry1.configure(selectforeground="white")

        self.student_id_entry2 = tk.Entry(top)
        self.student_id_entry2.place(relx=0.459, rely=0.535, height=20
                , relwidth=0.318)
        self.student_id_entry2.configure(background="white")
        self.student_id_entry2.configure(disabledforeground="#a3a3a3")
        self.student_id_entry2.configure(font="TkFixedFont")
        self.student_id_entry2.configure(foreground="#000000")
        self.student_id_entry2.configure(highlightbackground="#d9d9d9")
        self.student_id_entry2.configure(highlightcolor="black")
        self.student_id_entry2.configure(insertbackground="black")
        self.student_id_entry2.configure(selectbackground="blue")
        self.student_id_entry2.configure(selectforeground="white")

        self.roll_no_entry2 = tk.Entry(top)
        self.roll_no_entry2.place(relx=0.459, rely=0.605, height=20
                , relwidth=0.318)
        self.roll_no_entry2.configure(background="white")
        self.roll_no_entry2.configure(disabledforeground="#a3a3a3")
        self.roll_no_entry2.configure(font="TkFixedFont")
        self.roll_no_entry2.configure(foreground="#000000")
        self.roll_no_entry2.configure(highlightbackground="#d9d9d9")
        self.roll_no_entry2.configure(highlightcolor="black")
        self.roll_no_entry2.configure(insertbackground="black")
        self.roll_no_entry2.configure(selectbackground="blue")
        self.roll_no_entry2.configure(selectforeground="white")

        self.email_entry2 = tk.Entry(top)
        self.email_entry2.place(relx=0.459, rely=0.674, height=20
                , relwidth=0.318)
        self.email_entry2.configure(background="white")
        self.email_entry2.configure(disabledforeground="#a3a3a3")
        self.email_entry2.configure(font="TkFixedFont")
        self.email_entry2.configure(foreground="#000000")
        self.email_entry2.configure(highlightbackground="#d9d9d9")
        self.email_entry2.configure(highlightcolor="black")
        self.email_entry2.configure(insertbackground="black")
        self.email_entry2.configure(selectbackground="blue")
        self.email_entry2.configure(selectforeground="white")

        self.password_entry2 = tk.Entry(top)
        self.password_entry2.place(relx=0.459, rely=0.744, height=20
                , relwidth=0.318)
        self.password_entry2.configure(background="white")
        self.password_entry2.configure(disabledforeground="#a3a3a3")
        self.password_entry2.configure(font="TkFixedFont")
        self.password_entry2.configure(foreground="#000000")
        self.password_entry2.configure(highlightbackground="#d9d9d9")
        self.password_entry2.configure(highlightcolor="black")
        self.password_entry2.configure(insertbackground="black")
        self.password_entry2.configure(selectbackground="blue")
        self.password_entry2.configure(selectforeground="white")

        self.branch_id_entry2 = tk.Entry(top)
        self.branch_id_entry2.place(relx=0.459, rely=0.814, height=20
                , relwidth=0.318)
        self.branch_id_entry2.configure(background="white")
        self.branch_id_entry2.configure(disabledforeground="#a3a3a3")
        self.branch_id_entry2.configure(font="TkFixedFont")
        self.branch_id_entry2.configure(foreground="#000000")
        self.branch_id_entry2.configure(highlightbackground="#d9d9d9")
        self.branch_id_entry2.configure(highlightcolor="black")
        self.branch_id_entry2.configure(insertbackground="black")
        self.branch_id_entry2.configure(selectbackground="blue")
        self.branch_id_entry2.configure(selectforeground="white")

        self.student_id_label2 = tk.Label(top)
        self.student_id_label2.place(relx=0.214, rely=0.54, height=14, width=65)
        self.student_id_label2.configure(activebackground="#f9f9f9")
        self.student_id_label2.configure(activeforeground="black")
        self.student_id_label2.configure(background="#CED4DA")
        self.student_id_label2.configure(disabledforeground="#a3a3a3")
        self.student_id_label2.configure(foreground="#000000")
        self.student_id_label2.configure(highlightbackground="#d9d9d9")
        self.student_id_label2.configure(highlightcolor="black")
        self.student_id_label2.configure(text='''Student id :''')

        self.roll_no_label2 = tk.Label(top)
        self.roll_no_label2.place(relx=0.251, rely=0.609, height=13, width=56)
        self.roll_no_label2.configure(activebackground="#f9f9f9")
        self.roll_no_label2.configure(activeforeground="black")
        self.roll_no_label2.configure(background="#CED4DA")
        self.roll_no_label2.configure(disabledforeground="#a3a3a3")
        self.roll_no_label2.configure(foreground="#000000")
        self.roll_no_label2.configure(highlightbackground="#d9d9d9")
        self.roll_no_label2.configure(highlightcolor="black")
        self.roll_no_label2.configure(text='''Roll no. :''')

        self.email_label2 = tk.Label(top)
        self.email_label2.place(relx=0.269, rely=0.681, height=12, width=55)
        self.email_label2.configure(activebackground="#f9f9f9")
        self.email_label2.configure(activeforeground="black")
        self.email_label2.configure(background="#CED4DA")
        self.email_label2.configure(disabledforeground="#a3a3a3")
        self.email_label2.configure(foreground="#000000")
        self.email_label2.configure(highlightbackground="#d9d9d9")
        self.email_label2.configure(highlightcolor="black")
        self.email_label2.configure(text='''Email :''')

        self.password_label2 = tk.Label(top)
        self.password_label2.place(relx=0.22, rely=0.753, height=13, width=64)
        self.password_label2.configure(activebackground="#f9f9f9")
        self.password_label2.configure(activeforeground="black")
        self.password_label2.configure(background="#CED4DA")
        self.password_label2.configure(disabledforeground="#a3a3a3")
        self.password_label2.configure(foreground="#000000")
        self.password_label2.configure(highlightbackground="#d9d9d9")
        self.password_label2.configure(highlightcolor="black")
        self.password_label2.configure(text='''Password :''')

        self.branch_id_label2 = tk.Label(top)
        self.branch_id_label2.place(relx=0.211, rely=0.823, height=13, width=70)
        self.branch_id_label2.configure(activebackground="#f9f9f9")
        self.branch_id_label2.configure(activeforeground="black")
        self.branch_id_label2.configure(background="#CED4DA")
        self.branch_id_label2.configure(disabledforeground="#a3a3a3")
        self.branch_id_label2.configure(foreground="#000000")
        self.branch_id_label2.configure(highlightbackground="#d9d9d9")
        self.branch_id_label2.configure(highlightcolor="black")
        self.branch_id_label2.configure(text='''Branch id :''')

        self.modify_button = tk.Button(top)
        self.modify_button.place(relx=0.642, rely=0.907, height=24, width=77)
        self.modify_button.configure(activebackground="#ececec")
        self.modify_button.configure(activeforeground="#000000")
        self.modify_button.configure(background="#E9ECEF")
        self.modify_button.configure(disabledforeground="#a3a3a3")
        self.modify_button.configure(foreground="#000000")
        self.modify_button.configure(highlightbackground="#d9d9d9")
        self.modify_button.configure(highlightcolor="black")
        self.modify_button.configure(pady="0")
        self.modify_button.configure(text='''Modify''')

        self.cancel_button = tk.Button(top)
        self.cancel_button.place(relx=0.153, rely=0.907, height=24, width=77)
        self.cancel_button.configure(activebackground="#ececec")
        self.cancel_button.configure(activeforeground="#000000")
        self.cancel_button.configure(background="#E9ECEF")
        self.cancel_button.configure(disabledforeground="#a3a3a3")
        self.cancel_button.configure(foreground="#000000")
        self.cancel_button.configure(highlightbackground="#d9d9d9")
        self.cancel_button.configure(highlightcolor="black")
        self.cancel_button.configure(pady="0")
        self.cancel_button.configure(text='''Cancel''')


root = tk.Tk()
top = StudentModify (root)
root.mainloop()
