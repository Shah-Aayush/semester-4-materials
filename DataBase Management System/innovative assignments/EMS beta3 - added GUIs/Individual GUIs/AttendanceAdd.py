import tkinter as tk


class AttendanceAdd:
    def __init__(self, top=None):
        top.geometry("342x224+434+151")
        top.minsize(120, 1)
        top.maxsize(1370, 749)
        top.resizable(1,  1)
        top.title("Add")
        top.configure(background="#CED4DA")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.att_id_label = tk.Label(top)
        self.att_id_label.place(relx=0.152, rely=0.089, height=15, width=94)
        self.att_id_label.configure(activebackground="#f9f9f9")
        self.att_id_label.configure(activeforeground="black")
        self.att_id_label.configure(background="#CED4DA")
        self.att_id_label.configure(disabledforeground="#a3a3a3")
        self.att_id_label.configure(foreground="#000000")
        self.att_id_label.configure(highlightbackground="#d9d9d9")
        self.att_id_label.configure(highlightcolor="black")
        self.att_id_label.configure(text='''Attendance id :''')

        self.login_label = tk.Label(top)
        self.login_label.place(relx=0.205, rely=0.223, height=19, width=74)
        self.login_label.configure(activebackground="#f9f9f9")
        self.login_label.configure(activeforeground="black")
        self.login_label.configure(background="#CED4DA")
        self.login_label.configure(disabledforeground="#a3a3a3")
        self.login_label.configure(foreground="#000000")
        self.login_label.configure(highlightbackground="#d9d9d9")
        self.login_label.configure(highlightcolor="black")
        self.login_label.configure(text='''Login time :''')

        self.att_id_entry = tk.Entry(top)
        self.att_id_entry.place(relx=0.468, rely=0.089, height=20
                , relwidth=0.304)
        self.att_id_entry.configure(background="white")
        self.att_id_entry.configure(disabledforeground="#a3a3a3")
        self.att_id_entry.configure(font="TkFixedFont")
        self.att_id_entry.configure(foreground="#000000")
        self.att_id_entry.configure(highlightbackground="#d9d9d9")
        self.att_id_entry.configure(highlightcolor="black")
        self.att_id_entry.configure(insertbackground="black")
        self.att_id_entry.configure(selectbackground="blue")
        self.att_id_entry.configure(selectforeground="white")

        self.login_entry = tk.Entry(top)
        self.login_entry.place(relx=0.468, rely=0.223, height=20, relwidth=0.304)

        self.login_entry.configure(background="white")
        self.login_entry.configure(disabledforeground="#a3a3a3")
        self.login_entry.configure(font="TkFixedFont")
        self.login_entry.configure(foreground="#000000")
        self.login_entry.configure(highlightbackground="#d9d9d9")
        self.login_entry.configure(highlightcolor="black")
        self.login_entry.configure(insertbackground="black")
        self.login_entry.configure(selectbackground="blue")
        self.login_entry.configure(selectforeground="white")

        self.back_button = tk.Button(top)
        self.back_button.place(relx=0.175, rely=0.804, height=24, width=87)
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
        self.add_button.place(relx=0.585, rely=0.804, height=24, width=87)
        self.add_button.configure(activebackground="#ececec")
        self.add_button.configure(activeforeground="#000000")
        self.add_button.configure(background="#E9ECEF")
        self.add_button.configure(disabledforeground="#a3a3a3")
        self.add_button.configure(foreground="#000000")
        self.add_button.configure(highlightbackground="#d9d9d9")
        self.add_button.configure(highlightcolor="black")
        self.add_button.configure(pady="0")
        self.add_button.configure(text='''Add''')

        self.logout_label = tk.Label(top)
        self.logout_label.place(relx=0.175, rely=0.357, height=19, width=84)
        self.logout_label.configure(activebackground="#f9f9f9")
        self.logout_label.configure(activeforeground="black")
        self.logout_label.configure(background="#CED4DA")
        self.logout_label.configure(disabledforeground="#a3a3a3")
        self.logout_label.configure(foreground="#000000")
        self.logout_label.configure(highlightbackground="#d9d9d9")
        self.logout_label.configure(highlightcolor="black")
        self.logout_label.configure(text='''Logout time :''')

        self.student_id_label = tk.Label(top)
        self.student_id_label.place(relx=0.205, rely=0.491, height=19, width=74)
        self.student_id_label.configure(activebackground="#f9f9f9")
        self.student_id_label.configure(activeforeground="black")
        self.student_id_label.configure(background="#CED4DA")
        self.student_id_label.configure(disabledforeground="#a3a3a3")
        self.student_id_label.configure(foreground="#000000")
        self.student_id_label.configure(highlightbackground="#d9d9d9")
        self.student_id_label.configure(highlightcolor="black")
        self.student_id_label.configure(text='''Student id :''')

        self.exam_id_label = tk.Label(top)
        self.exam_id_label.place(relx=0.219, rely=0.625, height=21, width=74)
        self.exam_id_label.configure(activebackground="#f9f9f9")
        self.exam_id_label.configure(activeforeground="black")
        self.exam_id_label.configure(background="#CED4DA")
        self.exam_id_label.configure(disabledforeground="#a3a3a3")
        self.exam_id_label.configure(foreground="#000000")
        self.exam_id_label.configure(highlightbackground="#d9d9d9")
        self.exam_id_label.configure(highlightcolor="black")
        self.exam_id_label.configure(text='''Exam id :''')

        self.logout_entry = tk.Entry(top)
        self.logout_entry.place(relx=0.468, rely=0.357, height=20
                , relwidth=0.304)
        self.logout_entry.configure(background="white")
        self.logout_entry.configure(disabledforeground="#a3a3a3")
        self.logout_entry.configure(font="TkFixedFont")
        self.logout_entry.configure(foreground="#000000")
        self.logout_entry.configure(highlightbackground="#d9d9d9")
        self.logout_entry.configure(highlightcolor="black")
        self.logout_entry.configure(insertbackground="black")
        self.logout_entry.configure(selectbackground="blue")
        self.logout_entry.configure(selectforeground="white")

        self.student_id_entry = tk.Entry(top)
        self.student_id_entry.place(relx=0.468, rely=0.491, height=20
                , relwidth=0.304)
        self.student_id_entry.configure(background="white")
        self.student_id_entry.configure(disabledforeground="#a3a3a3")
        self.student_id_entry.configure(font="TkFixedFont")
        self.student_id_entry.configure(foreground="#000000")
        self.student_id_entry.configure(highlightbackground="#d9d9d9")
        self.student_id_entry.configure(highlightcolor="black")
        self.student_id_entry.configure(insertbackground="black")
        self.student_id_entry.configure(selectbackground="blue")
        self.student_id_entry.configure(selectforeground="white")

        self.exam_id_entry = tk.Entry(top)
        self.exam_id_entry.place(relx=0.468, rely=0.625, height=20
                , relwidth=0.304)
        self.exam_id_entry.configure(background="white")
        self.exam_id_entry.configure(disabledforeground="#a3a3a3")
        self.exam_id_entry.configure(font="TkFixedFont")
        self.exam_id_entry.configure(foreground="#000000")
        self.exam_id_entry.configure(highlightbackground="#d9d9d9")
        self.exam_id_entry.configure(highlightcolor="black")
        self.exam_id_entry.configure(insertbackground="black")
        self.exam_id_entry.configure(selectbackground="blue")
        self.exam_id_entry.configure(selectforeground="white")


root = tk.Tk()
top = AttendanceAdd (root)
root.mainloop()