import tkinter as tk


class SubjectAdd:
    def __init__(self, top=None):
        top.geometry("342x200+501+160")
        top.minsize(120, 1)
        top.maxsize(1370, 749)
        top.resizable(1,  1)
        top.title("Add")
        top.configure(background="#CED4DA")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.sub_code_label = tk.Label(top)
        self.sub_code_label.place(relx=0.175, rely=0.12, height=13, width=84)
        self.sub_code_label.configure(activebackground="#f9f9f9")
        self.sub_code_label.configure(activeforeground="black")
        self.sub_code_label.configure(background="#CED4DA")
        self.sub_code_label.configure(disabledforeground="#a3a3a3")
        self.sub_code_label.configure(foreground="#000000")
        self.sub_code_label.configure(highlightbackground="#d9d9d9")
        self.sub_code_label.configure(highlightcolor="black")
        self.sub_code_label.configure(text='''Subject code :''')

        self.sub_name_label = tk.Label(top)
        self.sub_name_label.place(relx=0.158, rely=0.25, height=17, width=94)
        self.sub_name_label.configure(activebackground="#f9f9f9")
        self.sub_name_label.configure(activeforeground="black")
        self.sub_name_label.configure(background="#CED4DA")
        self.sub_name_label.configure(disabledforeground="#a3a3a3")
        self.sub_name_label.configure(foreground="#000000")
        self.sub_name_label.configure(highlightbackground="#d9d9d9")
        self.sub_name_label.configure(highlightcolor="black")
        self.sub_name_label.configure(text='''Subject name :''')

        self.sub_code_entry = tk.Entry(top)
        self.sub_code_entry.place(relx=0.468, rely=0.1, height=20
                , relwidth=0.304)
        self.sub_code_entry.configure(background="white")
        self.sub_code_entry.configure(disabledforeground="#a3a3a3")
        self.sub_code_entry.configure(font="TkFixedFont")
        self.sub_code_entry.configure(foreground="#000000")
        self.sub_code_entry.configure(highlightbackground="#d9d9d9")
        self.sub_code_entry.configure(highlightcolor="black")
        self.sub_code_entry.configure(insertbackground="black")
        self.sub_code_entry.configure(selectbackground="blue")
        self.sub_code_entry.configure(selectforeground="white")

        self.sub_name_entry = tk.Entry(top)
        self.sub_name_entry.place(relx=0.468, rely=0.25, height=20
                , relwidth=0.304)
        self.sub_name_entry.configure(background="white")
        self.sub_name_entry.configure(disabledforeground="#a3a3a3")
        self.sub_name_entry.configure(font="TkFixedFont")
        self.sub_name_entry.configure(foreground="#000000")
        self.sub_name_entry.configure(highlightbackground="#d9d9d9")
        self.sub_name_entry.configure(highlightcolor="black")
        self.sub_name_entry.configure(insertbackground="black")
        self.sub_name_entry.configure(selectbackground="blue")
        self.sub_name_entry.configure(selectforeground="white")

        self.back_button = tk.Button(top)
        self.back_button.place(relx=0.175, rely=0.75, height=24, width=87)
        self.back_button.configure(activebackground="#ececec")
        self.back_button.configure(activeforeground="#000000")
        self.back_button.configure(background="#E9ECEF")
        self.back_button.configure(disabledforeground="#a3a3a3")
        self.back_button.configure(foreground="#000000")
        self.back_button.configure(highlightbackground="#d9d9d9")
        self.back_button.configure(highlightcolor="black")
        self.back_button.configure(pady="0")
        self.back_button.configure(text='''Back''')

        self.add_button = tk.Button(top)
        self.add_button.place(relx=0.585, rely=0.75, height=24, width=87)
        self.add_button.configure(activebackground="#ececec")
        self.add_button.configure(activeforeground="#000000")
        self.add_button.configure(background="#E9ECEF")
        self.add_button.configure(disabledforeground="#a3a3a3")
        self.add_button.configure(foreground="#000000")
        self.add_button.configure(highlightbackground="#d9d9d9")
        self.add_button.configure(highlightcolor="black")
        self.add_button.configure(pady="0")
        self.add_button.configure(text='''Add''')

        self.sub_credit_label = tk.Label(top)
        self.sub_credit_label.place(relx=0.173, rely=0.4, height=17, width=84)
        self.sub_credit_label.configure(activebackground="#f9f9f9")
        self.sub_credit_label.configure(activeforeground="black")
        self.sub_credit_label.configure(background="#CED4DA")
        self.sub_credit_label.configure(disabledforeground="#a3a3a3")
        self.sub_credit_label.configure(foreground="#000000")
        self.sub_credit_label.configure(highlightbackground="#d9d9d9")
        self.sub_credit_label.configure(highlightcolor="black")
        self.sub_credit_label.configure(text='''Subject credit :''')

        self.branch_id_label = tk.Label(top)
        self.branch_id_label.place(relx=0.219, rely=0.55, height=17, width=74)
        self.branch_id_label.configure(activebackground="#f9f9f9")
        self.branch_id_label.configure(activeforeground="black")
        self.branch_id_label.configure(background="#CED4DA")
        self.branch_id_label.configure(disabledforeground="#a3a3a3")
        self.branch_id_label.configure(foreground="#000000")
        self.branch_id_label.configure(highlightbackground="#d9d9d9")
        self.branch_id_label.configure(highlightcolor="black")
        self.branch_id_label.configure(text='''Branch id :''')

        self.sub_credit_entry = tk.Entry(top)
        self.sub_credit_entry.place(relx=0.468, rely=0.4, height=20
                , relwidth=0.304)
        self.sub_credit_entry.configure(background="white")
        self.sub_credit_entry.configure(disabledforeground="#a3a3a3")
        self.sub_credit_entry.configure(font="TkFixedFont")
        self.sub_credit_entry.configure(foreground="#000000")
        self.sub_credit_entry.configure(highlightbackground="#d9d9d9")
        self.sub_credit_entry.configure(highlightcolor="black")
        self.sub_credit_entry.configure(insertbackground="black")
        self.sub_credit_entry.configure(selectbackground="blue")
        self.sub_credit_entry.configure(selectforeground="white")

        self.branch_id_entry = tk.Entry(top)
        self.branch_id_entry.place(relx=0.468, rely=0.55, height=20
                , relwidth=0.304)
        self.branch_id_entry.configure(background="white")
        self.branch_id_entry.configure(disabledforeground="#a3a3a3")
        self.branch_id_entry.configure(font="TkFixedFont")
        self.branch_id_entry.configure(foreground="#000000")
        self.branch_id_entry.configure(highlightbackground="#d9d9d9")
        self.branch_id_entry.configure(highlightcolor="black")
        self.branch_id_entry.configure(insertbackground="black")
        self.branch_id_entry.configure(selectbackground="blue")
        self.branch_id_entry.configure(selectforeground="white")


root = tk.Tk()
top = SubjectAdd (root)
root.mainloop()
