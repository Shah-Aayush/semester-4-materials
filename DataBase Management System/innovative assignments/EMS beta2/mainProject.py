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
    
    #python backend starts
    
def display_table(choice):          #1=student; 2=exam; 3=subject; 4=result; 5=attendance; 6=branch
    if choice==1:
        mycursor.execute("select * from student")
        data = mycursor.fetchall()
        return data 
    elif choice==2:
        mycursor.execute("select * from exam")
        data = mycursor.fetchall()
        return data
    elif choice==3:
        mycursor.execute("select * from subject")
        data = mycursor.fetchall()
        return data
    elif choice==4:
        mycursor.execute("select * from result")
        data = mycursor.fetchall()
        return data
    elif choice==5:
        mycursor.execute("select * from attendance")
        data = mycursor.fetchall()
        return data
    elif choice==6:
        mycursor.execute("select * from branch")#        Error.setMessage(self, message_shown="Cannot fetch data!")
        
        data = mycursor.fetchall()
        return data
    else:
        #        Error(Toplevel(self.master))
        return "Cannot fetch data!"
    
    
    
    #python backend ends
    
    
    #Tkinter GUI code starts
    
class Student:
    def __init__(self, top=None):
        self.master=top
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
        count = 0
        for i in range(20):
            self.tv.insert(parent='', index="end", iid=count, text="Parent" + str(count),
                values=("Col1" + str(count), "Col2" + str(count), "Col3" + str(count)))
            count += 1
            
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
        
        
class Exam:
    def __init__(self, top=None):
        self.master=top
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
            command = self.back)
        
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
            command = self.back)
        
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
            command = self.back)
        
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
            command = self.back)
        
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
        tv.column("#0", width=0,stretch="NO")
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
            command = self.back)

        #real data
        mycursor.execute("SELECT * from branch;")
        output = mycursor.fetchall()
        
        for list_item in output:
            tv.insert(parent='', index="end", text="Parent", values=(str(list_item[0]), str(list_item[1])))
        
        #sample data
#        count = 0
#        for i in range(20):
#            tv.insert(parent='', index="end", iid=count, text="Parent" + str(count), values=("Col1 long long long long long long long long long long long text" + str(count), "Col2 such a long freaking text" + str(count)))
#            count += 1
        
    def back(self):
        self.master.withdraw()
        MainScreen(Toplevel(self.master))
    
    def select_modify(self):
        if(tv.focus() != ""):
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
                mycursor.execute(sql_query)                                     #executing query
            except (mysql.connector.Error, mysql.connector.Warning) as e:       #fetching error
                messagebox.showerror(str(e))                                    #displaying error
            
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
        self.style.configure('.',background="#d9d9d9")
        self.style.configure('.',foreground="#000000")
        self.style.map('.',background=[('selected', "#d9d9d9"), ('active',"#ececec")])
        
        top.geometry("705x450+373+129")
        top.minsize(120, 1)
        top.maxsize(1370, 749)
        top.resizable(1,  1)
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
        sql_query = self.Entry1.get()                                       #getting text from entry
        try:
            mycursor.execute(sql_query)                                     #executing query
            self.display_output(mycursor.fetchall(),1)                        #displaying output
        except (mysql.connector.Error, mysql.connector.Warning) as e:       #fetching error
            self.display_output("ERROR MESSAGE : \n" + str(e),2)              #displaying error
        mydb.commit()
    
    def select_clear(self):
        Scrolledtext1.config(state="normal")
        self.Entry1.delete(0, 'end')
        Scrolledtext1.delete("1.0", "end")
        Scrolledtext1.config(state="disable")
        
    def display_output(self,output_message,choice):
    
        Scrolledtext1.config(state="normal")        # changing text box's state so that we can edit it
        Scrolledtext1.delete("1.0", "end")          # deletes previous contents
        
        if choice==1:       #select statement
            myTable = PrettyTable()
            for list_item in output_message:
                myTable.add_row(list_item)
            print(myTable)
            Scrolledtext1.insert(1.0,myTable)           # showing output message
            
        else:               #not select  statement
            print(output_message)
            Scrolledtext1.insert(1.0,output_message)           # showing output message
        Scrolledtext1.config(state="disable")       # disabling text box's state so that user cannot change it's content
        
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
            
            
class MainScreen:
    def __init__(self, top=None):
        self.master = top
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

class BranchModify:
    def __init__(self, top=None):
        self.master = top
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
        
        self.modify_button = tk.Button(top, command= lambda:self.select_modify(self.Entry1_1.get(), self.Entry1_2.get()))
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
        self.Entry1.insert(0,item_modifyBranch[0])
        self.Entry1.config(state="disable")
        self.Entry2.insert(0,item_modifyBranch[1])
        self.Entry2.config(state="disable")
    
    def select_back(self):
        self.master.withdraw()
    
    def select_modify(self,branch_id,branch_name):
        try:
            sql_query = "UPDATE branch SET branch_id=" + str(self.Entry1_1.get()) + ", branch_name='" + str(self.Entry1_2.get()) + "' WHERE branch_id=" + str(item_modifyBranch[0]) + ";"
            try:
                mycursor.execute(sql_query)                                     #executing query
                tv.item(tv.focus(), text="", values=(str(self.Entry1_1.get()),self.Entry1_2.get()))
            except (mysql.connector.Error, mysql.connector.Warning) as e:       #fetching error
                messagebox.showerror(str(e))                                    #displaying error
            
        except:
            messagebox.showerror("showerror", "Modification failed")
        mydb.commit()
        self.master.withdraw()

class BranchAdd:
    def __init__(self, top=None):
        self.master = top
        top.geometry("342x139+527+141")
        top.minsize(120, 1)
        top.maxsize(1370, 749)
        top.resizable(1,  1)
        top.title("Add")
        top.configure(background="#d9d9d9")
        
        self.id_label = tk.Label(top)
        self.id_label.place(relx=0.234, rely=0.144, height=17, width=74)
        self.id_label.configure(background="#d9d9d9")
        self.id_label.configure(disabledforeground="#a3a3a3")
        self.id_label.configure(foreground="#000000")
        self.id_label.configure(text='''Branch id :''')
        
        self.name_label = tk.Label(top)
        self.name_label.place(relx=0.187, rely=0.36, height=17, width=84)
        self.name_label.configure(background="#d9d9d9")
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
        self.back_button.configure(background="#d9d9d9")
        self.back_button.configure(disabledforeground="#a3a3a3")
        self.back_button.configure(foreground="#000000")
        self.back_button.configure(highlightbackground="#d9d9d9")
        self.back_button.configure(highlightcolor="black")
        self.back_button.configure(pady="0")
        self.back_button.configure(text='''Back''')
        
        self.add_button = tk.Button(top, command= lambda :self.select_add(self.id_entry.get(),self.name_entry.get()))
        self.add_button.place(relx=0.594, rely=0.647, height=24, width=87)
        self.add_button.configure(activebackground="#ececec")
        self.add_button.configure(activeforeground="#000000")
        self.add_button.configure(background="#d9d9d9")
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
    
root = tk.Tk()
top = MainScreen(root)
root.mainloop()

#Tkinter GUI code ends