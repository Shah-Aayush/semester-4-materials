import tkinter as tk


class MainScreen:
    def __init__(self, top=None):
        top.geometry("600x450+383+106")
        top.minsize(120, 1)
        top.maxsize(1370, 749)
        top.resizable(1,  1)
        top.title("Exam Management System")
        top.configure(background="#212529")

        self.Canvas = tk.Canvas(top)
        self.Canvas.place(relx=0.117, rely=0.178, relheight=0.607, relwidth=0.772)
        self.Canvas.configure(background="#f8f9fa")
        self.Canvas.configure(insertbackground="black")
        self.Canvas.configure(relief="ridge")
        self.Canvas.configure(selectbackground="blue")
        self.Canvas.configure(selectforeground="white")

        self.student_button = tk.Button(self.Canvas)
        self.student_button.place(relx=0.13, rely=0.33, height=24, width=90)
        self.student_button.configure(activebackground="#ececec")
        self.student_button.configure(activeforeground="#000000")
        self.student_button.configure(background="#3F454C")
        self.student_button.configure(borderwidth="0")
        self.student_button.configure(disabledforeground="#a3a3a3")
        self.student_button.configure(font="-family {Segoe UI} -size 9 -weight bold")
        self.student_button.configure(foreground="#ffffff")
        self.student_button.configure(highlightbackground="#d9d9d9")
        self.student_button.configure(highlightcolor="black")
        self.student_button.configure(pady="0")
        self.student_button.configure(text='''Student''')

        self.exam_button = tk.Button(self.Canvas)
        self.exam_button.place(relx=0.67, rely=0.33, height=24, width=90)
        self.exam_button.configure(activebackground="#ececec")
        self.exam_button.configure(activeforeground="#000000")
        self.exam_button.configure(background="#3F454C")
        self.exam_button.configure(borderwidth="0")
        self.exam_button.configure(disabledforeground="#a3a3a3")
        self.exam_button.configure(font="-family {Segoe UI} -size 9 -weight bold")
        self.exam_button.configure(foreground="white")
        self.exam_button.configure(highlightbackground="#d9d9d9")
        self.exam_button.configure(highlightcolor="black")
        self.exam_button.configure(pady="0")
        self.exam_button.configure(text='''Exam''')

        self.subject_button = tk.Button(self.Canvas)
        self.subject_button.place(relx=0.13, rely=0.513, height=24, width=90)
        self.subject_button.configure(activebackground="#ececec")
        self.subject_button.configure(activeforeground="#000000")
        self.subject_button.configure(background="#3F454C")
        self.subject_button.configure(borderwidth="0")
        self.subject_button.configure(disabledforeground="#a3a3a3")
        self.subject_button.configure(font="-family {Segoe UI} -size 9 -weight bold")
        self.subject_button.configure(foreground="#ffffff")
        self.subject_button.configure(highlightbackground="#d9d9d9")
        self.subject_button.configure(highlightcolor="black")
        self.subject_button.configure(pady="0")
        self.subject_button.configure(text='''Subject''')

        self.result_button = tk.Button(self.Canvas)
        self.result_button.place(relx=0.67, rely=0.513, height=24, width=90)
        self.result_button.configure(activebackground="#ececec")
        self.result_button.configure(activeforeground="#000000")
        self.result_button.configure(background="#3F454C")
        self.result_button.configure(borderwidth="0")
        self.result_button.configure(disabledforeground="#a3a3a3")
        self.result_button.configure(font="-family {Segoe UI} -size 9 -weight bold")
        self.result_button.configure(foreground="white")
        self.result_button.configure(highlightbackground="#d9d9d9")
        self.result_button.configure(highlightcolor="black")
        self.result_button.configure(pady="0")
        self.result_button.configure(text='''Result''')

        self.attendance_button = tk.Button(self.Canvas)
        self.attendance_button.place(relx=0.13, rely=0.696, height=24, width=90)
        self.attendance_button.configure(activebackground="#ececec")
        self.attendance_button.configure(activeforeground="#000000")
        self.attendance_button.configure(background="#3F454C")
        self.attendance_button.configure(borderwidth="0")
        self.attendance_button.configure(disabledforeground="#a3a3a3")
        self.attendance_button.configure(font="-family {Segoe UI} -size 9 -weight bold")
        self.attendance_button.configure(foreground="white")
        self.attendance_button.configure(highlightbackground="#d9d9d9")
        self.attendance_button.configure(highlightcolor="black")
        self.attendance_button.configure(pady="0")
        self.attendance_button.configure(text="Attendance")

        self.branch_button = tk.Button(self.Canvas)
        self.branch_button.place(relx=0.67, rely=0.696, height=24, width=90)
        self.branch_button.configure(activebackground="#ececec")
        self.branch_button.configure(activeforeground="#000000")
        self.branch_button.configure(background="#3F454C")
        self.branch_button.configure(borderwidth="0")
        self.branch_button.configure(disabledforeground="#a3a3a3")
        self.branch_button.configure(font="-family {Segoe UI} -size 9 -weight bold")
        self.branch_button.configure(foreground="white")
        self.branch_button.configure(highlightbackground="#d9d9d9")
        self.branch_button.configure(highlightcolor="black")
        self.branch_button.configure(overrelief="flat")
        self.branch_button.configure(text="Branch")

        self.custom_query_button = tk.Button(self.Canvas)
        self.custom_query_button.place(relx=0.382, rely=0.844, height=24, width=110)
        self.custom_query_button.configure(activebackground="#ececec")
        self.custom_query_button.configure(activeforeground="#000000")
        self.custom_query_button.configure(background="#3F454C")
        self.custom_query_button.configure(font="-family {Segoe UI} -size 9 -weight bold")
        self.custom_query_button.configure(borderwidth="0")
        self.custom_query_button.configure(disabledforeground="#a3a3a3")
        self.custom_query_button.configure(foreground="#ffffff")
        self.custom_query_button.configure(highlightbackground="#d9d9d9")
        self.custom_query_button.configure(highlightcolor="black")
        self.custom_query_button.configure(overrelief="flat")
        self.custom_query_button.configure(text="Custom Query")

        self.Label1 = tk.Label(self.Canvas)
        self.Label1.place(relx=0.216, rely=0.11, height=31, width=264)
        self.Label1.configure(background="#f8f9fa")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font="-family {Segoe UI} -size 14 -weight bold")
        self.Label1.configure(foreground="#212529")
        self.Label1.configure(text="Select a table")


root = tk.Tk()
top = MainScreen(root)
root.mainloop()
