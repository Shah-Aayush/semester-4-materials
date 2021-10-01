import sys
import tkinter as tk
from tkinter import *
import mysql.connector
import platform
from tkinter import messagebox
from prettytable import PrettyTable

mydb = mysql.connector.connect(host="localhost", user="root", passwd="123password", database="innovative_assignment")
mycursor = mydb.cursor()

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

    # python backend starts


def display_table(choice):  # 1=student; 2=exam; 3=subject; 4=result; 5=attendance; 6=branch
    if choice == 1:
        mycursor.execute("select * from student")
        data = mycursor.fetchall()
        return data
    elif choice == 2:
        mycursor.execute("select * from exam")
        data = mycursor.fetchall()
        return data
    elif choice == 3:
        mycursor.execute("select * from subject")
        data = mycursor.fetchall()
        return data
    elif choice == 4:
        mycursor.execute("select * from result")
        data = mycursor.fetchall()
        return data
    elif choice == 5:
        mycursor.execute("select * from attendance")
        data = mycursor.fetchall()
        return data
    elif choice == 6:
        mycursor.execute("select * from branch")  # Error.setMessage(self, message_shown="Cannot fetch data!")

        data = mycursor.fetchall()
        return data
    else:
        #        Error(Toplevel(self.master))
        return "Cannot fetch data!"

    # python backend ends

    # Tkinter GUI code starts


class Student:
    def __init__(self, top=None):
        self.master = top
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.', background='#d9d9d9')
        self.style.configure('.', foreground="#000000")
        self.style.configure('.', font="TkDefaultFont")
        self.style.map('.', background=
        [('selected', "#d9d9d9"), ('active', "#ececec")])

        top.geometry("600x450+383+106")
        top.minsize(120, 1)
        top.maxsize(1370, 749)
        top.resizable(0, 0)
        top.title("Student")
        top.configure(background="#212529")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.Canvas1 = tk.Canvas(top)
        self.Canvas1.place(relx=0.067, rely=0.111, relheight=0.74
                           , relwidth=0.872)
        self.Canvas1.configure(background="white")
        self.Canvas1.configure(insertbackground="black", highlightbackground="#d9d9d9", highlightcolor="black")
        self.Canvas1.configure(relief="ridge")
        self.Canvas1.configure(selectbackground="blue")
        self.Canvas1.configure(selectforeground="white")

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.367, rely=0.022, height=31, width=174)
        self.Label1.configure(background="#212529", font="-family {Segoe UI} -size 13 -weight bold",
                              foreground="#ffffff", text='''Student Table''')

        self.style.configure('Treeview', font="TkDefaultFont", borderwidth=0)
        global tv
        tv = ScrolledTreeView(self.Canvas1)
        tv.place(relx=0.0, rely=0.0, relheight=0.712, relwidth=1.0)
        tv['columns'] = ("Col1", "Col2", "Col3")
        tv.column("#0", width=50)
        tv.column("Col1", width=100)
        tv.column("Col2", width=100, anchor="center")
        tv.column("Col3", width=100)
        tv.heading("#0", text="Phantom", anchor="w")
        tv.heading("Col1", text="Column1", anchor="w")
        tv.heading("Col2", text="Column2", anchor="center")
        tv.heading("Col3", text="Column3", anchor="w")
        count = 0
        for i in range(20):
            tv.insert(parent='', index="end", iid=count, text="Parent" + str(count),
                           values=("Col1" + str(count), "Col2" + str(count), "Col3" + str(count)))
            count += 1

        self.add_button = tk.Button(self.Canvas1, command=self.select_add)
        self.add_button.place(relx=0.402, rely=0.871, height=24, width=79)
        self.add_button.configure(activebackground="#ececec", activeforeground="#000000", background="#3F454C",
                                  borderwidth="0", disabledforeground="#a3a3a3", font="-family {Segoe UI} -size 9 "
                                                                                      "-weight bold",
                                  foreground="white", highlightbackground="#d9d9d9", highlightcolor="black",
                                  pady="0", text='''Add''')

        self.delete_button = tk.Button(self.Canvas1, command=self.select_delete)
        self.delete_button.place(relx=0.593, rely=0.871, height=24, width=79)
        self.delete_button.configure(activebackground="#ececec", activeforeground="#000000", background="#3F454C",
                                     borderwidth="0", disabledforeground="#a3a3a3", font="-family {Segoe UI} -size 9 "
                                                                                         "-weight bold",
                                     foreground="white", highlightbackground="#d9d9d9", highlightcolor="black",
                                     text="Delete")

        self.modify_button = tk.Button(self.Canvas1, command=self.select_modify)
        self.modify_button.place(relx=0.784, rely=0.871, height=24, width=79)
        self.modify_button.configure(activebackground="#ececec", activeforeground="#000000", background="#3F454C",
                                     borderwidth="0", disabledforeground="#a3a3a3",
                                     font="-family {Segoe UI} -size 9 -weight bold",
                                     foreground="white", highlightbackground="#d9d9d9", highlightcolor="black",
                                     text='''Modify''')

        self.back_button = tk.Button(self.Canvas1, command=self.select_back)
        self.back_button.place(relx=0.038, rely=0.871, height=24, width=79)
        self.back_button.configure(activebackground="#ececec", activeforeground="#000000", background="#343a40",
                                   borderwidth="0", disabledforeground="#a3a3a3",
                                   font="-family {Segoe UI} -size 9 -weight bold", foreground="#ffffff",
                                   highlightbackground="#d9d9d9", highlightcolor="black", pady="0", text='''Back''')

    def select_back(self):
        self.master.withdraw()
        MainScreen(Toplevel(self.master))
        
    def select_delete(self):
        MainScreen(Toplevel(self.master))
        
    def select_add(self):
        StudentAdd(Toplevel(self.master))
        
    def select_modify(self):
        StudentModify(Toplevel(self.master))


class Exam:
    def __init__(self, top=None):
        self.master = top
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.', background='#d9d9d9')
        self.style.configure('.', foreground="#000000")
        self.style.configure('.', font="TkDefaultFont")
        self.style.map('.', background=
        [('selected', "#d9d9d9"), ('active', "#ececec")])

        top.geometry("600x450+383+106")
        top.minsize(120, 1)
        top.maxsize(1370, 749)
        top.resizable(0, 0)
        top.title("Eaxm ")
        top.configure(background="#212529")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.Canvas1 = tk.Canvas(top)
        self.Canvas1.place(relx=0.067, rely=0.111, relheight=0.74
                           , relwidth=0.872)
        self.Canvas1.configure(background="white")
        self.Canvas1.configure(insertbackground="black", highlightbackground="#d9d9d9", highlightcolor="black")
        self.Canvas1.configure(relief="ridge")
        self.Canvas1.configure(selectbackground="blue")
        self.Canvas1.configure(selectforeground="white")

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.367, rely=0.022, height=31, width=174)
        self.Label1.configure(background="#212529", font="-family {Segoe UI} -size 13 -weight bold",
                              foreground="#ffffff", text='''Eaxm Table''')

        self.style.configure('Treeview', font="TkDefaultFont", borderwidth=0)
        self.tv = ScrolledTreeView(self.Canvas1)
        self.tv.place(relx=0.0, rely=0.0, relheight=0.712, relwidth=1.0)
        self.tv['columns'] = ("Col1", "Col2", "Col3")
        self.tv.column("#0", width=50)
        self.tv.column("Col1", width=100)
        self.tv.column("Col2", width=100, anchor="center")
        self.tv.column("Col3", width=100)
        self.tv.heading("#0", text="Phantom", anchor="w")
        self.tv.heading("Col1", text="Column1", anchor="w")
        self.tv.heading("Col2", text="Column2", anchor="center")
        self.tv.heading("Col3", text="Column3", anchor="w")
        # count = 0
        # for i in range(20):
        #     self.tv.insert(parent='', index="end", iid=count, text="Parent" + str(count),
        #                    values=("Col1" + str(count), "Col2" + str(count), "Col3" + str(count)))
        #     count += 1

        self.add_button = tk.Button(self.Canvas1)
        self.add_button.place(relx=0.402, rely=0.871, height=24, width=79)
        self.add_button.configure(activebackground="#ececec", activeforeground="#000000", background="#3F454C",
                                  borderwidth="0", disabledforeground="#a3a3a3", font="-family {Segoe UI} -size 9 "
                                                                                      "-weight bold",
                                  foreground="white", highlightbackground="#d9d9d9", highlightcolor="black",
                                  pady="0", text='''Add''')

        self.delete_button = tk.Button(self.Canvas1)
        self.delete_button.place(relx=0.593, rely=0.871, height=24, width=79)
        self.delete_button.configure(activebackground="#ececec", activeforeground="#000000", background="#3F454C",
                                     borderwidth="0", disabledforeground="#a3a3a3", font="-family {Segoe UI} -size 9 "
                                                                                         "-weight bold",
                                     foreground="white", highlightbackground="#d9d9d9", highlightcolor="black",
                                     text="Delete")

        self.modify_button = tk.Button(self.Canvas1)
        self.modify_button.place(relx=0.784, rely=0.871, height=24, width=79)
        self.modify_button.configure(activebackground="#ececec", activeforeground="#000000", background="#3F454C",
                                     borderwidth="0", disabledforeground="#a3a3a3",
                                     font="-family {Segoe UI} -size 9 -weight bold",
                                     foreground="white", highlightbackground="#d9d9d9", highlightcolor="black",
                                     text='''Modify''')

        self.back_button = tk.Button(self.Canvas1)
        self.back_button.place(relx=0.038, rely=0.871, height=24, width=79)
        self.back_button.configure(activebackground="#ececec", activeforeground="#000000", background="#343a40",
                                   borderwidth="0", disabledforeground="#a3a3a3",
                                   font="-family {Segoe UI} -size 9 -weight bold", foreground="#ffffff",
                                   highlightbackground="#d9d9d9", highlightcolor="black", pady="0", text='''Back''',
                                   command=self.back)

    def back(self):
        self.master.withdraw()
        MainScreen(Toplevel(self.master))


class Result:
    def __init__(self, top=None):
        self.master = top
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.', background='#d9d9d9')
        self.style.configure('.', foreground="#000000")
        self.style.configure('.', font="TkDefaultFont")
        self.style.map('.', background=
        [('selected', "#d9d9d9"), ('active', "#ececec")])

        top.geometry("600x450+383+106")
        top.minsize(120, 1)
        top.maxsize(1370, 749)
        top.resizable(0, 0)
        top.title("Result ")
        top.configure(background="#212529")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.Canvas1 = tk.Canvas(top)
        self.Canvas1.place(relx=0.067, rely=0.111, relheight=0.74
                           , relwidth=0.872)
        self.Canvas1.configure(background="white")
        self.Canvas1.configure(insertbackground="black", highlightbackground="#d9d9d9", highlightcolor="black")
        self.Canvas1.configure(relief="ridge")
        self.Canvas1.configure(selectbackground="blue")
        self.Canvas1.configure(selectforeground="white")

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.367, rely=0.022, height=31, width=174)
        self.Label1.configure(background="#212529", font="-family {Segoe UI} -size 13 -weight bold",
                              foreground="#ffffff", text='''Result Table''')

        self.style.configure('Treeview', font="TkDefaultFont", borderwidth=0)
        self.tv = ScrolledTreeView(self.Canvas1)
        self.tv.place(relx=0.0, rely=0.0, relheight=0.712, relwidth=1.0)
        self.tv['columns'] = ("Col1", "Col2", "Col3")
        self.tv.column("#0", width=50)
        self.tv.column("Col1", width=100)
        self.tv.column("Col2", width=100, anchor="center")
        self.tv.column("Col3", width=100)
        self.tv.heading("#0", text="Phantom", anchor="w")
        self.tv.heading("Col1", text="Column1", anchor="w")
        self.tv.heading("Col2", text="Column2", anchor="center")
        self.tv.heading("Col3", text="Column3", anchor="w")
        # count = 0
        # for i in range(20):
        #     self.tv.insert(parent='', index="end", iid=count, text="Parent" + str(count),
        #                    values=("Col1" + str(count), "Col2" + str(count), "Col3" + str(count)))
        #     count += 1

        self.add_button = tk.Button(self.Canvas1)
        self.add_button.place(relx=0.402, rely=0.871, height=24, width=79)
        self.add_button.configure(activebackground="#ececec", activeforeground="#000000", background="#3F454C",
                                  borderwidth="0", disabledforeground="#a3a3a3", font="-family {Segoe UI} -size 9 "
                                                                                      "-weight bold",
                                  foreground="white", highlightbackground="#d9d9d9", highlightcolor="black",
                                  pady="0", text='''Add''')

        self.delete_button = tk.Button(self.Canvas1)
        self.delete_button.place(relx=0.593, rely=0.871, height=24, width=79)
        self.delete_button.configure(activebackground="#ececec", activeforeground="#000000", background="#3F454C",
                                     borderwidth="0", disabledforeground="#a3a3a3", font="-family {Segoe UI} -size 9 "
                                                                                         "-weight bold",
                                     foreground="white", highlightbackground="#d9d9d9", highlightcolor="black",
                                     text="Delete")

        self.modify_button = tk.Button(self.Canvas1)
        self.modify_button.place(relx=0.784, rely=0.871, height=24, width=79)
        self.modify_button.configure(activebackground="#ececec", activeforeground="#000000", background="#3F454C",
                                     borderwidth="0", disabledforeground="#a3a3a3",
                                     font="-family {Segoe UI} -size 9 -weight bold",
                                     foreground="white", highlightbackground="#d9d9d9", highlightcolor="black",
                                     text='''Modify''')

        self.back_button = tk.Button(self.Canvas1)
        self.back_button.place(relx=0.038, rely=0.871, height=24, width=79)
        self.back_button.configure(activebackground="#ececec", activeforeground="#000000", background="#343a40",
                                   borderwidth="0", disabledforeground="#a3a3a3",
                                   font="-family {Segoe UI} -size 9 -weight bold", foreground="#ffffff",
                                   highlightbackground="#d9d9d9", highlightcolor="black", pady="0", text='''Back''',
                                   command=self.back)

    def back(self):
        self.master.withdraw()
        MainScreen(Toplevel(self.master))


class Subject:
    def __init__(self, top=None):
        self.master = top
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.', background='#d9d9d9')
        self.style.configure('.', foreground="#000000")
        self.style.configure('.', font="TkDefaultFont")
        self.style.map('.', background=
        [('selected', "#d9d9d9"), ('active', "#ececec")])

        top.geometry("600x450+383+106")
        top.minsize(120, 1)
        top.maxsize(1370, 749)
        top.resizable(0, 0)
        top.title("Subject ")
        top.configure(background="#212529")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.Canvas1 = tk.Canvas(top)
        self.Canvas1.place(relx=0.067, rely=0.111, relheight=0.74
                           , relwidth=0.872)
        self.Canvas1.configure(background="white")
        self.Canvas1.configure(insertbackground="black", highlightbackground="#d9d9d9", highlightcolor="black")
        self.Canvas1.configure(relief="ridge")
        self.Canvas1.configure(selectbackground="blue")
        self.Canvas1.configure(selectforeground="white")

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.367, rely=0.022, height=31, width=174)
        self.Label1.configure(background="#212529", font="-family {Segoe UI} -size 13 -weight bold",
                              foreground="#ffffff", text='''Subject Table''')

        self.style.configure('Treeview', font="TkDefaultFont", borderwidth=0)
        self.tv = ScrolledTreeView(self.Canvas1)
        self.tv.place(relx=0.0, rely=0.0, relheight=0.712, relwidth=1.0)
        self.tv['columns'] = ("Col1", "Col2", "Col3")
        self.tv.column("#0", width=50)
        self.tv.column("Col1", width=100)
        self.tv.column("Col2", width=100, anchor="center")
        self.tv.column("Col3", width=100)
        self.tv.heading("#0", text="Phantom", anchor="w")
        self.tv.heading("Col1", text="Column1", anchor="w")
        self.tv.heading("Col2", text="Column2", anchor="center")
        self.tv.heading("Col3", text="Column3", anchor="w")
        # count = 0
        # for i in range(20):
        #     self.tv.insert(parent='', index="end", iid=count, text="Parent" + str(count),
        #                    values=("Col1" + str(count), "Col2" + str(count), "Col3" + str(count)))
        #     count += 1

        self.add_button = tk.Button(self.Canvas1)
        self.add_button.place(relx=0.402, rely=0.871, height=24, width=79)
        self.add_button.configure(activebackground="#ececec", activeforeground="#000000", background="#3F454C",
                                  borderwidth="0", disabledforeground="#a3a3a3", font="-family {Segoe UI} -size 9 "
                                                                                      "-weight bold",
                                  foreground="white", highlightbackground="#d9d9d9", highlightcolor="black",
                                  pady="0", text='''Add''')

        self.delete_button = tk.Button(self.Canvas1)
        self.delete_button.place(relx=0.593, rely=0.871, height=24, width=79)
        self.delete_button.configure(activebackground="#ececec", activeforeground="#000000", background="#3F454C",
                                     borderwidth="0", disabledforeground="#a3a3a3", font="-family {Segoe UI} -size 9 "
                                                                                         "-weight bold",
                                     foreground="white", highlightbackground="#d9d9d9", highlightcolor="black",
                                     text="Delete")

        self.modify_button = tk.Button(self.Canvas1)
        self.modify_button.place(relx=0.784, rely=0.871, height=24, width=79)
        self.modify_button.configure(activebackground="#ececec", activeforeground="#000000", background="#3F454C",
                                     borderwidth="0", disabledforeground="#a3a3a3",
                                     font="-family {Segoe UI} -size 9 -weight bold",
                                     foreground="white", highlightbackground="#d9d9d9", highlightcolor="black",
                                     text='''Modify''')

        self.back_button = tk.Button(self.Canvas1)
        self.back_button.place(relx=0.038, rely=0.871, height=24, width=79)
        self.back_button.configure(activebackground="#ececec", activeforeground="#000000", background="#343a40",
                                   borderwidth="0", disabledforeground="#a3a3a3",
                                   font="-family {Segoe UI} -size 9 -weight bold", foreground="#ffffff",
                                   highlightbackground="#d9d9d9", highlightcolor="black", pady="0", text='''Back''',
                                   command=self.back)

    def back(self):
        self.master.withdraw()
        MainScreen(Toplevel(self.master))


class Attendance:
    def __init__(self, top=None):
        self.master = top
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.', background='#d9d9d9')
        self.style.configure('.', foreground="#000000")
        self.style.configure('.', font="TkDefaultFont")
        self.style.map('.', background=
        [('selected', "#d9d9d9"), ('active', "#ececec")])

        top.geometry("600x450+383+106")
        top.minsize(120, 1)
        top.maxsize(1370, 749)
        top.resizable(0, 0)
        top.title("Attendance ")
        top.configure(background="#212529")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.Canvas1 = tk.Canvas(top)
        self.Canvas1.place(relx=0.067, rely=0.111, relheight=0.74
                           , relwidth=0.872)
        self.Canvas1.configure(background="white")
        self.Canvas1.configure(insertbackground="black", highlightbackground="#d9d9d9", highlightcolor="black")
        self.Canvas1.configure(relief="ridge")
        self.Canvas1.configure(selectbackground="blue")
        self.Canvas1.configure(selectforeground="white")

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.367, rely=0.022, height=31, width=174)
        self.Label1.configure(background="#212529", font="-family {Segoe UI} -size 13 -weight bold",
                              foreground="#ffffff", text='''Attendance Table''')

        self.style.configure('Treeview', font="TkDefaultFont", borderwidth=0)
        self.tv = ScrolledTreeView(self.Canvas1)
        self.tv.place(relx=0.0, rely=0.0, relheight=0.712, relwidth=1.0)
        self.tv['columns'] = ("Col1", "Col2", "Col3")
        self.tv.column("#0", width=50)
        self.tv.column("Col1", width=100)
        self.tv.column("Col2", width=100, anchor="center")
        self.tv.column("Col3", width=100)
        self.tv.heading("#0", text="Phantom", anchor="w")
        self.tv.heading("Col1", text="Column1", anchor="w")
        self.tv.heading("Col2", text="Column2", anchor="center")
        self.tv.heading("Col3", text="Column3", anchor="w")
        # count = 0
        # for i in range(20):
        #     self.tv.insert(parent='', index="end", iid=count, text="Parent" + str(count),
        #                    values=("Col1" + str(count), "Col2" + str(count), "Col3" + str(count)))
        #     count += 1

        self.add_button = tk.Button(self.Canvas1)
        self.add_button.place(relx=0.402, rely=0.871, height=24, width=79)
        self.add_button.configure(activebackground="#ececec", activeforeground="#000000", background="#3F454C",
                                  borderwidth="0", disabledforeground="#a3a3a3", font="-family {Segoe UI} -size 9 "
                                                                                      "-weight bold",
                                  foreground="white", highlightbackground="#d9d9d9", highlightcolor="black",
                                  pady="0", text='''Add''')

        self.delete_button = tk.Button(self.Canvas1)
        self.delete_button.place(relx=0.593, rely=0.871, height=24, width=79)
        self.delete_button.configure(activebackground="#ececec", activeforeground="#000000", background="#3F454C",
                                     borderwidth="0", disabledforeground="#a3a3a3", font="-family {Segoe UI} -size 9 "
                                                                                         "-weight bold",
                                     foreground="white", highlightbackground="#d9d9d9", highlightcolor="black",
                                     text="Delete")

        self.modify_button = tk.Button(self.Canvas1)
        self.modify_button.place(relx=0.784, rely=0.871, height=24, width=79)
        self.modify_button.configure(activebackground="#ececec", activeforeground="#000000", background="#3F454C",
                                     borderwidth="0", disabledforeground="#a3a3a3",
                                     font="-family {Segoe UI} -size 9 -weight bold",
                                     foreground="white", highlightbackground="#d9d9d9", highlightcolor="black",
                                     text='''Modify''')

        self.back_button = tk.Button(self.Canvas1)
        self.back_button.place(relx=0.038, rely=0.871, height=24, width=79)
        self.back_button.configure(activebackground="#ececec", activeforeground="#000000", background="#343a40",
                                   borderwidth="0", disabledforeground="#a3a3a3",
                                   font="-family {Segoe UI} -size 9 -weight bold", foreground="#ffffff",
                                   highlightbackground="#d9d9d9", highlightcolor="black", pady="0", text='''Back''',
                                   command=self.back)

    def back(self):
        self.master.withdraw()
        MainScreen(Toplevel(self.master))


class Branch:
    def __init__(self, top=None):
        self.master = top
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.', background='#d9d9d9')
        self.style.configure('.', foreground="#000000")
        self.style.configure('.', font="TkDefaultFont")
        self.style.map('.', background=
        [('selected', "#d9d9d9"), ('active', "#ececec")])

        top.geometry("600x450+383+106")
        top.minsize(120, 1)
        top.maxsize(1370, 749)
        top.resizable(0, 0)
        top.title("Branch")
        top.configure(background="#212529")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.Canvas1 = tk.Canvas(top)
        self.Canvas1.place(relx=0.067, rely=0.111, relheight=0.74
                           , relwidth=0.872)
        self.Canvas1.configure(background="white")
        self.Canvas1.configure(insertbackground="black", highlightbackground="#d9d9d9", highlightcolor="black")
        self.Canvas1.configure(relief="ridge")
        self.Canvas1.configure(selectbackground="blue")
        self.Canvas1.configure(selectforeground="white")

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.367, rely=0.022, height=31, width=174)
        self.Label1.configure(background="#212529", font="-family {Segoe UI} -size 13 -weight bold",
                              foreground="#ffffff", text='''Branch Table''')

        self.style.configure('Treeview', font="TkDefaultFont", borderwidth=0)
        global tv
        tv = ScrolledTreeView(self.Canvas1)
        tv.place(relx=0.0, rely=0.0, relheight=0.712, relwidth=1.0)
        tv['columns'] = ("Col1", "Col2")
        tv.column("#0", width=0, stretch="NO")
        tv.column("Col1", width=100)
        tv.column("Col2", width=100, anchor="center")
        tv.heading("#0", text="", anchor="w")
        tv.heading("Col1", text="Branch id", anchor="w")
        tv.heading("Col2", text="Branch name", anchor="center")

        #        count = 0
        #        for i in range(20):
        #            self.tv.insert(parent='', index="end", iid=count, text="Parent" + str(count),
        #                values=("Col1 long long long long long long long long long long long text" + str(count), "Col2 such a long freaking text" + str(count)))
        #            count += 1

        self.add_button = tk.Button(self.Canvas1, command=self.select_add)
        self.add_button.place(relx=0.402, rely=0.871, height=24, width=79)
        self.add_button.configure(activebackground="#ececec", activeforeground="#000000", background="#3F454C",
                                  borderwidth="0", disabledforeground="#a3a3a3", font="-family {Segoe UI} -size 9 "
                                                                                      "-weight bold",
                                  foreground="white", highlightbackground="#d9d9d9", highlightcolor="black",
                                  pady="0", text='''Add''')

        self.delete_button = tk.Button(self.Canvas1, command=self.select_delete)
        self.delete_button.place(relx=0.593, rely=0.871, height=24, width=79)
        self.delete_button.configure(activebackground="#ececec", activeforeground="#000000", background="#3F454C",
                                     borderwidth="0", disabledforeground="#a3a3a3", font="-family {Segoe UI} -size 9 "
                                                                                         "-weight bold",
                                     foreground="white", highlightbackground="#d9d9d9", highlightcolor="black",
                                     text="Delete")

        self.modify_button = tk.Button(self.Canvas1, command=self.select_modify)
        self.modify_button.place(relx=0.784, rely=0.871, height=24, width=79)
        self.modify_button.configure(activebackground="#ececec", activeforeground="#000000", background="#3F454C",
                                     borderwidth="0", disabledforeground="#a3a3a3",
                                     font="-family {Segoe UI} -size 9 -weight bold",
                                     foreground="white", highlightbackground="#d9d9d9", highlightcolor="black",
                                     text='''Modify''')

        self.back_button = tk.Button(self.Canvas1)
        self.back_button.place(relx=0.038, rely=0.871, height=24, width=79)
        self.back_button.configure(activebackground="#ececec", activeforeground="#000000", background="#343a40",
                                   borderwidth="0", disabledforeground="#a3a3a3",
                                   font="-family {Segoe UI} -size 9 -weight bold", foreground="#ffffff",
                                   highlightbackground="#d9d9d9", highlightcolor="black", pady="0", text='''Back''',
                                   command=self.back)

        # real data
        mycursor.execute("SELECT * from branch;")
        output = mycursor.fetchall()

        for list_item in output:
            tv.insert(parent='', index="end", text="Parent", values=(str(list_item[0]), str(list_item[1])))

        # sample data

    #        count = 0
    #        for i in range(20):
    #            tv.insert(parent='', index="end", iid=count, text="Parent" + str(count), values=("Col1 long long long long long long long long long long long text" + str(count), "Col2 such a long freaking text" + str(count)))
    #            count += 1

    def back(self):
        self.master.withdraw()
        MainScreen(Toplevel(self.master))

    def select_modify(self):
        if (tv.focus() != ""):
            BranchModify(Toplevel(self.master))
        else:
            messagebox.showerror("Please select a row to be modified")

    def select_delete(self):
        try:
            #            row_id = int(tv.focus().replace("I", ""))
            item = tv.item(tv.focus())
            tv.delete(tv.focus())
            sql_query = "DELETE FROM branch WHERE branch_id=" + str(item['values'][0]) + ";"
            try:
                mycursor.execute(sql_query)  # executing query
            except (mysql.connector.Error, mysql.connector.Warning) as e:  # fetching error
                messagebox.showerror(str(e))  # displaying error

        except:
            messagebox.showerror("showerror", "Please select a row to be deleted")
        mydb.commit()

    def select_add(self):
        BranchAdd(Toplevel(self.master))


class CustomQuery:
    def __init__(self, top=None):
        self.master = top
        '''This class configures and populates the toplevel window.
                        top is the toplevel containing window.'''
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.', background="#d9d9d9")
        self.style.configure('.', foreground="#000000")
        self.style.map('.', background=[('selected', "#d9d9d9"), ('active', "#ececec")])

        top.geometry("705x450+373+129")
        top.minsize(120, 1)
        top.maxsize(1370, 749)
        top.resizable(1, 1)
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

        self.Entry1 = tk.Entry(top)
        self.Entry1.place(relx=0.085, rely=0.067, height=20, relwidth=0.743)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(highlightbackground="#d9d9d9")
        self.Entry1.configure(highlightcolor="black")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(selectbackground="blue")
        self.Entry1.configure(selectforeground="white")

        self.execute_button = tk.Button(top, command=self.select_execute)
        self.execute_button.place(relx=0.851, rely=0.067, height=24, width=87)
        self.execute_button.configure(activebackground="#ececec")
        self.execute_button.configure(activeforeground="#000000")
        self.execute_button.configure(background="#CED4DA")
        self.execute_button.configure(disabledforeground="#a3a3a3")
        self.execute_button.configure(foreground="#000000")
        self.execute_button.configure(highlightbackground="#d9d9d9")
        self.execute_button.configure(highlightcolor="black")
        self.execute_button.configure(pady="0")
        self.execute_button.configure(text='''Execute''')

        self.clear_button = tk.Button(top, command=self.select_clear)
        self.clear_button.place(relx=0.539, rely=0.889, height=24, width=87)
        self.clear_button.configure(activebackground="#ececec")
        self.clear_button.configure(activeforeground="#000000")
        self.clear_button.configure(background="#CED4DA")
        self.clear_button.configure(disabledforeground="#a3a3a3")
        self.clear_button.configure(foreground="#000000")
        self.clear_button.configure(highlightbackground="#d9d9d9")
        self.clear_button.configure(highlightcolor="black")
        self.clear_button.configure(pady="0")
        self.clear_button.configure(text='''Clear''')

        global Scrolledtext1
        Scrolledtext1 = ScrolledText(top, state="disable")
        Scrolledtext1.place(relx=0.028, rely=0.2, relheight=0.633
                            , relwidth=0.945)
        Scrolledtext1.configure(background="white")
        Scrolledtext1.configure(font="TkTextFont")
        Scrolledtext1.configure(foreground="black")
        Scrolledtext1.configure(highlightbackground="#d9d9d9")
        Scrolledtext1.configure(highlightcolor="black")
        Scrolledtext1.configure(insertbackground="black")
        Scrolledtext1.configure(insertborderwidth="3")
        Scrolledtext1.configure(selectbackground="blue")
        Scrolledtext1.configure(selectforeground="white")
        Scrolledtext1.configure(wrap="none")

        self.back_button = tk.Button(top, command=self.back)
        self.back_button.place(relx=0.355, rely=0.889, height=24, width=87)
        self.back_button.configure(activebackground="#ececec")
        self.back_button.configure(activeforeground="#000000")
        self.back_button.configure(background="#CED4DA")
        self.back_button.configure(disabledforeground="#a3a3a3")
        self.back_button.configure(foreground="#000000")
        self.back_button.configure(highlightbackground="#d9d9d9")
        self.back_button.configure(highlightcolor="black")
        self.back_button.configure(pady="0")
        self.back_button.configure(text='''Back''')

    def select_execute(self):
        sql_query = self.Entry1.get()  # getting text from entry
        try:
            mycursor.execute(sql_query)  # executing query
            self.display_output(mycursor.fetchall(), 1)  # displaying output
        except (mysql.connector.Error, mysql.connector.Warning) as e:  # fetching error
            self.display_output("ERROR MESSAGE : \n" + str(e), 2)  # displaying error
        mydb.commit()

    def select_clear(self):
        Scrolledtext1.config(state="normal")
        self.Entry1.delete(0, 'end')
        Scrolledtext1.delete("1.0", "end")
        Scrolledtext1.config(state="disable")

    def display_output(self, output_message, choice):

        Scrolledtext1.config(state="normal")  # changing text box's state so that we can edit it
        Scrolledtext1.delete("1.0", "end")  # deletes previous contents

        if choice == 1:  # select statement
            myTable = PrettyTable()
            for list_item in output_message:
                myTable.add_row(list_item)
            print(myTable)
            Scrolledtext1.insert(1.0, myTable)  # showing output message

        else:  # not select  statement
            print(output_message)
            Scrolledtext1.insert(1.0, output_message)  # showing output message
        Scrolledtext1.config(state="disable")  # disabling text box's state so that user cannot change it's content

    def back(self):
        self.master.withdraw()
        MainScreen(Toplevel(self.master))


class AutoScroll(object):
    '''Configure the scrollbars for a widget.'''

    def __init__(self, master):
        #  Rozen. Added the try-except clauses so that this class
        #  could be used for scrolled entry widget for which vertical
        #  scrolling is not supported. 5/7/14.
        try:
            vsb = ttk.Scrollbar(master, orient='vertical', command=self.yview)
        except:
            pass
        hsb = ttk.Scrollbar(master, orient='horizontal', command=self.xview)
        try:
            self.configure(yscrollcommand=self._autoscroll(vsb))
        except:
            pass
        self.configure(xscrollcommand=self._autoscroll(hsb))
        self.grid(column=0, row=0, sticky='nsew')
        try:
            vsb.grid(column=1, row=0, sticky='ns')
        except:
            pass
        hsb.grid(column=0, row=1, sticky='ew')
        master.grid_columnconfigure(0, weight=1)
        master.grid_rowconfigure(0, weight=1)
        # Copy geometry methods of master  (taken from ScrolledText.py)
        if py3:
            methods = tk.Pack.__dict__.keys() | tk.Grid.__dict__.keys() | tk.Place.__dict__.keys()
        else:
            methods = tk.Pack.__dict__.keys() + tk.Grid.__dict__.keys() + tk.Place.__dict__.keys()
        for meth in methods:
            if meth[0] != '_' and meth not in ('config', 'configure'):
                setattr(self, meth, getattr(master, meth))

    @staticmethod
    def _autoscroll(sbar):
        '''Hide and show scrollbar as needed.'''

        def wrapped(first, last):
            first, last = float(first), float(last)
            if first <= 0 and last >= 1:
                sbar.grid_remove()
            else:
                sbar.grid()
            sbar.set(first, last)

        return wrapped

    def __str__(self):
        return str(self.master)


def _create_container(func):
    '''Creates a ttk Frame with a given master, and use this new frame to
                place the scrollbars and the widget.'''

    def wrapped(cls, master, **kw):
        container = ttk.Frame(master)
        container.bind('<Enter>', lambda e: _bound_to_mousewheel(e, container))
        container.bind('<Leave>', lambda e: _unbound_to_mousewheel(e, container))
        return func(cls, container, **kw)

    return wrapped


class ScrolledText(AutoScroll, tk.Text):
    '''A standard Tkinter Text widget with scrollbars that will
        automatically show/hide as needed.'''

    @_create_container
    def __init__(self, master, **kw):
        tk.Text.__init__(self, master, **kw)
        AutoScroll.__init__(self, master)


class ScrolledTreeView(AutoScroll, ttk.Treeview):
    '''A standard ttk Treeview widget with scrollbars that will
                automatically show/hide as needed.'''

    @_create_container
    def __init__(self, master, **kw):
        ttk.Treeview.__init__(self, master, **kw)
        AutoScroll.__init__(self, master)


def _bound_to_mousewheel(event, widget):
    child = widget.winfo_children()[0]
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        child.bind_all('<MouseWheel>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-MouseWheel>', lambda e: _on_shiftmouse(e, child))
    else:
        child.bind_all('<Button-4>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Button-5>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-Button-4>', lambda e: _on_shiftmouse(e, child))
        child.bind_all('<Shift-Button-5>', lambda e: _on_shiftmouse(e, child))


def _unbound_to_mousewheel(event, widget):
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        widget.unbind_all('<MouseWheel>')
        widget.unbind_all('<Shift-MouseWheel>')
    else:
        widget.unbind_all('<Button-4>')
        widget.unbind_all('<Button-5>')
        widget.unbind_all('<Shift-Button-4>')
        widget.unbind_all('<Shift-Button-5>')


def _on_mousewheel(event, widget):
    if platform.system() == 'Windows':
        widget.yview_scroll(-1 * int(event.delta / 120), 'units')
    elif platform.system() == 'Darwin':
        widget.yview_scroll(-1 * int(event.delta), 'units')
    else:
        if event.num == 4:
            widget.yview_scroll(-1, 'units')
        elif event.num == 5:
            widget.yview_scroll(1, 'units')


def _on_shiftmouse(event, widget):
    if platform.system() == 'Windows':
        widget.xview_scroll(-1 * int(event.delta / 120), 'units')
    elif platform.system() == 'Darwin':
        widget.xview_scroll(-1 * int(event.delta), 'units')
    else:
        if event.num == 4:
            widget.xview_scroll(-1, 'units')
        elif event.num == 5:
            widget.xview_scroll(1, 'units')


class BranchAdd:
    def __init__(self, top=None):
        self.master = top
        top.geometry("342x139+527+141")
        top.minsize(120, 1)
        top.maxsize(1370, 749)
        top.resizable(1,  1)
        top.title("Add")
        top.configure(background="#CED4DA")

        self.id_label = tk.Label(top)
        self.id_label.place(relx=0.234, rely=0.144, height=17, width=74)
        self.id_label.configure(background="#CED4DA")
        self.id_label.configure(disabledforeground="#a3a3a3")
        self.id_label.configure(foreground="#000000")
        self.id_label.configure(text='''Branch id :''')

        self.name_label = tk.Label(top)
        self.name_label.place(relx=0.187, rely=0.36, height=17, width=84)
        self.name_label.configure(background="#CED4DA")
        self.name_label.configure(disabledforeground="#a3a3a3")
        self.name_label.configure(foreground="#000000")
        self.name_label.configure(text='''Branch name :''')

        self.id_entry = tk.Entry(top)
        self.id_entry.place(relx=0.468, rely=0.144, height=20, relwidth=0.304)
        self.id_entry.configure(background="white")
        self.id_entry.configure(disabledforeground="#a3a3a3")
        self.id_entry.configure(font="TkFixedFont")
        self.id_entry.configure(foreground="#000000")
        self.id_entry.configure(insertbackground="black")

        self.name_entry = tk.Entry(top)
        self.name_entry.place(relx=0.468, rely=0.36, height=20, relwidth=0.304)
        self.name_entry.configure(background="white")
        self.name_entry.configure(disabledforeground="#a3a3a3")
        self.name_entry.configure(font="TkFixedFont")
        self.name_entry.configure(foreground="#000000")
        self.name_entry.configure(insertbackground="black")

        self.back_button = tk.Button(top, command=self.select_back)
        self.back_button.place(relx=0.146, rely=0.647, height=24, width=87)
        self.back_button.configure(activebackground="#ececec")
        self.back_button.configure(activeforeground="#000000")
        self.back_button.configure(background="#E9ECEF")
        self.back_button.configure(disabledforeground="#a3a3a3")
        self.back_button.configure(foreground="#000000")
        self.back_button.configure(highlightbackground="#d9d9d9")
        self.back_button.configure(highlightcolor="black")
        self.back_button.configure(pady="0")
        self.back_button.configure(text='''Back''')

        self.add_button = tk.Button(top, command= lambda :self.select_add(self.id_entry.get(),self.name_entry.get()))
        self.add_button.place(relx=0.556, rely=0.647, height=24, width=87)
        self.add_button.configure(activebackground="#ececec")
        self.add_button.configure(activeforeground="#000000")
        self.add_button.configure(background="#E9ECEF")
        self.add_button.configure(disabledforeground="#a3a3a3")
        self.add_button.configure(foreground="#000000")
        self.add_button.configure(highlightbackground="#d9d9d9")
        self.add_button.configure(highlightcolor="black")
        self.add_button.configure(pady="0")
        self.add_button.configure(text='''Add''')
      
    def select_back(self):
      self.master.withdraw()
      
    def select_add(self, branch_id, branch_name):
      if branch_id.isnumeric() and len(branch_id)!=0:
        if len(branch_name)!=0:
          
          sql_query = "INSERT INTO branch VALUES(" + branch_id + ", '" + branch_name + "');"
          try:
            mycursor.execute(sql_query)                                     #executing query
            tv.insert(parent='', index='end', text="Parent", values=(str(branch_id), branch_name))
            print("inside try : ",mycursor.fetchall())
          except (mysql.connector.Error, mysql.connector.Warning) as e:       #fetching error
            messagebox.showerror("ERROR MESSAGE :\n" + str(e)) 
            print("inside except : ",mycursor.fetchall())                             #displaying error
          
        else:
          messagebox.showerror("Enter branch name")
      else:
        messagebox.showerror("Enter proper branch id")
      print(branch_id,branch_name)
      self.master.withdraw()
      mydb.commit()


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


class ExamAdd:
    def __init__(self, top=None):
        top.geometry("342x316+624+174")
        top.minsize(120, 1)
        top.maxsize(1370, 749)
        top.resizable(1,  1)
        top.title("Add")
        top.configure(background="#CED4DA")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.exam_id_label = tk.Label(top)
        self.exam_id_label.place(relx=0.234, rely=0.063, height=21, width=64)
        self.exam_id_label.configure(activebackground="#f9f9f9")
        self.exam_id_label.configure(activeforeground="black")
        self.exam_id_label.configure(background="#CED4DA")
        self.exam_id_label.configure(disabledforeground="#a3a3a3")
        self.exam_id_label.configure(foreground="#000000")
        self.exam_id_label.configure(highlightbackground="#d9d9d9")
        self.exam_id_label.configure(highlightcolor="black")
        self.exam_id_label.configure(text='''Exam id :''')

        self.exam_duration_label = tk.Label(top)
        self.exam_duration_label.place(relx=0.14, rely=0.253, height=18
                , width=94)
        self.exam_duration_label.configure(activebackground="#f9f9f9")
        self.exam_duration_label.configure(activeforeground="black")
        self.exam_duration_label.configure(background="#CED4DA")
        self.exam_duration_label.configure(disabledforeground="#a3a3a3")
        self.exam_duration_label.configure(foreground="#000000")
        self.exam_duration_label.configure(highlightbackground="#d9d9d9")
        self.exam_duration_label.configure(highlightcolor="black")
        self.exam_duration_label.configure(text='''Exam duration :''')

        self.exam_id_entry = tk.Entry(top)
        self.exam_id_entry.place(relx=0.468, rely=0.063, height=20
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

        self.name_entry = tk.Entry(top)
        self.name_entry.place(relx=0.468, rely=0.158, height=20, relwidth=0.304)
        self.name_entry.configure(background="white")
        self.name_entry.configure(disabledforeground="#a3a3a3")
        self.name_entry.configure(font="TkFixedFont")
        self.name_entry.configure(foreground="#000000")
        self.name_entry.configure(highlightbackground="#d9d9d9")
        self.name_entry.configure(highlightcolor="black")
        self.name_entry.configure(insertbackground="black")
        self.name_entry.configure(selectbackground="blue")
        self.name_entry.configure(selectforeground="white")

        self.back_button = tk.Button(top)
        self.back_button.place(relx=0.175, rely=0.854, height=24, width=87)
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
        self.add_button.place(relx=0.585, rely=0.854, height=24, width=87)
        self.add_button.configure(activebackground="#ececec")
        self.add_button.configure(activeforeground="#000000")
        self.add_button.configure(background="#E9ECEF")
        self.add_button.configure(disabledforeground="#a3a3a3")
        self.add_button.configure(foreground="#000000")
        self.add_button.configure(highlightbackground="#d9d9d9")
        self.add_button.configure(highlightcolor="black")
        self.add_button.configure(pady="0")
        self.add_button.configure(text='''Add''')

        self.tot_ques_label = tk.Label(top)
        self.tot_ques_label.place(relx=0.117, rely=0.443, height=18, width=104)
        self.tot_ques_label.configure(activebackground="#f9f9f9")
        self.tot_ques_label.configure(activeforeground="black")
        self.tot_ques_label.configure(background="#CED4DA")
        self.tot_ques_label.configure(disabledforeground="#a3a3a3")
        self.tot_ques_label.configure(foreground="#000000")
        self.tot_ques_label.configure(highlightbackground="#d9d9d9")
        self.tot_ques_label.configure(highlightcolor="black")
        self.tot_ques_label.configure(text='''Total questions :''')

        self.branch_id_label = tk.Label(top)
        self.branch_id_label.place(relx=0.205, rely=0.633, height=18, width=74)
        self.branch_id_label.configure(activebackground="#f9f9f9")
        self.branch_id_label.configure(activeforeground="black")
        self.branch_id_label.configure(background="#CED4DA")
        self.branch_id_label.configure(disabledforeground="#a3a3a3")
        self.branch_id_label.configure(foreground="#000000")
        self.branch_id_label.configure(highlightbackground="#d9d9d9")
        self.branch_id_label.configure(highlightcolor="black")
        self.branch_id_label.configure(text='''Branch id :''')

        self.duration_entry = tk.Entry(top)
        self.duration_entry.place(relx=0.468, rely=0.253, height=20
                , relwidth=0.304)
        self.duration_entry.configure(background="white")
        self.duration_entry.configure(disabledforeground="#a3a3a3")
        self.duration_entry.configure(font="TkFixedFont")
        self.duration_entry.configure(foreground="#000000")
        self.duration_entry.configure(highlightbackground="#d9d9d9")
        self.duration_entry.configure(highlightcolor="black")
        self.duration_entry.configure(insertbackground="black")
        self.duration_entry.configure(selectbackground="blue")
        self.duration_entry.configure(selectforeground="white")

        self.date_entry = tk.Entry(top)
        self.date_entry.place(relx=0.468, rely=0.348, height=20, relwidth=0.304)
        self.date_entry.configure(background="white")
        self.date_entry.configure(disabledforeground="#a3a3a3")
        self.date_entry.configure(font="TkFixedFont")
        self.date_entry.configure(foreground="#000000")
        self.date_entry.configure(highlightbackground="#d9d9d9")
        self.date_entry.configure(highlightcolor="black")
        self.date_entry.configure(insertbackground="black")
        self.date_entry.configure(selectbackground="blue")
        self.date_entry.configure(selectforeground="white")

        self.tot_ques_entry = tk.Entry(top)
        self.tot_ques_entry.place(relx=0.468, rely=0.443, height=20
                , relwidth=0.304)
        self.tot_ques_entry.configure(background="white")
        self.tot_ques_entry.configure(disabledforeground="#a3a3a3")
        self.tot_ques_entry.configure(font="TkFixedFont")
        self.tot_ques_entry.configure(foreground="#000000")
        self.tot_ques_entry.configure(highlightbackground="#d9d9d9")
        self.tot_ques_entry.configure(highlightcolor="black")
        self.tot_ques_entry.configure(insertbackground="black")
        self.tot_ques_entry.configure(selectbackground="blue")
        self.tot_ques_entry.configure(selectforeground="white")

        self.tot_marks_entry = tk.Entry(top)
        self.tot_marks_entry.place(relx=0.468, rely=0.538, height=20
                , relwidth=0.304)
        self.tot_marks_entry.configure(background="white")
        self.tot_marks_entry.configure(disabledforeground="#a3a3a3")
        self.tot_marks_entry.configure(font="TkFixedFont")
        self.tot_marks_entry.configure(foreground="#000000")
        self.tot_marks_entry.configure(highlightbackground="#d9d9d9")
        self.tot_marks_entry.configure(highlightcolor="black")
        self.tot_marks_entry.configure(insertbackground="black")
        self.tot_marks_entry.configure(selectbackground="blue")
        self.tot_marks_entry.configure(selectforeground="white")

        self.branch_id_entry = tk.Entry(top)
        self.branch_id_entry.place(relx=0.468, rely=0.633, height=20
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

        self.sub_code_entry = tk.Entry(top)
        self.sub_code_entry.place(relx=0.468, rely=0.728, height=20
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

        self.exam_name_label = tk.Label(top)
        self.exam_name_label.place(relx=0.175, rely=0.158, height=21, width=84)
        self.exam_name_label.configure(activebackground="#f9f9f9")
        self.exam_name_label.configure(activeforeground="black")
        self.exam_name_label.configure(background="#CED4DA")
        self.exam_name_label.configure(disabledforeground="#a3a3a3")
        self.exam_name_label.configure(foreground="#000000")
        self.exam_name_label.configure(highlightbackground="#d9d9d9")
        self.exam_name_label.configure(highlightcolor="black")
        self.exam_name_label.configure(text='''Exam name :''')

        self.exam_date_label = tk.Label(top)
        self.exam_date_label.place(relx=0.199, rely=0.348, height=21, width=74)
        self.exam_date_label.configure(activebackground="#f9f9f9")
        self.exam_date_label.configure(activeforeground="black")
        self.exam_date_label.configure(background="#CED4DA")
        self.exam_date_label.configure(disabledforeground="#a3a3a3")
        self.exam_date_label.configure(foreground="#000000")
        self.exam_date_label.configure(highlightbackground="#d9d9d9")
        self.exam_date_label.configure(highlightcolor="black")
        self.exam_date_label.configure(text='''Exam date :''')

        self.tot_marks_label = tk.Label(top)
        self.tot_marks_label.place(relx=0.175, rely=0.538, height=21, width=84)
        self.tot_marks_label.configure(activebackground="#f9f9f9")
        self.tot_marks_label.configure(activeforeground="black")
        self.tot_marks_label.configure(background="#CED4DA")
        self.tot_marks_label.configure(disabledforeground="#a3a3a3")
        self.tot_marks_label.configure(foreground="#000000")
        self.tot_marks_label.configure(highlightbackground="#d9d9d9")
        self.tot_marks_label.configure(highlightcolor="black")
        self.tot_marks_label.configure(text='''Total marks :''')

        self.sub_code_label = tk.Label(top)
        self.sub_code_label.place(relx=0.164, rely=0.728, height=21, width=84)
        self.sub_code_label.configure(activebackground="#f9f9f9")
        self.sub_code_label.configure(activeforeground="black")
        self.sub_code_label.configure(background="#CED4DA")
        self.sub_code_label.configure(disabledforeground="#a3a3a3")
        self.sub_code_label.configure(foreground="#000000")
        self.sub_code_label.configure(highlightbackground="#d9d9d9")
        self.sub_code_label.configure(highlightcolor="black")
        self.sub_code_label.configure(text='''Subject code :''')


class ResultAdd:
    def __init__(self, top=None):
        top.geometry("342x224+501+160")
        top.minsize(120, 1)
        top.maxsize(1370, 749)
        top.resizable(0,0)
        top.title("Add")
        top.configure(background="#CED4DA")
        top.configure(highlightcolor="black")

        self.res_id_label = tk.Label(top)
        self.res_id_label.place(relx=0.234, rely=0.089, height=15, width=64)
        self.res_id_label.configure(activebackground="#f9f9f9")
        self.res_id_label.configure(activeforeground="black")
        self.res_id_label.configure(background="#CED4DA")
        self.res_id_label.configure(disabledforeground="#a3a3a3")
        self.res_id_label.configure(foreground="#000000")
        self.res_id_label.configure(highlightbackground="#d9d9d9")
        self.res_id_label.configure(highlightcolor="black")
        self.res_id_label.configure(text='''Result id :''')

        self.marks_label = tk.Label(top)
        self.marks_label.place(relx=0.117, rely=0.223, height=19, width=104)
        self.marks_label.configure(activebackground="#f9f9f9")
        self.marks_label.configure(activeforeground="black")
        self.marks_label.configure(background="#CED4DA")
        self.marks_label.configure(disabledforeground="#a3a3a3")
        self.marks_label.configure(foreground="#000000")
        self.marks_label.configure(highlightbackground="#d9d9d9")
        self.marks_label.configure(highlightcolor="black")
        self.marks_label.configure(text='''Marks obtained :''')

        self.res_id_entry = tk.Entry(top)
        self.res_id_entry.place(relx=0.468, rely=0.089, height=20
                , relwidth=0.304)
        self.res_id_entry.configure(background="white")
        self.res_id_entry.configure(disabledforeground="#a3a3a3")
        self.res_id_entry.configure(font="TkFixedFont")
        self.res_id_entry.configure(foreground="#000000")
        self.res_id_entry.configure(highlightbackground="#d9d9d9")
        self.res_id_entry.configure(highlightcolor="black")
        self.res_id_entry.configure(insertbackground="black")
        self.res_id_entry.configure(selectbackground="blue")
        self.res_id_entry.configure(selectforeground="white")

        self.marks_entry = tk.Entry(top)
        self.marks_entry.place(relx=0.468, rely=0.223, height=20, relwidth=0.304)

        self.marks_entry.configure(background="white")
        self.marks_entry.configure(disabledforeground="#a3a3a3")
        self.marks_entry.configure(font="TkFixedFont")
        self.marks_entry.configure(foreground="#000000")
        self.marks_entry.configure(highlightbackground="#d9d9d9")
        self.marks_entry.configure(highlightcolor="black")
        self.marks_entry.configure(insertbackground="black")
        self.marks_entry.configure(selectbackground="blue")
        self.marks_entry.configure(selectforeground="white")

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

        self.res_label = tk.Label(top)
        self.res_label.place(relx=0.263, rely=0.357, height=19, width=54)
        self.res_label.configure(activebackground="#f9f9f9")
        self.res_label.configure(activeforeground="black")
        self.res_label.configure(background="#CED4DA")
        self.res_label.configure(disabledforeground="#a3a3a3")
        self.res_label.configure(foreground="#000000")
        self.res_label.configure(highlightbackground="#d9d9d9")
        self.res_label.configure(highlightcolor="black")
        self.res_label.configure(text='''Result :''')

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

        self.res_entry = tk.Entry(top)
        self.res_entry.place(relx=0.468, rely=0.357, height=20, relwidth=0.304)
        self.res_entry.configure(background="white")
        self.res_entry.configure(disabledforeground="#a3a3a3")
        self.res_entry.configure(font="TkFixedFont")
        self.res_entry.configure(foreground="#000000")
        self.res_entry.configure(highlightbackground="#d9d9d9")
        self.res_entry.configure(highlightcolor="black")
        self.res_entry.configure(insertbackground="black")
        self.res_entry.configure(selectbackground="blue")
        self.res_entry.configure(selectforeground="white")

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


class StudentAdd:
    def __init__(self, top=None):

        top.geometry("342x224+510+158")
        top.minsize(120, 1)
        top.maxsize(1370, 749)
        top.resizable(0,0)
        top.title("Add")
        top.configure(background="#CED4DA")

        self.student_id_label = tk.Label(top)
        self.student_id_label.place(relx=0.211, rely=0.089, height=15, width=74)
        self.student_id_label.configure(activebackground="#f9f9f9")
        self.student_id_label.configure(activeforeground="black")
        self.student_id_label.configure(background="#CED4DA")
        self.student_id_label.configure(disabledforeground="#a3a3a3")
        self.student_id_label.configure(foreground="#000000")
        self.student_id_label.configure(highlightbackground="#d9d9d9")
        self.student_id_label.configure(highlightcolor="black")
        self.student_id_label.configure(text='''Student id :''')

        self.roll_no_label = tk.Label(top)
        self.roll_no_label.place(relx=0.257, rely=0.223, height=19, width=54)
        self.roll_no_label.configure(background="#CED4DA")
        self.roll_no_label.configure(disabledforeground="#a3a3a3")
        self.roll_no_label.configure(foreground="#000000")
        self.roll_no_label.configure(text='''Roll no. :''')

        self.student_id_entry = tk.Entry(top)
        self.student_id_entry.place(relx=0.468, rely=0.089, height=20
                , relwidth=0.304)
        self.student_id_entry.configure(background="white")
        self.student_id_entry.configure(foreground="#000000")
        self.student_id_entry.configure(highlightbackground="#d9d9d9")
        self.student_id_entry.configure(highlightcolor="black")
        self.student_id_entry.configure(insertbackground="black")
        self.student_id_entry.configure(selectbackground="blue")
        self.student_id_entry.configure(selectforeground="white")

        self.roll_no_entry = tk.Entry(top)
        self.roll_no_entry.place(relx=0.468, rely=0.223, height=20
                , relwidth=0.304)
        self.roll_no_entry.configure(background="white")
        self.roll_no_entry.configure(disabledforeground="#a3a3a3")
        self.roll_no_entry.configure(font="TkFixedFont")
        self.roll_no_entry.configure(foreground="#000000")
        self.roll_no_entry.configure(highlightbackground="#d9d9d9")
        self.roll_no_entry.configure(highlightcolor="black")
        self.roll_no_entry.configure(insertbackground="black")
        self.roll_no_entry.configure(selectbackground="blue")
        self.roll_no_entry.configure(selectforeground="white")

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

        self.email_label = tk.Label(top)
        self.email_label.place(relx=0.254, rely=0.357, height=19, width=64)
        self.email_label.configure(activebackground="#f9f9f9")
        self.email_label.configure(activeforeground="black")
        self.email_label.configure(background="#CED4DA")
        self.email_label.configure(disabledforeground="#a3a3a3")
        self.email_label.configure(foreground="#000000")
        self.email_label.configure(highlightbackground="#d9d9d9")
        self.email_label.configure(highlightcolor="black")
        self.email_label.configure(text='''E-mail :''')

        self.password_label = tk.Label(top)
        self.password_label.place(relx=0.234, rely=0.491, height=19, width=64)
        self.password_label.configure(activebackground="#f9f9f9")
        self.password_label.configure(activeforeground="black")
        self.password_label.configure(background="#CED4DA")
        self.password_label.configure(cursor="fleur")
        self.password_label.configure(disabledforeground="#a3a3a3")
        self.password_label.configure(foreground="#000000")
        self.password_label.configure(highlightbackground="#d9d9d9")
        self.password_label.configure(highlightcolor="black")
        self.password_label.configure(text='''Password :''')

        self.branch_id_label = tk.Label(top)
        self.branch_id_label.place(relx=0.219, rely=0.625, height=21, width=74)
        self.branch_id_label.configure(activebackground="#f9f9f9")
        self.branch_id_label.configure(activeforeground="black")
        self.branch_id_label.configure(background="#CED4DA")
        self.branch_id_label.configure(disabledforeground="#a3a3a3")
        self.branch_id_label.configure(foreground="#000000")
        self.branch_id_label.configure(highlightbackground="#d9d9d9")
        self.branch_id_label.configure(highlightcolor="black")
        self.branch_id_label.configure(text='''Branch id :''')

        self.email_entry = tk.Entry(top)
        self.email_entry.place(relx=0.468, rely=0.357, height=20, relwidth=0.304)

        self.email_entry.configure(background="white")
        self.email_entry.configure(disabledforeground="#a3a3a3")
        self.email_entry.configure(font="TkFixedFont")
        self.email_entry.configure(foreground="#000000")
        self.email_entry.configure(highlightbackground="#d9d9d9")
        self.email_entry.configure(highlightcolor="black")
        self.email_entry.configure(insertbackground="black")
        self.email_entry.configure(selectbackground="blue")
        self.email_entry.configure(selectforeground="white")

        self.password_entry = tk.Entry(top)
        self.password_entry.place(relx=0.468, rely=0.491, height=20
                , relwidth=0.304)
        self.password_entry.configure(background="white")
        self.password_entry.configure(disabledforeground="#a3a3a3")
        self.password_entry.configure(font="TkFixedFont")
        self.password_entry.configure(foreground="#000000")
        self.password_entry.configure(highlightbackground="#d9d9d9")
        self.password_entry.configure(highlightcolor="black")
        self.password_entry.configure(insertbackground="black")
        self.password_entry.configure(selectbackground="blue")
        self.password_entry.configure(selectforeground="white")

        self.branch_id_entry = tk.Entry(top)
        self.branch_id_entry.place(relx=0.468, rely=0.625, height=20
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


class BranchModify:
    def __init__(self, top=None):
        self.master = top
        top.geometry("327x253+556+102")
        top.minsize(120, 1)
        top.maxsize(1370, 749)
        top.resizable(0, 0)
        top.title("Modify")
        top.configure(background="#CED4DA")

        self.menubar = tk.Menu(top, font="TkMenuFont", bg="#d9d9d9", fg="#000000")

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

        self.back_button = tk.Button(top, command=self.select_back)
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

        self.modify_button = tk.Button(top,
                                       command=lambda: self.select_modify(self.Entry1_1.get(), self.Entry1_2.get()))
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

        global item_modifyBranch
        item_modifyBranch = tv.item(tv.focus())['values']
        print("PREVIOUSLY : ")
        print(item_modifyBranch[0])
        print(item_modifyBranch[1])
        self.Entry1.insert(0, item_modifyBranch[0])
        self.Entry1.config(state="disable")
        self.Entry2.insert(0, item_modifyBranch[1])
        self.Entry2.config(state="disable")

    def select_back(self):
        self.master.withdraw()

    def select_modify(self, branch_id, branch_name):
        try:
            sql_query = "UPDATE branch SET branch_id=" + str(self.Entry1_1.get()) + ", branch_name='" + str(
                self.Entry1_2.get()) + "' WHERE branch_id=" + str(item_modifyBranch[0]) + ";"
            try:
                mycursor.execute(sql_query)  # executing query
                tv.item(tv.focus(), text="", values=(str(self.Entry1_1.get()), self.Entry1_2.get()))
            except (mysql.connector.Error, mysql.connector.Warning) as e:  # fetching error
                messagebox.showerror(str(e))  # displaying error

        except:
            messagebox.showerror("showerror", "Modification failed")
        mydb.commit()
        self.master.withdraw()


class ExamModify:
    def __init__(self, top=None):
        top.geometry("327x602+562+80")
        top.minsize(120, 1)
        top.maxsize(1370, 749)
        top.resizable(0,0)
        top.title("Modify")
        top.configure(background="#CED4DA")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.present_label = tk.Label(top)
        self.present_label.place(relx=0.245, rely=0.017, height=19, width=154)
        self.present_label.configure(activebackground="#CED4DA")
        self.present_label.configure(activeforeground="black")
        self.present_label.configure(background="#CED4DA")
        self.present_label.configure(disabledforeground="#a3a3a3")
        self.present_label.configure(font="-family {Segoe UI} -size 13 -weight bold")
        self.present_label.configure(foreground="#212529")
        self.present_label.configure(highlightbackground="#d9d9d9")
        self.present_label.configure(highlightcolor="black")
        self.present_label.configure(text='''PRESENT DATA''')

        self.new_label = tk.Label(top)
        self.new_label.place(relx=0.306, rely=0.473, height=19, width=114)
        self.new_label.configure(activebackground="#f9f9f9")
        self.new_label.configure(activeforeground="black")
        self.new_label.configure(background="#CED4DA")
        self.new_label.configure(disabledforeground="#a3a3a3")
        self.new_label.configure(font="-family {Segoe UI} -size 13 -weight bold")
        self.new_label.configure(foreground="#212529")
        self.new_label.configure(highlightbackground="#d9d9d9")
        self.new_label.configure(highlightcolor="black")
        self.new_label.configure(text='''NEW DATA''')

        self.exam_label1 = tk.Label(top)
        self.exam_label1.place(relx=0.245, rely=0.066, height=19, width=55)
        self.exam_label1.configure(activebackground="#f9f9f9")
        self.exam_label1.configure(activeforeground="black")
        self.exam_label1.configure(background="#CED4DA")
        self.exam_label1.configure(disabledforeground="#a3a3a3")
        self.exam_label1.configure(foreground="#000000")
        self.exam_label1.configure(highlightbackground="#d9d9d9")
        self.exam_label1.configure(highlightcolor="black")
        self.exam_label1.configure(text='''Exam id :''')

        self.exam_entry1 = tk.Entry(top)
        self.exam_entry1.place(relx=0.459, rely=0.066, height=20, relwidth=0.318)
        self.exam_entry1.configure(background="white")
        self.exam_entry1.configure(disabledforeground="#a3a3a3")
        self.exam_entry1.configure(font="TkFixedFont")
        self.exam_entry1.configure(foreground="#000000")
        self.exam_entry1.configure(highlightbackground="#d9d9d9")
        self.exam_entry1.configure(highlightcolor="black")
        self.exam_entry1.configure(insertbackground="black")
        self.exam_entry1.configure(selectbackground="blue")
        self.exam_entry1.configure(selectforeground="white")

        self.name_label1 = tk.Label(top)
        self.name_label1.place(relx=0.275, rely=0.116, height=18, width=46)
        self.name_label1.configure(activebackground="#f9f9f9")
        self.name_label1.configure(activeforeground="black")
        self.name_label1.configure(background="#CED4DA")
        self.name_label1.configure(disabledforeground="#a3a3a3")
        self.name_label1.configure(foreground="#000000")
        self.name_label1.configure(highlightbackground="#d9d9d9")
        self.name_label1.configure(highlightcolor="black")
        self.name_label1.configure(text='''Name :''')

        self.name_entry1 = tk.Entry(top)
        self.name_entry1.place(relx=0.459, rely=0.116, height=20, relwidth=0.318)
        self.name_entry1.configure(background="white")
        self.name_entry1.configure(disabledforeground="#a3a3a3")
        self.name_entry1.configure(font="TkFixedFont")
        self.name_entry1.configure(foreground="#000000")
        self.name_entry1.configure(highlightbackground="#d9d9d9")
        self.name_entry1.configure(highlightcolor="black")
        self.name_entry1.configure(insertbackground="black")
        self.name_entry1.configure(selectbackground="blue")
        self.name_entry1.configure(selectforeground="white")

        self.duration_label1 = tk.Label(top)
        self.duration_label1.place(relx=0.239, rely=0.166, height=18, width=55)
        self.duration_label1.configure(activebackground="#f9f9f9")
        self.duration_label1.configure(activeforeground="black")
        self.duration_label1.configure(background="#CED4DA")
        self.duration_label1.configure(disabledforeground="#a3a3a3")
        self.duration_label1.configure(foreground="#000000")
        self.duration_label1.configure(highlightbackground="#d9d9d9")
        self.duration_label1.configure(highlightcolor="black")
        self.duration_label1.configure(text='''Duration :''')

        self.duration_entry1 = tk.Entry(top)
        self.duration_entry1.place(relx=0.459, rely=0.166, height=20, relwidth=0.318)
        self.duration_entry1.configure(background="white")
        self.duration_entry1.configure(disabledforeground="#a3a3a3")
        self.duration_entry1.configure(font="TkFixedFont")
        self.duration_entry1.configure(foreground="#000000")
        self.duration_entry1.configure(highlightbackground="#d9d9d9")
        self.duration_entry1.configure(highlightcolor="black")
        self.duration_entry1.configure(insertbackground="black")
        self.duration_entry1.configure(selectbackground="blue")
        self.duration_entry1.configure(selectforeground="white")

        self.date_label1 = tk.Label(top)
        self.date_label1.place(relx=0.275, rely=0.216, height=18, width=55)
        self.date_label1.configure(activebackground="#f9f9f9")
        self.date_label1.configure(activeforeground="black")
        self.date_label1.configure(background="#CED4DA")
        self.date_label1.configure(disabledforeground="#a3a3a3")
        self.date_label1.configure(foreground="#000000")
        self.date_label1.configure(highlightbackground="#d9d9d9")
        self.date_label1.configure(highlightcolor="black")
        self.date_label1.configure(text='''Date :''')

        self.date_entry1 = tk.Entry(top)
        self.date_entry1.place(relx=0.459, rely=0.216, height=20, relwidth=0.318)
        self.date_entry1.configure(background="white")
        self.date_entry1.configure(disabledforeground="#a3a3a3")
        self.date_entry1.configure(font="TkFixedFont")
        self.date_entry1.configure(foreground="#000000")
        self.date_entry1.configure(highlightbackground="#d9d9d9")
        self.date_entry1.configure(highlightcolor="black")
        self.date_entry1.configure(insertbackground="black")
        self.date_entry1.configure(selectbackground="blue")
        self.date_entry1.configure(selectforeground="white")

        self.ques_label1 = tk.Label(top)
        self.ques_label1.place(relx=0.135, rely=0.266, height=18, width=89)
        self.ques_label1.configure(activebackground="#f9f9f9")
        self.ques_label1.configure(activeforeground="black")
        self.ques_label1.configure(background="#CED4DA")
        self.ques_label1.configure(disabledforeground="#a3a3a3")
        self.ques_label1.configure(foreground="#000000")
        self.ques_label1.configure(highlightbackground="#d9d9d9")
        self.ques_label1.configure(highlightcolor="black")
        self.ques_label1.configure(text='''Total questions :''')

        self.ques_entry1 = tk.Entry(top)
        self.ques_entry1.place(relx=0.459, rely=0.266, height=20, relwidth=0.318)
        self.ques_entry1.configure(background="white")
        self.ques_entry1.configure(disabledforeground="#a3a3a3")
        self.ques_entry1.configure(font="TkFixedFont")
        self.ques_entry1.configure(foreground="#000000")
        self.ques_entry1.configure(highlightbackground="#d9d9d9")
        self.ques_entry1.configure(highlightcolor="black")
        self.ques_entry1.configure(insertbackground="black")
        self.ques_entry1.configure(selectbackground="blue")
        self.ques_entry1.configure(selectforeground="white")

        self.marks_label1 = tk.Label(top)
        self.marks_label1.place(relx=0.19, rely=0.316, height=17, width=75)
        self.marks_label1.configure(activebackground="#f9f9f9")
        self.marks_label1.configure(activeforeground="black")
        self.marks_label1.configure(background="#CED4DA")
        self.marks_label1.configure(disabledforeground="#a3a3a3")
        self.marks_label1.configure(foreground="#000000")
        self.marks_label1.configure(highlightbackground="#d9d9d9")
        self.marks_label1.configure(highlightcolor="black")
        self.marks_label1.configure(text='''Total marks :''')

        self.marks_entry1 = tk.Entry(top)
        self.marks_entry1.place(relx=0.459, rely=0.316, height=20, relwidth=0.318)
        self.marks_entry1.configure(background="white")
        self.marks_entry1.configure(disabledforeground="#a3a3a3")
        self.marks_entry1.configure(font="TkFixedFont")
        self.marks_entry1.configure(foreground="#000000")
        self.marks_entry1.configure(highlightbackground="#d9d9d9")
        self.marks_entry1.configure(highlightcolor="black")
        self.marks_entry1.configure(insertbackground="black")
        self.marks_entry1.configure(selectbackground="blue")
        self.marks_entry1.configure(selectforeground="white")

        self.branch_label1 = tk.Label(top)
        self.branch_label1.place(relx=0.22, rely=0.365, height=18, width=64)
        self.branch_label1.configure(activebackground="#f9f9f9")
        self.branch_label1.configure(activeforeground="black")
        self.branch_label1.configure(background="#CED4DA")
        self.branch_label1.configure(disabledforeground="#a3a3a3")
        self.branch_label1.configure(foreground="#000000")
        self.branch_label1.configure(highlightbackground="#d9d9d9")
        self.branch_label1.configure(highlightcolor="black")
        self.branch_label1.configure(text='''Branch id :''')

        self.branch_entry1 = tk.Entry(top)
        self.branch_entry1.place(relx=0.459, rely=0.365, height=20, relwidth=0.318)
        self.branch_entry1.configure(background="white")
        self.branch_entry1.configure(disabledforeground="#a3a3a3")
        self.branch_entry1.configure(font="TkFixedFont")
        self.branch_entry1.configure(foreground="#000000")
        self.branch_entry1.configure(highlightbackground="#d9d9d9")
        self.branch_entry1.configure(highlightcolor="black")
        self.branch_entry1.configure(insertbackground="black")
        self.branch_entry1.configure(selectbackground="blue")
        self.branch_entry1.configure(selectforeground="white")

        self.subject_label1 = tk.Label(top)
        self.subject_label1.place(relx=0.162, rely=0.415, height=18, width=80)
        self.subject_label1.configure(activebackground="#f9f9f9")
        self.subject_label1.configure(activeforeground="black")
        self.subject_label1.configure(background="#CED4DA")
        self.subject_label1.configure(disabledforeground="#a3a3a3")
        self.subject_label1.configure(foreground="#000000")
        self.subject_label1.configure(highlightbackground="#d9d9d9")
        self.subject_label1.configure(highlightcolor="black")
        self.subject_label1.configure(text='''Subject code :''')

        self.subject_entry1 = tk.Entry(top)
        self.subject_entry1.place(relx=0.459, rely=0.415, height=20, relwidth=0.318)
        self.subject_entry1.configure(background="white")
        self.subject_entry1.configure(disabledforeground="#a3a3a3")
        self.subject_entry1.configure(font="TkFixedFont")
        self.subject_entry1.configure(foreground="#000000")
        self.subject_entry1.configure(highlightbackground="#d9d9d9")
        self.subject_entry1.configure(highlightcolor="black")
        self.subject_entry1.configure(insertbackground="black")
        self.subject_entry1.configure(selectbackground="blue")
        self.subject_entry1.configure(selectforeground="white")

        self.exam_label2 = tk.Label(top)
        self.exam_label2.place(relx=0.245, rely=0.523, height=20, width=55)
        self.exam_label2.configure(activebackground="#f9f9f9")
        self.exam_label2.configure(activeforeground="black")
        self.exam_label2.configure(background="#CED4DA")
        self.exam_label2.configure(disabledforeground="#a3a3a3")
        self.exam_label2.configure(foreground="#000000")
        self.exam_label2.configure(highlightbackground="#d9d9d9")
        self.exam_label2.configure(highlightcolor="black")
        self.exam_label2.configure(text='''Exam id :''')

        self.exam_entry2 = tk.Entry(top)
        self.exam_entry2.place(relx=0.459, rely=0.523, height=20, relwidth=0.318)
        self.exam_entry2.configure(background="white")
        self.exam_entry2.configure(disabledforeground="#a3a3a3")
        self.exam_entry2.configure(font="TkFixedFont")
        self.exam_entry2.configure(foreground="#000000")
        self.exam_entry2.configure(highlightbackground="#d9d9d9")
        self.exam_entry2.configure(highlightcolor="black")
        self.exam_entry2.configure(insertbackground="black")
        self.exam_entry2.configure(selectbackground="blue")
        self.exam_entry2.configure(selectforeground="white")

        self.name_label2 = tk.Label(top)
        self.name_label2.place(relx=0.275, rely=0.573, height=18, width=46)
        self.name_label2.configure(activebackground="#f9f9f9")
        self.name_label2.configure(activeforeground="black")
        self.name_label2.configure(background="#CED4DA")
        self.name_label2.configure(disabledforeground="#a3a3a3")
        self.name_label2.configure(foreground="#000000")
        self.name_label2.configure(highlightbackground="#d9d9d9")
        self.name_label2.configure(highlightcolor="black")
        self.name_label2.configure(text='''Name :''')

        self.name_entry2 = tk.Entry(top)
        self.name_entry2.place(relx=0.459, rely=0.573, height=20, relwidth=0.318)
        self.name_entry2.configure(background="white")
        self.name_entry2.configure(disabledforeground="#a3a3a3")
        self.name_entry2.configure(font="TkFixedFont")
        self.name_entry2.configure(foreground="#000000")
        self.name_entry2.configure(highlightbackground="#d9d9d9")
        self.name_entry2.configure(highlightcolor="black")
        self.name_entry2.configure(insertbackground="black")
        self.name_entry2.configure(selectbackground="blue")
        self.name_entry2.configure(selectforeground="white")

        self.duration_label2 = tk.Label(top)
        self.duration_label2.place(relx=0.239, rely=0.623, height=18, width=55)
        self.duration_label2.configure(activebackground="#f9f9f9")
        self.duration_label2.configure(activeforeground="black")
        self.duration_label2.configure(background="#CED4DA")
        self.duration_label2.configure(disabledforeground="#a3a3a3")
        self.duration_label2.configure(foreground="#000000")
        self.duration_label2.configure(highlightbackground="#d9d9d9")
        self.duration_label2.configure(highlightcolor="black")
        self.duration_label2.configure(text='''Duration :''')

        self.duration_entry2 = tk.Entry(top)
        self.duration_entry2.place(relx=0.459, rely=0.623, height=20, relwidth=0.318)
        self.duration_entry2.configure(background="white")
        self.duration_entry2.configure(disabledforeground="#a3a3a3")
        self.duration_entry2.configure(font="TkFixedFont")
        self.duration_entry2.configure(foreground="#000000")
        self.duration_entry2.configure(highlightbackground="#d9d9d9")
        self.duration_entry2.configure(highlightcolor="black")
        self.duration_entry2.configure(insertbackground="black")
        self.duration_entry2.configure(selectbackground="blue")
        self.duration_entry2.configure(selectforeground="white")

        self.date_label2 = tk.Label(top)
        self.date_label2.place(relx=0.275, rely=0.673, height=18, width=55)
        self.date_label2.configure(activebackground="#f9f9f9")
        self.date_label2.configure(activeforeground="black")
        self.date_label2.configure(background="#CED4DA")
        self.date_label2.configure(disabledforeground="#a3a3a3")
        self.date_label2.configure(foreground="#000000")
        self.date_label2.configure(highlightbackground="#d9d9d9")
        self.date_label2.configure(highlightcolor="black")
        self.date_label2.configure(text='''Date :''')

        self.date_entry2 = tk.Entry(top)
        self.date_entry2.place(relx=0.459, rely=0.673, height=20, relwidth=0.318)
        self.date_entry2.configure(background="white")
        self.date_entry2.configure(disabledforeground="#a3a3a3")
        self.date_entry2.configure(font="TkFixedFont")
        self.date_entry2.configure(foreground="#000000")
        self.date_entry2.configure(highlightbackground="#d9d9d9")
        self.date_entry2.configure(highlightcolor="black")
        self.date_entry2.configure(insertbackground="black")
        self.date_entry2.configure(selectbackground="blue")
        self.date_entry2.configure(selectforeground="white")

        self.ques_label2 = tk.Label(top)
        self.ques_label2.place(relx=0.135, rely=0.723, height=18, width=89)
        self.ques_label2.configure(activebackground="#f9f9f9")
        self.ques_label2.configure(activeforeground="black")
        self.ques_label2.configure(background="#CED4DA")
        self.ques_label2.configure(disabledforeground="#a3a3a3")
        self.ques_label2.configure(foreground="#000000")
        self.ques_label2.configure(highlightbackground="#d9d9d9")
        self.ques_label2.configure(highlightcolor="black")
        self.ques_label2.configure(text='''Total questions :''')

        self.ques_entry2 = tk.Entry(top)
        self.ques_entry2.place(relx=0.459, rely=0.723, height=20, relwidth=0.318)
        self.ques_entry2.configure(background="white")
        self.ques_entry2.configure(disabledforeground="#a3a3a3")
        self.ques_entry2.configure(font="TkFixedFont")
        self.ques_entry2.configure(foreground="#000000")
        self.ques_entry2.configure(highlightbackground="#d9d9d9")
        self.ques_entry2.configure(highlightcolor="black")
        self.ques_entry2.configure(insertbackground="black")
        self.ques_entry2.configure(selectbackground="blue")
        self.ques_entry2.configure(selectforeground="white")

        self.marks_label2 = tk.Label(top)
        self.marks_label2.place(relx=0.19, rely=0.772, height=17, width=75)
        self.marks_label2.configure(activebackground="#f9f9f9")
        self.marks_label2.configure(activeforeground="black")
        self.marks_label2.configure(background="#CED4DA")
        self.marks_label2.configure(disabledforeground="#a3a3a3")
        self.marks_label2.configure(foreground="#000000")
        self.marks_label2.configure(highlightbackground="#d9d9d9")
        self.marks_label2.configure(highlightcolor="black")
        self.marks_label2.configure(text='''Total marks :''')

        self.marks_entry2 = tk.Entry(top)
        self.marks_entry2.place(relx=0.459, rely=0.772, height=20, relwidth=0.318)
        self.marks_entry2.configure(background="white")
        self.marks_entry2.configure(disabledforeground="#a3a3a3")
        self.marks_entry2.configure(font="TkFixedFont")
        self.marks_entry2.configure(foreground="#000000")
        self.marks_entry2.configure(highlightbackground="#d9d9d9")
        self.marks_entry2.configure(highlightcolor="black")
        self.marks_entry2.configure(insertbackground="black")
        self.marks_entry2.configure(selectbackground="blue")
        self.marks_entry2.configure(selectforeground="white")

        self.branch_label2 = tk.Label(top)
        self.branch_label2.place(relx=0.22, rely=0.822, height=18, width=64)
        self.branch_label2.configure(activebackground="#f9f9f9")
        self.branch_label2.configure(activeforeground="black")
        self.branch_label2.configure(background="#CED4DA")
        self.branch_label2.configure(disabledforeground="#a3a3a3")
        self.branch_label2.configure(foreground="#000000")
        self.branch_label2.configure(highlightbackground="#d9d9d9")
        self.branch_label2.configure(highlightcolor="black")
        self.branch_label2.configure(text='''Branch id :''')

        self.branch_entry2 = tk.Entry(top)
        self.branch_entry2.place(relx=0.459, rely=0.822, height=20, relwidth=0.318)
        self.branch_entry2.configure(background="white")
        self.branch_entry2.configure(disabledforeground="#a3a3a3")
        self.branch_entry2.configure(font="TkFixedFont")
        self.branch_entry2.configure(foreground="#000000")
        self.branch_entry2.configure(highlightbackground="#d9d9d9")
        self.branch_entry2.configure(highlightcolor="black")
        self.branch_entry2.configure(insertbackground="black")
        self.branch_entry2.configure(selectbackground="blue")
        self.branch_entry2.configure(selectforeground="white")

        self.subject_label2 = tk.Label(top)
        self.subject_label2.place(relx=0.168, rely=0.872, height=18, width=80)
        self.subject_label2.configure(activebackground="#f9f9f9")
        self.subject_label2.configure(activeforeground="black")
        self.subject_label2.configure(background="#CED4DA")
        self.subject_label2.configure(disabledforeground="#a3a3a3")
        self.subject_label2.configure(foreground="#000000")
        self.subject_label2.configure(highlightbackground="#d9d9d9")
        self.subject_label2.configure(highlightcolor="black")
        self.subject_label2.configure(text='''Subject code :''')

        self.subject_entry2 = tk.Entry(top)
        self.subject_entry2.place(relx=0.459, rely=0.872, height=20, relwidth=0.318)
        self.subject_entry2.configure(background="white")
        self.subject_entry2.configure(disabledforeground="#a3a3a3")
        self.subject_entry2.configure(font="TkFixedFont")
        self.subject_entry2.configure(foreground="#000000")
        self.subject_entry2.configure(highlightbackground="#d9d9d9")
        self.subject_entry2.configure(highlightcolor="black")
        self.subject_entry2.configure(insertbackground="black")
        self.subject_entry2.configure(selectbackground="blue")
        self.subject_entry2.configure(selectforeground="white")

        self.modify_button = tk.Button(top)
        self.modify_button.place(relx=0.642, rely=0.93, height=24, width=77)
        self.modify_button.configure(activebackground="#ececec")
        self.modify_button.configure(activeforeground="#000000")
        self.modify_button.configure(background="#E9ECEF")
        self.modify_button.configure(disabledforeground="#a3a3a3")
        self.modify_button.configure(foreground="#000000")
        self.modify_button.configure(highlightbackground="#d9d9d9")
        self.modify_button.configure(highlightcolor="black")
        self.modify_button.configure(pady="0")
        self.modify_button.configure(text='''Modify''')

        self.back_button = tk.Button(top)
        self.back_button.place(relx=0.135, rely=0.93, height=24, width=77)
        self.back_button.configure(activebackground="#ececec")
        self.back_button.configure(activeforeground="#000000")
        self.back_button.configure(background="#E9ECEF")
        self.back_button.configure(disabledforeground="#a3a3a3")
        self.back_button.configure(foreground="#000000")
        self.back_button.configure(highlightbackground="#d9d9d9")
        self.back_button.configure(highlightcolor="black")
        self.back_button.configure(pady="0")
        self.back_button.configure(text='''Back''')


class ResultModify:
    def __init__(self, top=None):
        top.geometry("327x430+589+46")
        top.minsize(120, 1)
        top.maxsize(1370, 749)
        top.resizable(1,  1)
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

        self.marks_label1 = tk.Label(top)
        self.marks_label1.place(relx=0.125, rely=0.167, height=12, width=95)
        self.marks_label1.configure(activebackground="#f9f9f9")
        self.marks_label1.configure(activeforeground="black")
        self.marks_label1.configure(background="#CED4DA")
        self.marks_label1.configure(disabledforeground="#a3a3a3")
        self.marks_label1.configure(foreground="#000000")
        self.marks_label1.configure(highlightbackground="#d9d9d9")
        self.marks_label1.configure(highlightcolor="black")
        self.marks_label1.configure(text='''Marks obtained :''')

        self.res_label1 = tk.Label(top)
        self.res_label1.place(relx=0.275, rely=0.24, height=13, width=46)
        self.res_label1.configure(activebackground="#f9f9f9")
        self.res_label1.configure(activeforeground="black")
        self.res_label1.configure(background="#CED4DA")
        self.res_label1.configure(disabledforeground="#a3a3a3")
        self.res_label1.configure(foreground="#000000")
        self.res_label1.configure(highlightbackground="#d9d9d9")
        self.res_label1.configure(highlightcolor="black")
        self.res_label1.configure(text='''Result :''')

        self.res_id_label1 = tk.Label(top)
        self.res_id_label1.place(relx=0.245, rely=0.098, height=14, width=55)
        self.res_id_label1.configure(activebackground="#f9f9f9")
        self.res_id_label1.configure(activeforeground="black")
        self.res_id_label1.configure(background="#CED4DA")
        self.res_id_label1.configure(disabledforeground="#a3a3a3")
        self.res_id_label1.configure(foreground="#000000")
        self.res_id_label1.configure(highlightbackground="#d9d9d9")
        self.res_id_label1.configure(highlightcolor="black")
        self.res_id_label1.configure(text='''Result id :''')

        self.exam_id_label = tk.Label(top)
        self.exam_id_label.place(relx=0.239, rely=0.381, height=13, width=60)
        self.exam_id_label.configure(activebackground="#f9f9f9")
        self.exam_id_label.configure(activeforeground="black")
        self.exam_id_label.configure(background="#CED4DA")
        self.exam_id_label.configure(disabledforeground="#a3a3a3")
        self.exam_id_label.configure(foreground="#000000")
        self.exam_id_label.configure(highlightbackground="#d9d9d9")
        self.exam_id_label.configure(highlightcolor="black")
        self.exam_id_label.configure(text='''Exam id :''')

        self.student_id_label1 = tk.Label(top)
        self.student_id_label1.place(relx=0.214, rely=0.312, height=13, width=64)

        self.student_id_label1.configure(activebackground="#f9f9f9")
        self.student_id_label1.configure(activeforeground="black")
        self.student_id_label1.configure(background="#CED4DA")
        self.student_id_label1.configure(disabledforeground="#a3a3a3")
        self.student_id_label1.configure(foreground="#000000")
        self.student_id_label1.configure(highlightbackground="#d9d9d9")
        self.student_id_label1.configure(highlightcolor="black")
        self.student_id_label1.configure(text='''Student id :''')

        self.res_id_entry1 = tk.Entry(top)
        self.res_id_entry1.place(relx=0.459, rely=0.093, height=20
                , relwidth=0.318)
        self.res_id_entry1.configure(background="white")
        self.res_id_entry1.configure(disabledforeground="#a3a3a3")
        self.res_id_entry1.configure(font="TkFixedFont")
        self.res_id_entry1.configure(foreground="#000000")
        self.res_id_entry1.configure(highlightbackground="#d9d9d9")
        self.res_id_entry1.configure(highlightcolor="black")
        self.res_id_entry1.configure(insertbackground="black")
        self.res_id_entry1.configure(selectbackground="blue")
        self.res_id_entry1.configure(selectforeground="white")

        self.marks_entry1 = tk.Entry(top)
        self.marks_entry1.place(relx=0.459, rely=0.163, height=20
                , relwidth=0.318)
        self.marks_entry1.configure(background="white")
        self.marks_entry1.configure(disabledforeground="#a3a3a3")
        self.marks_entry1.configure(font="TkFixedFont")
        self.marks_entry1.configure(foreground="#000000")
        self.marks_entry1.configure(highlightbackground="#d9d9d9")
        self.marks_entry1.configure(highlightcolor="black")
        self.marks_entry1.configure(insertbackground="black")
        self.marks_entry1.configure(selectbackground="blue")
        self.marks_entry1.configure(selectforeground="white")

        self.res_entry1 = tk.Entry(top)
        self.res_entry1.place(relx=0.459, rely=0.233, height=20, relwidth=0.318)
        self.res_entry1.configure(background="white")
        self.res_entry1.configure(disabledforeground="#a3a3a3")
        self.res_entry1.configure(font="TkFixedFont")
        self.res_entry1.configure(foreground="#000000")
        self.res_entry1.configure(highlightbackground="#d9d9d9")
        self.res_entry1.configure(highlightcolor="black")
        self.res_entry1.configure(insertbackground="black")
        self.res_entry1.configure(selectbackground="blue")
        self.res_entry1.configure(selectforeground="white")

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

        self.res_id_entry2 = tk.Entry(top)
        self.res_id_entry2.place(relx=0.459, rely=0.535, height=20
                , relwidth=0.318)
        self.res_id_entry2.configure(background="white")
        self.res_id_entry2.configure(disabledforeground="#a3a3a3")
        self.res_id_entry2.configure(font="TkFixedFont")
        self.res_id_entry2.configure(foreground="#000000")
        self.res_id_entry2.configure(highlightbackground="#d9d9d9")
        self.res_id_entry2.configure(highlightcolor="black")
        self.res_id_entry2.configure(insertbackground="black")
        self.res_id_entry2.configure(selectbackground="blue")
        self.res_id_entry2.configure(selectforeground="white")

        self.marks_entry2 = tk.Entry(top)
        self.marks_entry2.place(relx=0.459, rely=0.605, height=20
                , relwidth=0.318)
        self.marks_entry2.configure(background="white")
        self.marks_entry2.configure(disabledforeground="#a3a3a3")
        self.marks_entry2.configure(font="TkFixedFont")
        self.marks_entry2.configure(foreground="#000000")
        self.marks_entry2.configure(highlightbackground="#d9d9d9")
        self.marks_entry2.configure(highlightcolor="black")
        self.marks_entry2.configure(insertbackground="black")
        self.marks_entry2.configure(selectbackground="blue")
        self.marks_entry2.configure(selectforeground="white")

        self.res_entry2 = tk.Entry(top)
        self.res_entry2.place(relx=0.459, rely=0.674, height=20, relwidth=0.318)
        self.res_entry2.configure(background="white")
        self.res_entry2.configure(disabledforeground="#a3a3a3")
        self.res_entry2.configure(font="TkFixedFont")
        self.res_entry2.configure(foreground="#000000")
        self.res_entry2.configure(highlightbackground="#d9d9d9")
        self.res_entry2.configure(highlightcolor="black")
        self.res_entry2.configure(insertbackground="black")
        self.res_entry2.configure(selectbackground="blue")
        self.res_entry2.configure(selectforeground="white")

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

        self.Entry1_7 = tk.Entry(top)
        self.Entry1_7.place(relx=2.875, rely=1.828, height=20, relwidth=0.318)
        self.Entry1_7.configure(background="white")
        self.Entry1_7.configure(disabledforeground="#a3a3a3")
        self.Entry1_7.configure(font="TkFixedFont")
        self.Entry1_7.configure(foreground="#000000")
        self.Entry1_7.configure(highlightbackground="#d9d9d9")
        self.Entry1_7.configure(highlightcolor="black")
        self.Entry1_7.configure(insertbackground="black")
        self.Entry1_7.configure(selectbackground="blue")
        self.Entry1_7.configure(selectforeground="white")

        self.res_id_label2 = tk.Label(top)
        self.res_id_label2.place(relx=0.245, rely=0.54, height=14, width=55)
        self.res_id_label2.configure(activebackground="#f9f9f9")
        self.res_id_label2.configure(activeforeground="black")
        self.res_id_label2.configure(background="#CED4DA")
        self.res_id_label2.configure(disabledforeground="#a3a3a3")
        self.res_id_label2.configure(foreground="#000000")
        self.res_id_label2.configure(highlightbackground="#d9d9d9")
        self.res_id_label2.configure(highlightcolor="black")
        self.res_id_label2.configure(text='''Result id :''')

        self.marks_label2 = tk.Label(top)
        self.marks_label2.place(relx=0.128, rely=0.609, height=13, width=96)
        self.marks_label2.configure(activebackground="#f9f9f9")
        self.marks_label2.configure(activeforeground="black")
        self.marks_label2.configure(background="#CED4DA")
        self.marks_label2.configure(disabledforeground="#a3a3a3")
        self.marks_label2.configure(foreground="#000000")
        self.marks_label2.configure(highlightbackground="#d9d9d9")
        self.marks_label2.configure(highlightcolor="black")
        self.marks_label2.configure(text='''Marks obtained :''')

        self.res_label2 = tk.Label(top)
        self.res_label2.place(relx=0.269, rely=0.681, height=12, width=55)
        self.res_label2.configure(activebackground="#f9f9f9")
        self.res_label2.configure(activeforeground="black")
        self.res_label2.configure(background="#CED4DA")
        self.res_label2.configure(disabledforeground="#a3a3a3")
        self.res_label2.configure(foreground="#000000")
        self.res_label2.configure(highlightbackground="#d9d9d9")
        self.res_label2.configure(highlightcolor="black")
        self.res_label2.configure(text='''Result :''')

        self.student_id_label2 = tk.Label(top)
        self.student_id_label2.place(relx=0.22, rely=0.753, height=13, width=64)
        self.student_id_label2.configure(activebackground="#f9f9f9")
        self.student_id_label2.configure(activeforeground="black")
        self.student_id_label2.configure(background="#CED4DA")
        self.student_id_label2.configure(disabledforeground="#a3a3a3")
        self.student_id_label2.configure(foreground="#000000")
        self.student_id_label2.configure(highlightbackground="#d9d9d9")
        self.student_id_label2.configure(highlightcolor="black")
        self.student_id_label2.configure(text='''Student id :''')

        self.exam_id_label2 = tk.Label(top)
        self.exam_id_label2.place(relx=0.226, rely=0.823, height=13, width=70)
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


class SubjectModify:
    def __init__(self, top=None):
        top.geometry("327x370+455+152")
        top.minsize(120, 1)
        top.maxsize(1370, 749)
        top.resizable(0,0)
        top.title("Modify")
        top.configure(background="#CED4DA")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.245, rely=0.027, height=22, width=154)
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
        self.Label1_1.place(relx=0.306, rely=0.432, height=22, width=114)
        self.Label1_1.configure(activebackground="#f9f9f9")
        self.Label1_1.configure(activeforeground="black")
        self.Label1_1.configure(background="#CED4DA")
        self.Label1_1.configure(disabledforeground="#a3a3a3")
        self.Label1_1.configure(font="-family {Segoe UI} -size 13 -weight bold")
        self.Label1_1.configure(foreground="#212529")
        self.Label1_1.configure(highlightbackground="#d9d9d9")
        self.Label1_1.configure(highlightcolor="black")
        self.Label1_1.configure(text='''NEW DATA''')

        self.name_label1 = tk.Label(top)
        self.name_label1.place(relx=0.122, rely=0.189, height=19, width=95)
        self.name_label1.configure(activebackground="#f9f9f9")
        self.name_label1.configure(activeforeground="black")
        self.name_label1.configure(background="#CED4DA")
        self.name_label1.configure(disabledforeground="#a3a3a3")
        self.name_label1.configure(foreground="#000000")
        self.name_label1.configure(highlightbackground="#d9d9d9")
        self.name_label1.configure(highlightcolor="black")
        self.name_label1.configure(text='''Subject name :''')

        self.credit_label1 = tk.Label(top)
        self.credit_label1.place(relx=0.135, rely=0.27, height=20, width=86)
        self.credit_label1.configure(activebackground="#f9f9f9")
        self.credit_label1.configure(activeforeground="black")
        self.credit_label1.configure(background="#CED4DA")
        self.credit_label1.configure(disabledforeground="#a3a3a3")
        self.credit_label1.configure(foreground="#000000")
        self.credit_label1.configure(highlightbackground="#d9d9d9")
        self.credit_label1.configure(highlightcolor="black")
        self.credit_label1.configure(text='''Subject credit :''')

        self.code_label1 = tk.Label(top)
        self.code_label1.place(relx=0.128, rely=0.103, height=22, width=95)
        self.code_label1.configure(activebackground="#f9f9f9")
        self.code_label1.configure(activeforeground="black")
        self.code_label1.configure(background="#CED4DA")
        self.code_label1.configure(disabledforeground="#a3a3a3")
        self.code_label1.configure(foreground="#000000")
        self.code_label1.configure(highlightbackground="#d9d9d9")
        self.code_label1.configure(highlightcolor="black")
        self.code_label1.configure(text='''Subject code :''')

        self.branch_id_label1 = tk.Label(top)
        self.branch_id_label1.place(relx=0.183, rely=0.362, height=11, width=74)
        self.branch_id_label1.configure(activebackground="#f9f9f9")
        self.branch_id_label1.configure(activeforeground="black")
        self.branch_id_label1.configure(background="#CED4DA")
        self.branch_id_label1.configure(disabledforeground="#a3a3a3")
        self.branch_id_label1.configure(foreground="#000000")
        self.branch_id_label1.configure(highlightbackground="#d9d9d9")
        self.branch_id_label1.configure(highlightcolor="black")
        self.branch_id_label1.configure(text='''Branch id :''')

        self.code_entry1 = tk.Entry(top)
        self.code_entry1.place(relx=0.459, rely=0.108, height=20, relwidth=0.318)

        self.code_entry1.configure(background="white")
        self.code_entry1.configure(disabledforeground="#a3a3a3")
        self.code_entry1.configure(font="TkFixedFont")
        self.code_entry1.configure(foreground="#000000")
        self.code_entry1.configure(highlightbackground="#d9d9d9")
        self.code_entry1.configure(highlightcolor="black")
        self.code_entry1.configure(insertbackground="black")
        self.code_entry1.configure(selectbackground="blue")
        self.code_entry1.configure(selectforeground="white")

        self.name_entry1 = tk.Entry(top)
        self.name_entry1.place(relx=0.459, rely=0.189, height=20, relwidth=0.318)

        self.name_entry1.configure(background="white")
        self.name_entry1.configure(disabledforeground="#a3a3a3")
        self.name_entry1.configure(font="TkFixedFont")
        self.name_entry1.configure(foreground="#000000")
        self.name_entry1.configure(highlightbackground="#d9d9d9")
        self.name_entry1.configure(highlightcolor="black")
        self.name_entry1.configure(insertbackground="black")
        self.name_entry1.configure(selectbackground="blue")
        self.name_entry1.configure(selectforeground="white")

        self.credit_entry1 = tk.Entry(top)
        self.credit_entry1.place(relx=0.459, rely=0.27, height=20
                , relwidth=0.318)
        self.credit_entry1.configure(background="white")
        self.credit_entry1.configure(disabledforeground="#a3a3a3")
        self.credit_entry1.configure(font="TkFixedFont")
        self.credit_entry1.configure(foreground="#000000")
        self.credit_entry1.configure(highlightbackground="#d9d9d9")
        self.credit_entry1.configure(highlightcolor="black")
        self.credit_entry1.configure(insertbackground="black")
        self.credit_entry1.configure(selectbackground="blue")
        self.credit_entry1.configure(selectforeground="white")

        self.branch_id_entry1 = tk.Entry(top)
        self.branch_id_entry1.place(relx=0.459, rely=0.351, height=20
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

        self.code_entry2 = tk.Entry(top)
        self.code_entry2.place(relx=0.459, rely=0.514, height=20, relwidth=0.318)

        self.code_entry2.configure(background="white")
        self.code_entry2.configure(disabledforeground="#a3a3a3")
        self.code_entry2.configure(font="TkFixedFont")
        self.code_entry2.configure(foreground="#000000")
        self.code_entry2.configure(highlightbackground="#d9d9d9")
        self.code_entry2.configure(highlightcolor="black")
        self.code_entry2.configure(insertbackground="black")
        self.code_entry2.configure(selectbackground="blue")
        self.code_entry2.configure(selectforeground="white")

        self.name_entry2 = tk.Entry(top)
        self.name_entry2.place(relx=0.459, rely=0.595, height=20, relwidth=0.318)

        self.name_entry2.configure(background="white")
        self.name_entry2.configure(disabledforeground="#a3a3a3")
        self.name_entry2.configure(font="TkFixedFont")
        self.name_entry2.configure(foreground="#000000")
        self.name_entry2.configure(highlightbackground="#d9d9d9")
        self.name_entry2.configure(highlightcolor="black")
        self.name_entry2.configure(insertbackground="black")
        self.name_entry2.configure(selectbackground="blue")
        self.name_entry2.configure(selectforeground="white")

        self.credit_entry2 = tk.Entry(top)
        self.credit_entry2.place(relx=0.459, rely=0.676, height=20
                , relwidth=0.318)
        self.credit_entry2.configure(background="white")
        self.credit_entry2.configure(disabledforeground="#a3a3a3")
        self.credit_entry2.configure(font="TkFixedFont")
        self.credit_entry2.configure(foreground="#000000")
        self.credit_entry2.configure(highlightbackground="#d9d9d9")
        self.credit_entry2.configure(highlightcolor="black")
        self.credit_entry2.configure(insertbackground="black")
        self.credit_entry2.configure(selectbackground="blue")
        self.credit_entry2.configure(selectforeground="white")

        self.branch_id_entry2 = tk.Entry(top)
        self.branch_id_entry2.place(relx=0.459, rely=0.757, height=20
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

        self.code_label2 = tk.Label(top)
        self.code_label2.place(relx=0.153, rely=0.514, height=22, width=85)
        self.code_label2.configure(activebackground="#f9f9f9")
        self.code_label2.configure(activeforeground="black")
        self.code_label2.configure(background="#CED4DA")
        self.code_label2.configure(disabledforeground="#a3a3a3")
        self.code_label2.configure(foreground="#000000")
        self.code_label2.configure(highlightbackground="#d9d9d9")
        self.code_label2.configure(highlightcolor="black")
        self.code_label2.configure(text='''Subject code :''')

        self.name_label2 = tk.Label(top)
        self.name_label2.place(relx=0.147, rely=0.595, height=20, width=86)
        self.name_label2.configure(activebackground="#f9f9f9")
        self.name_label2.configure(activeforeground="black")
        self.name_label2.configure(background="#CED4DA")
        self.name_label2.configure(disabledforeground="#a3a3a3")
        self.name_label2.configure(foreground="#000000")
        self.name_label2.configure(highlightbackground="#d9d9d9")
        self.name_label2.configure(highlightcolor="black")
        self.name_label2.configure(text='''Subject name :''')

        self.credit_label2 = tk.Label(top)
        self.credit_label2.place(relx=0.15, rely=0.673, height=19, width=85)
        self.credit_label2.configure(activebackground="#f9f9f9")
        self.credit_label2.configure(activeforeground="black")
        self.credit_label2.configure(background="#CED4DA")
        self.credit_label2.configure(disabledforeground="#a3a3a3")
        self.credit_label2.configure(foreground="#000000")
        self.credit_label2.configure(highlightbackground="#d9d9d9")
        self.credit_label2.configure(highlightcolor="black")
        self.credit_label2.configure(text='''Subject credit :''')

        self.branch_id_label2 = tk.Label(top)
        self.branch_id_label2.place(relx=0.214, rely=0.768, height=11, width=64)
        self.branch_id_label2.configure(activebackground="#f9f9f9")
        self.branch_id_label2.configure(activeforeground="black")
        self.branch_id_label2.configure(background="#CED4DA")
        self.branch_id_label2.configure(disabledforeground="#a3a3a3")
        self.branch_id_label2.configure(foreground="#000000")
        self.branch_id_label2.configure(highlightbackground="#d9d9d9")
        self.branch_id_label2.configure(highlightcolor="black")
        self.branch_id_label2.configure(text='''Branch id :''')

        self.modify_button = tk.Button(top)
        self.modify_button.place(relx=0.612, rely=0.865, height=24, width=77)
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
        self.cancel_button.place(relx=0.183, rely=0.865, height=24, width=77)
        self.cancel_button.configure(activebackground="#ececec")
        self.cancel_button.configure(activeforeground="#000000")
        self.cancel_button.configure(background="#E9ECEF")
        self.cancel_button.configure(disabledforeground="#a3a3a3")
        self.cancel_button.configure(foreground="#000000")
        self.cancel_button.configure(highlightbackground="#d9d9d9")
        self.cancel_button.configure(highlightcolor="black")
        self.cancel_button.configure(pady="0")
        self.cancel_button.configure(text='''Cancel''')


class MainScreen:
    def __init__(self, top=None):
        self.master = top
        top.geometry("600x450+383+106")
        top.minsize(120, 1)
        top.maxsize(1370, 749)
        top.resizable(1, 1)
        top.title("Exam Management System")
        top.configure(background="#212529")

        self.Canvas = tk.Canvas(top)
        self.Canvas.place(relx=0.117, rely=0.178, relheight=0.607, relwidth=0.772)
        self.Canvas.configure(background="#f8f9fa")
        self.Canvas.configure(insertbackground="black")
        self.Canvas.configure(relief="ridge")
        self.Canvas.configure(selectbackground="blue")
        self.Canvas.configure(selectforeground="white")

        self.student_button = tk.Button(self.Canvas, command=self.select_student)
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

        self.exam_button = tk.Button(self.Canvas, command=self.select_exam)
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

        self.subject_button = tk.Button(self.Canvas, command=self.select_subject)
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

        self.result_button = tk.Button(self.Canvas, command=self.select_result)
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

        self.attendance_button = tk.Button(self.Canvas, command=self.select_attendance)
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

        self.branch_button = tk.Button(self.Canvas, command=self.select_branch)
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

        self.custom_query_button = tk.Button(self.Canvas, command=self.select_custom_query)
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

    def select_student(self):
        self.master.withdraw()
        Student(Toplevel(self.master))

    def select_exam(self):
        self.master.withdraw()
        Exam(Toplevel(self.master))

    def select_subject(self):
        self.master.withdraw()
        Subject(Toplevel(self.master))

    def select_result(self):
        self.master.withdraw()
        Result(Toplevel(self.master))

    def select_attendance(self):
        self.master.withdraw()
        Attendance(Toplevel(self.master))

    def select_branch(self):
        self.master.withdraw()
        Branch(Toplevel(self.master))

    def select_custom_query(self):
        self.master.withdraw()
        CustomQuery(Toplevel(self.master))



root = tk.Tk()
top = MainScreen(root)
root.mainloop()

# Tkinter GUI code ends
