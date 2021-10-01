import tkinter as tk


class AttendanceModify:
    def __init__(self, top=None):
        top.geometry("327x430+455+152")
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

        self.login_label1 = tk.Label(top)
        self.login_label1.place(relx=0.183, rely=0.163, height=22, width=75)
        self.login_label1.configure(activebackground="#f9f9f9")
        self.login_label1.configure(activeforeground="black")
        self.login_label1.configure(background="#CED4DA")
        self.login_label1.configure(disabledforeground="#a3a3a3")
        self.login_label1.configure(foreground="#000000")
        self.login_label1.configure(highlightbackground="#d9d9d9")
        self.login_label1.configure(highlightcolor="black")
        self.login_label1.configure(text='''Login time :''')

        self.logout_label1 = tk.Label(top)
        self.logout_label1.place(relx=0.153, rely=0.233, height=23, width=86)
        self.logout_label1.configure(activebackground="#f9f9f9")
        self.logout_label1.configure(activeforeground="black")
        self.logout_label1.configure(background="#CED4DA")
        self.logout_label1.configure(disabledforeground="#a3a3a3")
        self.logout_label1.configure(foreground="#000000")
        self.logout_label1.configure(highlightbackground="#d9d9d9")
        self.logout_label1.configure(highlightcolor="black")
        self.logout_label1.configure(text='''Logout time :''')

        self.attendance_id_label1 = tk.Label(top)
        self.attendance_id_label1.place(relx=0.144, rely=0.098, height=14
                , width=85)
        self.attendance_id_label1.configure(activebackground="#f9f9f9")
        self.attendance_id_label1.configure(activeforeground="black")
        self.attendance_id_label1.configure(background="#CED4DA")
        self.attendance_id_label1.configure(disabledforeground="#a3a3a3")
        self.attendance_id_label1.configure(foreground="#000000")
        self.attendance_id_label1.configure(highlightbackground="#d9d9d9")
        self.attendance_id_label1.configure(highlightcolor="black")
        self.attendance_id_label1.configure(text='''Attendance id :''')

        self.exam_id_label = tk.Label(top)
        self.exam_id_label.place(relx=0.242, rely=0.381, height=13, width=50)
        self.exam_id_label.configure(activebackground="#f9f9f9")
        self.exam_id_label.configure(activeforeground="black")
        self.exam_id_label.configure(background="#CED4DA")
        self.exam_id_label.configure(disabledforeground="#a3a3a3")
        self.exam_id_label.configure(foreground="#000000")
        self.exam_id_label.configure(highlightbackground="#d9d9d9")
        self.exam_id_label.configure(highlightcolor="black")
        self.exam_id_label.configure(text='''Exam id :''')

        self.student_id_label1 = tk.Label(top)
        self.student_id_label1.place(relx=0.19, rely=0.312, height=13, width=74)
        self.student_id_label1.configure(activebackground="#f9f9f9")
        self.student_id_label1.configure(activeforeground="black")
        self.student_id_label1.configure(background="#CED4DA")
        self.student_id_label1.configure(disabledforeground="#a3a3a3")
        self.student_id_label1.configure(foreground="#000000")
        self.student_id_label1.configure(highlightbackground="#d9d9d9")
        self.student_id_label1.configure(highlightcolor="black")
        self.student_id_label1.configure(text='''Student id :''')

        self.attendance_id_entry1 = tk.Entry(top)
        self.attendance_id_entry1.place(relx=0.459, rely=0.093, height=20
                , relwidth=0.318)
        self.attendance_id_entry1.configure(background="white")
        self.attendance_id_entry1.configure(disabledforeground="#a3a3a3")
        self.attendance_id_entry1.configure(font="TkFixedFont")
        self.attendance_id_entry1.configure(foreground="#000000")
        self.attendance_id_entry1.configure(highlightbackground="#d9d9d9")
        self.attendance_id_entry1.configure(highlightcolor="black")
        self.attendance_id_entry1.configure(insertbackground="black")
        self.attendance_id_entry1.configure(selectbackground="blue")
        self.attendance_id_entry1.configure(selectforeground="white")

        self.login_entry1 = tk.Entry(top)
        self.login_entry1.place(relx=0.459, rely=0.163, height=20
                , relwidth=0.318)
        self.login_entry1.configure(background="white")
        self.login_entry1.configure(disabledforeground="#a3a3a3")
        self.login_entry1.configure(font="TkFixedFont")
        self.login_entry1.configure(foreground="#000000")
        self.login_entry1.configure(highlightbackground="#d9d9d9")
        self.login_entry1.configure(highlightcolor="black")
        self.login_entry1.configure(insertbackground="black")
        self.login_entry1.configure(selectbackground="blue")
        self.login_entry1.configure(selectforeground="white")

        self.logout_entry1 = tk.Entry(top)
        self.logout_entry1.place(relx=0.459, rely=0.233, height=20
                , relwidth=0.318)
        self.logout_entry1.configure(background="white")
        self.logout_entry1.configure(disabledforeground="#a3a3a3")
        self.logout_entry1.configure(font="TkFixedFont")
        self.logout_entry1.configure(foreground="#000000")
        self.logout_entry1.configure(highlightbackground="#d9d9d9")
        self.logout_entry1.configure(highlightcolor="black")
        self.logout_entry1.configure(insertbackground="black")
        self.logout_entry1.configure(selectbackground="blue")
        self.logout_entry1.configure(selectforeground="white")

        self.student_id_entry1 = tk.Entry(top)
        self.student_id_entry1.place(relx=0.459, rely=0.302, height=20
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

        self.exam_id_entry1 = tk.Entry(top)
        self.exam_id_entry1.place(relx=0.459, rely=0.372, height=20
                , relwidth=0.318)
        self.exam_id_entry1.configure(background="white")
        self.exam_id_entry1.configure(disabledforeground="#a3a3a3")
        self.exam_id_entry1.configure(font="TkFixedFont")
        self.exam_id_entry1.configure(foreground="#000000")
        self.exam_id_entry1.configure(highlightbackground="#d9d9d9")
        self.exam_id_entry1.configure(highlightcolor="black")
        self.exam_id_entry1.configure(insertbackground="black")
        self.exam_id_entry1.configure(selectbackground="blue")
        self.exam_id_entry1.configure(selectforeground="white")

        self.attendance_id_entry2 = tk.Entry(top)
        self.attendance_id_entry2.place(relx=0.459, rely=0.535, height=20
                , relwidth=0.318)
        self.attendance_id_entry2.configure(background="white")
        self.attendance_id_entry2.configure(disabledforeground="#a3a3a3")
        self.attendance_id_entry2.configure(font="TkFixedFont")
        self.attendance_id_entry2.configure(foreground="#000000")
        self.attendance_id_entry2.configure(highlightbackground="#d9d9d9")
        self.attendance_id_entry2.configure(highlightcolor="black")
        self.attendance_id_entry2.configure(insertbackground="black")
        self.attendance_id_entry2.configure(selectbackground="blue")
        self.attendance_id_entry2.configure(selectforeground="white")

        self.login_entry2 = tk.Entry(top)
        self.login_entry2.place(relx=0.459, rely=0.605, height=20
                , relwidth=0.318)
        self.login_entry2.configure(background="white")
        self.login_entry2.configure(disabledforeground="#a3a3a3")
        self.login_entry2.configure(font="TkFixedFont")
        self.login_entry2.configure(foreground="#000000")
        self.login_entry2.configure(highlightbackground="#d9d9d9")
        self.login_entry2.configure(highlightcolor="black")
        self.login_entry2.configure(insertbackground="black")
        self.login_entry2.configure(selectbackground="blue")
        self.login_entry2.configure(selectforeground="white")

        self.logout_entry2 = tk.Entry(top)
        self.logout_entry2.place(relx=0.459, rely=0.674, height=20
                , relwidth=0.318)
        self.logout_entry2.configure(background="white")
        self.logout_entry2.configure(disabledforeground="#a3a3a3")
        self.logout_entry2.configure(font="TkFixedFont")
        self.logout_entry2.configure(foreground="#000000")
        self.logout_entry2.configure(highlightbackground="#d9d9d9")
        self.logout_entry2.configure(highlightcolor="black")
        self.logout_entry2.configure(insertbackground="black")
        self.logout_entry2.configure(selectbackground="blue")
        self.logout_entry2.configure(selectforeground="white")

        self.student_id_entry2 = tk.Entry(top)
        self.student_id_entry2.place(relx=0.459, rely=0.744, height=20
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

        self.exam_id_entry2 = tk.Entry(top)
        self.exam_id_entry2.place(relx=0.459, rely=0.814, height=20
                , relwidth=0.318)
        self.exam_id_entry2.configure(background="white")
        self.exam_id_entry2.configure(disabledforeground="#a3a3a3")
        self.exam_id_entry2.configure(font="TkFixedFont")
        self.exam_id_entry2.configure(foreground="#000000")
        self.exam_id_entry2.configure(highlightbackground="#d9d9d9")
        self.exam_id_entry2.configure(highlightcolor="black")
        self.exam_id_entry2.configure(insertbackground="black")
        self.exam_id_entry2.configure(selectbackground="blue")
        self.exam_id_entry2.configure(selectforeground="white")

        self.attendance_id_label2 = tk.Label(top)
        self.attendance_id_label2.place(relx=0.153, rely=0.54, height=14
                , width=85)
        self.attendance_id_label2.configure(activebackground="#f9f9f9")
        self.attendance_id_label2.configure(activeforeground="black")
        self.attendance_id_label2.configure(background="#CED4DA")
        self.attendance_id_label2.configure(disabledforeground="#a3a3a3")
        self.attendance_id_label2.configure(foreground="#000000")
        self.attendance_id_label2.configure(highlightbackground="#d9d9d9")
        self.attendance_id_label2.configure(highlightcolor="black")
        self.attendance_id_label2.configure(text='''Attendance id :''')

        self.login_label2 = tk.Label(top)
        self.login_label2.place(relx=0.183, rely=0.6, height=23, width=76)
        self.login_label2.configure(activebackground="#f9f9f9")
        self.login_label2.configure(activeforeground="black")
        self.login_label2.configure(background="#CED4DA")
        self.login_label2.configure(disabledforeground="#a3a3a3")
        self.login_label2.configure(foreground="#000000")
        self.login_label2.configure(highlightbackground="#d9d9d9")
        self.login_label2.configure(highlightcolor="black")
        self.login_label2.configure(text='''Login time :''')

        self.logout_label2 = tk.Label(top)
        self.logout_label2.place(relx=0.147, rely=0.674, height=22, width=95)
        self.logout_label2.configure(activebackground="#f9f9f9")
        self.logout_label2.configure(activeforeground="black")
        self.logout_label2.configure(background="#CED4DA")
        self.logout_label2.configure(disabledforeground="#a3a3a3")
        self.logout_label2.configure(foreground="#000000")
        self.logout_label2.configure(highlightbackground="#d9d9d9")
        self.logout_label2.configure(highlightcolor="black")
        self.logout_label2.configure(text='''Logout time :''')

        self.student_id_label2 = tk.Label(top)
        self.student_id_label2.place(relx=0.214, rely=0.753, height=13, width=64)

        self.student_id_label2.configure(activebackground="#f9f9f9")
        self.student_id_label2.configure(activeforeground="black")
        self.student_id_label2.configure(background="#CED4DA")
        self.student_id_label2.configure(disabledforeground="#a3a3a3")
        self.student_id_label2.configure(foreground="#000000")
        self.student_id_label2.configure(highlightbackground="#d9d9d9")
        self.student_id_label2.configure(highlightcolor="black")
        self.student_id_label2.configure(text='''Student id :''')

        self.exam_id_label2 = tk.Label(top)
        self.exam_id_label2.place(relx=0.214, rely=0.819, height=13, width=70)
        self.exam_id_label2.configure(activebackground="#f9f9f9")
        self.exam_id_label2.configure(activeforeground="black")
        self.exam_id_label2.configure(background="#CED4DA")
        self.exam_id_label2.configure(disabledforeground="#a3a3a3")
        self.exam_id_label2.configure(foreground="#000000")
        self.exam_id_label2.configure(highlightbackground="#d9d9d9")
        self.exam_id_label2.configure(highlightcolor="black")
        self.exam_id_label2.configure(text='''Exam id :''')

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
top = AttendanceModify (root)
root.mainloop()