import sys
import tkinter as tk
from tkinter import *
import mysql.connector

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
        mycursor.execute("select * from branch")
        data = mycursor.fetchall()
        return data
    else:
#        Error(Toplevel(self.master))
#        Error.setMessage(self, message_shown="Cannot fetch data!")
        return "Cannot fetch data!"
    

    
    #python backend ends
    
    
    #Tkinter GUI code starts
    
class Student:
    def __init__(self, top=None):
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
        top.resizable(0,0)
        top.title("Student ")
        top.configure(background="#212529")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")
        
        self.Canvas1 = tk.Canvas(top)
        self.Canvas1.place(relx=0.067, rely=0.111, relheight=0.74
            , relwidth=0.872)
        self.Canvas1.configure(background="white")
        self.Canvas1.configure(insertbackground="black")
        self.Canvas1.configure(relief="ridge")
        self.Canvas1.configure(selectbackground="blue")
        self.Canvas1.configure(selectforeground="white")
        
        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.367, rely=0.022, height=31, width=174)
        self.Label1.configure(background="#212529", font="-family {Segoe UI} -size 13 -weight bold",
            foreground="#ffffff", text='''Student Table''')
        
        self.style.configure('Treeview', font="TkDefaultFont")
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
        self.add_button.place(relx=0.096, rely=0.811, height=20, width=89)
        self.add_button.configure(activebackground="#ececec", activeforeground="#000000", background="#3F454C",
            borderwidth="0", disabledforeground="#a3a3a3", font="-family {Segoe UI} -size 9 "
            "-weight bold",
            foreground="white", highlightbackground="#d9d9d9", highlightcolor="black",
            pady="0", text='''Add''')
        
        self.delete_button = tk.Button(self.Canvas1)
        self.delete_button.place(relx=0.421, rely=0.811, height=20, width=86)
        self.delete_button.configure(activebackground="#ececec", activeforeground="#000000", background="#3F454C",
            borderwidth="0", disabledforeground="#a3a3a3", font="-family {Segoe UI} -size 9 "
            "-weight bold",
            foreground="white", highlightbackground="#d9d9d9", highlightcolor="black",
            text="Delete")
        
        self.modify_button = tk.Button(self.Canvas1)
        self.modify_button.place(relx=0.746, rely=0.811, height=20, width=86)
        self.modify_button.configure(activebackground="#ececec", activeforeground="#000000", background="#3F454C",
            borderwidth="0", disabledforeground="#a3a3a3",
            font="-family {Segoe UI} -size 9 -weight bold",
            foreground="white", highlightbackground="#d9d9d9", highlightcolor="black",
            text='''Modify''')
        
        
class Exam:
    def __init__(self, top=None):
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
        top.title("Exam ")
        top.configure(background="#212529")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")
        
        self.Canvas1 = tk.Canvas(top)
        self.Canvas1.place(relx=0.067, rely=0.111, relheight=0.74
            , relwidth=0.872)
        self.Canvas1.configure(background="white")
        self.Canvas1.configure(insertbackground="black")
        self.Canvas1.configure(relief="ridge")
        self.Canvas1.configure(selectbackground="blue")
        self.Canvas1.configure(selectforeground="white")
        
        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.367, rely=0.022, height=31, width=174)
        self.Label1.configure(background="#212529", font="-family {Segoe UI} -size 13 -weight bold",
            foreground="#ffffff", text='''Exam Table''')
        
        self.style.configure('Treeview', font="TkDefaultFont")
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
        self.add_button.place(relx=0.096, rely=0.811, height=20, width=89)
        self.add_button.configure(activebackground="#ececec", activeforeground="#000000", background="#3F454C",
            borderwidth="0", disabledforeground="#a3a3a3", font="-family {Segoe UI} -size 9 "
            "-weight bold",
            foreground="white", highlightbackground="#d9d9d9", highlightcolor="black",
            pady="0", text='''Add''')
        
        self.delete_button = tk.Button(self.Canvas1)
        self.delete_button.place(relx=0.421, rely=0.811, height=20, width=86)
        self.delete_button.configure(activebackground="#ececec", activeforeground="#000000", background="#3F454C",
            borderwidth="0", disabledforeground="#a3a3a3", font="-family {Segoe UI} -size 9 "
            "-weight bold",
            foreground="white", highlightbackground="#d9d9d9", highlightcolor="black",
            text="Delete")
        
        self.modify_button = tk.Button(self.Canvas1)
        self.modify_button.place(relx=0.746, rely=0.811, height=20, width=86)
        self.modify_button.configure(activebackground="#ececec", activeforeground="#000000", background="#3F454C",
            borderwidth="0", disabledforeground="#a3a3a3",
            font="-family {Segoe UI} -size 9 -weight bold",
            foreground="white", highlightbackground="#d9d9d9", highlightcolor="black",
            text='''Modify''')
        
        
class Result:
    def __init__(self, top=None):
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
        top.resizable(0,0)
        top.title("Result ")
        top.configure(background="#212529")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")
        
        self.Canvas1 = tk.Canvas(top)
        self.Canvas1.place(relx=0.067, rely=0.111, relheight=0.74
            , relwidth=0.872)
        self.Canvas1.configure(background="white")
        self.Canvas1.configure(insertbackground="black")
        self.Canvas1.configure(relief="ridge")
        self.Canvas1.configure(selectbackground="blue")
        self.Canvas1.configure(selectforeground="white")
        
        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.367, rely=0.022, height=31, width=174)
        self.Label1.configure(background="#212529", font="-family {Segoe UI} -size 13 -weight bold",
            foreground="#ffffff", text='''Result Table''')
        
        self.style.configure('Treeview', font="TkDefaultFont")
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
        self.add_button.place(relx=0.096, rely=0.811, height=20, width=89)
        self.add_button.configure(activebackground="#ececec", activeforeground="#000000", background="#3F454C",
            borderwidth="0", disabledforeground="#a3a3a3", font="-family {Segoe UI} -size 9 "
            "-weight bold",
            foreground="white", highlightbackground="#d9d9d9", highlightcolor="black",
            pady="0", text='''Add''')
        
        self.delete_button = tk.Button(self.Canvas1)
        self.delete_button.place(relx=0.421, rely=0.811, height=20, width=86)
        self.delete_button.configure(activebackground="#ececec", activeforeground="#000000", background="#3F454C",
            borderwidth="0", disabledforeground="#a3a3a3", font="-family {Segoe UI} -size 9 "
            "-weight bold",
            foreground="white", highlightbackground="#d9d9d9", highlightcolor="black",
            text="Delete")
        
        self.modify_button = tk.Button(self.Canvas1)
        self.modify_button.place(relx=0.746, rely=0.811, height=20, width=86)
        self.modify_button.configure(activebackground="#ececec", activeforeground="#000000", background="#3F454C",
            borderwidth="0", disabledforeground="#a3a3a3",
            font="-family {Segoe UI} -size 9 -weight bold",
            foreground="white", highlightbackground="#d9d9d9", highlightcolor="black",
            text='''Modify''')
        
        
class Subject:
    def __init__(self, top=None):
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
        self.Canvas1.configure(insertbackground="black")
        self.Canvas1.configure(relief="ridge")
        self.Canvas1.configure(selectbackground="blue")
        self.Canvas1.configure(selectforeground="white")
        
        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.367, rely=0.022, height=31, width=174)
        self.Label1.configure(background="#212529", font="-family {Segoe UI} -size 13 -weight bold",
            foreground="#ffffff", text='''Subject Table''')
        
        self.style.configure('Treeview', font="TkDefaultFont")
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
        self.add_button.place(relx=0.096, rely=0.811, height=20, width=89)
        self.add_button.configure(activebackground="#ececec", activeforeground="#000000", background="#3F454C",
            borderwidth="0", disabledforeground="#a3a3a3", font="-family {Segoe UI} -size 9 "
            "-weight bold",
            foreground="white", highlightbackground="#d9d9d9", highlightcolor="black",
            pady="0", text='''Add''')
        
        self.delete_button = tk.Button(self.Canvas1)
        self.delete_button.place(relx=0.421, rely=0.811, height=20, width=86)
        self.delete_button.configure(activebackground="#ececec", activeforeground="#000000", background="#3F454C",
            borderwidth="0", disabledforeground="#a3a3a3", font="-family {Segoe UI} -size 9 "
            "-weight bold",
            foreground="white", highlightbackground="#d9d9d9", highlightcolor="black",
            text="Delete")
        
        self.modify_button = tk.Button(self.Canvas1)
        self.modify_button.place(relx=0.746, rely=0.811, height=20, width=86)
        self.modify_button.configure(activebackground="#ececec", activeforeground="#000000", background="#3F454C",
            borderwidth="0", disabledforeground="#a3a3a3",
            font="-family {Segoe UI} -size 9 -weight bold",
            foreground="white", highlightbackground="#d9d9d9", highlightcolor="black",
            text='''Modify''')
        
        
class Attendance:
    def __init__(self, top=None):
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
        top.resizable(0,0)
        top.title("Attendance ")
        top.configure(background="#212529")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")
        
        self.Canvas1 = tk.Canvas(top)
        self.Canvas1.place(relx=0.067, rely=0.111, relheight=0.74
            , relwidth=0.872)
        self.Canvas1.configure(background="white")
        self.Canvas1.configure(insertbackground="black")
        self.Canvas1.configure(relief="ridge")
        self.Canvas1.configure(selectbackground="blue")
        self.Canvas1.configure(selectforeground="white")
        
        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.367, rely=0.022, height=31, width=174)
        self.Label1.configure(background="#212529", font="-family {Segoe UI} -size 13 -weight bold",
            foreground="#ffffff", text='''Attendance Table''')
        
        self.style.configure('Treeview', font="TkDefaultFont")
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
        self.add_button.place(relx=0.096, rely=0.811, height=20, width=89)
        self.add_button.configure(activebackground="#ececec", activeforeground="#000000", background="#3F454C",
            borderwidth="0", disabledforeground="#a3a3a3", font="-family {Segoe UI} -size 9 "
            "-weight bold",
            foreground="white", highlightbackground="#d9d9d9", highlightcolor="black",
            pady="0", text='''Add''')
        
        self.delete_button = tk.Button(self.Canvas1)
        self.delete_button.place(relx=0.421, rely=0.811, height=20, width=86)
        self.delete_button.configure(activebackground="#ececec", activeforeground="#000000", background="#3F454C",
            borderwidth="0", disabledforeground="#a3a3a3", font="-family {Segoe UI} -size 9 "
            "-weight bold",
            foreground="white", highlightbackground="#d9d9d9", highlightcolor="black",
            text="Delete")
        
        self.modify_button = tk.Button(self.Canvas1)
        self.modify_button.place(relx=0.746, rely=0.811, height=20, width=86)
        self.modify_button.configure(activebackground="#ececec", activeforeground="#000000", background="#3F454C",
            borderwidth="0", disabledforeground="#a3a3a3",
            font="-family {Segoe UI} -size 9 -weight bold",
            foreground="white", highlightbackground="#d9d9d9", highlightcolor="black",
            text='''Modify''')
        
        
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
        top.resizable(0,0)
        top.title("Branch ")
        top.configure(background="#212529")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")
        
        self.Canvas1 = tk.Canvas(top)
        self.Canvas1.place(relx=0.067, rely=0.111, relheight=0.74
            , relwidth=0.872)
        self.Canvas1.configure(background="white")
        self.Canvas1.configure(insertbackground="black")
        self.Canvas1.configure(relief="ridge")
        self.Canvas1.configure(selectbackground="blue")
        self.Canvas1.configure(selectforeground="white")
        
        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.367, rely=0.022, height=31, width=174)
        self.Label1.configure(background="#212529", font="-family {Segoe UI} -size 13 -weight bold",
            foreground="#ffffff", text='''Branch Table''')
        
        self.style.configure('Treeview', font="TkDefaultFont")
        self.tv = ScrolledTreeView(self.Canvas1)
        self.tv.place(relx=0.0, rely=0.0, relheight=0.712, relwidth=1.0)
        self.tv['columns'] = ("Col1", "Col2")
        self.tv.column("#0", width=0, stretch="NO")
        self.tv.column("Col1", width=100, anchor="center")
        self.tv.column("Col2", width=100, anchor="center")
        self.tv.heading("#0", text="")
        self.tv.heading("Col1", text="Column1", anchor="center")
        self.tv.heading("Col2", text="Column2", anchor="center")
        count = 0
        for i in range(20):
            self.tv.insert(parent='', index="end", iid=count,values=("Col1" + str(count), "Col2" + str(count)))
            count += 1
            
        self.add_button = tk.Button(self.Canvas1 , command=self.select_add)
        self.add_button.place(relx=0.096, rely=0.811, height=20, width=89)
        self.add_button.configure(activebackground="#ececec", activeforeground="#000000", background="#3F454C",
            borderwidth="0", disabledforeground="#a3a3a3", font="-family {Segoe UI} -size 9 "
            "-weight bold",
            foreground="white", highlightbackground="#d9d9d9", highlightcolor="black",
            pady="0", text='''Add''')
        
        self.delete_button = tk.Button(self.Canvas1, command=self.select_delete)
        self.delete_button.place(relx=0.421, rely=0.811, height=20, width=86)
        self.delete_button.configure(activebackground="#ececec", activeforeground="#000000", background="#3F454C",
            borderwidth="0", disabledforeground="#a3a3a3", font="-family {Segoe UI} -size 9 "
            "-weight bold",
            foreground="white", highlightbackground="#d9d9d9", highlightcolor="black",
            text="Delete")
        
        self.modify_button = tk.Button(self.Canvas1, command=self.select_modify)
        self.modify_button.place(relx=0.746, rely=0.811, height=20, width=86)
        self.modify_button.configure(activebackground="#ececec", activeforeground="#000000", background="#3F454C",
            borderwidth="0", disabledforeground="#a3a3a3",
            font="-family {Segoe UI} -size 9 -weight bold",
            foreground="white", highlightbackground="#d9d9d9", highlightcolor="black",
            text='''Modify''')
        
    def select_add(self):
        print()
        
    def select_modify(self):
        print()
        
    def select_delete(self):
        print()
    
    def select_display(self):
        data = display_table(6)
        print(data)
        
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
        
        
        # The following code is added to facilitate the Scrolled widgets you specified.
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


class ScrolledTreeView(AutoScroll, ttk.Treeview):
    '''A standard ttk Treeview widget with scrollbars that will
        automatically show/hide as needed.'''
    
    @_create_container
    def __init__(self, master, **kw):
        ttk.Treeview.__init__(self, master, **kw)
        AutoScroll.__init__(self, master)
        
        
import platform


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
        
        
root = tk.Tk()
top = MainScreen(root)
root.mainloop()

#Tkinter GUI code ends