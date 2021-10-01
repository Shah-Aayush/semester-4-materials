"""
This code is written by :

1. 19BCE237 - Sakshi Sanghavi
2. 19BCE238 - Harshil Sanghvi
3. 19BCE245 - Aayush Shah

"""

import os	#for creating directories Admin/Customer if it is not exists.
from datetime import date		#for date of account creation when new customer account is created.
import tkinter as tk
from tkinter import *

#Backend python functions code starts :
def is_valid(customer_account_number):
    try:
        customer_database = open("./database/Customer/customerDatabase.txt")
    except FileNotFoundError:
        os.makedirs("./database/Customer/customerDatabase.txt", exist_ok=True)
        print("# Customer database doesn't exists!\n# New Customer database created automatically.")
        customer_database = open("./database/Customer/customerDatabase.txt", "a")
    else:		#if customer account  number is already allocated then this will return false. otherwise true.
        if(check_credentials(customer_account_number, "DO_NOT_CHECK", 2,True)):
            return False
        else:
            return True
    
def check_leap(year):
    return ((int(year) % 4 == 0) and (int(year) % 100 != 0)) or (int(year) % 400 == 0)

def check_date(date):
    days_in_months = ["31", "28", "31", "30", "31", "30", "31", "31", "30", "31", "30", "31"]
    days_in_months_in_leap_year = ["31", "29", "31", "30", "31", "30", "31", "31", "30", "31", "30", "31"]
    date_elements = date.split("/")
    day = int(date_elements[0])
    month = int(date_elements[1])
    year = int(date_elements[2])
    if ((year > 2021 or year < 0) or (month > 12 or month < 1)):
        return False;
    else:
        if (check_leap(year)):
            numOfDays = days_in_months_in_leap_year[month - 1];
        else:
            numOfDays = days_in_months_in_leap_year[month - 1];
        return day <= int(numOfDays) and day >= 1;
    
def is_valid_mobile(mobile_number):
    if(mobile_number.__len__() == 10 and mobile_number.isnumeric()):
        return True
    else:
        return False
    
def append_data(database_path,data):
    customer_database = open(database_path,"a")
    customer_database.write(data)
    
def create_customer_account():
    
    customer_account_number = "NOT_SET"
    while True:				#set account number
        customer_account_number = str(input("\nPlease enter customer account number : "))
        if(is_valid(customer_account_number) and customer_account_number.isnumeric()):
            break
        else:
            print("\n# This account number already exists or invalid !")
            
    today = date.today()	#set date of account creation
    date_of_account_creation = today.strftime("%d/%m/%Y")
    
    name =  str(input("Enter name : "))		#set name
    
    account_type = "Savings or Current  [radio buttons]"
    while True:				#set account type
        choice = int(input("Select account type : \n[1.] Savings\n[2.] Current\n\tChoice : "))
        if(choice == 1):
            account_type = "Savings"
            break
        elif(choice == 2):
            account_type = "Current"
            break
        else:
            print("# Invalid choice!")
            
    date_or_birth = "NOT_SET"
    while True:				#set date of birth
        date_of_birth = str(input("Enter date of birth [format : dd/mm/yyyy]: "))
        if(check_date(date_of_birth)):
            break
        else:
            print("\n# Please enter a valid date. #")
            
    mobile_number = "NOT_SET"
    while True:				#set mobile number
        mobile_number = str(input("Enter mobile number : "))
        if(is_valid_mobile(mobile_number)):
            break
        else:
            mobile_number = str(input("Enter valid mobile number : "))
            
    gender = "MALE_or_FEMALE [radio button]"
    while True:				#set gender
        choice = int(input("Select gender : \n[1.] Male\n[2.] Female\n\tChoice : "))
        if(choice == 1):
            gender = "Male"
            break
        elif(choice == 2):
            gender = "Female"
            break
        else:
            print("# Invalid choice!")
            
    nationality = str(input("Enter nationality : ")) 		#set nationality
    
    KYC_document = str(input("Enter KYC document id : "))		#set KYC document
    
    PIN = "NOT_SET"
    while True:		#set PIN
        PIN = str(input("Enter 4 digit PIN : "))
        if(PIN.isnumeric() and PIN.__len__() == 4):
            PIN_confirm = str(input("Confirm  your PIN : "))
            if(PIN_confirm ==  PIN):
                print("PIN set successfully!")
                break
            else:
                print("PIN not matched :(")
        else:
            PIN = str(input("Enter valid PIN : "))
            
    initial_balance = "NOT_SET"
    while True:		#set initial balance
        initial_balance = str(input("Enter initial balance : "))
        if(initial_balance.isnumeric()):
            break
        else:
            initial_balance = str(input("Enter valid balance : "))
            
    data = customer_account_number + "\n" + PIN + "\n" + initial_balance + "\n" + date_of_account_creation + "\n" + name + "\n" + account_type + "\n" + date_of_birth + "\n" + mobile_number + "\n" + gender + "\n" + nationality + "\n" + KYC_document + "\n" + "*\n"
    append_data("./database/Customer/customerDatabase.txt", data)
    print()
    
def display_account_summary(id,choice):		#choice 1 for full summary; choice 2 for only account balance.
    flag = 0
    customer_database = open("./database/Customer/customerDatabase.txt")
    for line in customer_database:
        if(id == line.replace("\n", "")):
            if(choice == 1):
                print("Account number : ",line.replace("\n", ""))
                pin_ToBeSkipped = customer_database.__next__()
                print("Current balance : ",customer_database.__next__().replace("\n", ""))
                print("Date of account creation : ",customer_database.__next__().replace("\n", ""))
                print("Name of account holder : ",customer_database.__next__().replace("\n", ""))
                print("Type of account : ",customer_database.__next__().replace("\n", ""))
                print("Date of Birth : ",customer_database.__next__().replace("\n", ""))
                print("Mobile number : ",customer_database.__next__().replace("\n", ""))
                print("Gender r : ",customer_database.__next__().replace("\n", ""))
                print("Nationality : ",customer_database.__next__().replace("\n", ""))
                print("KYC : ",customer_database.__next__().replace("\n", ""))
                
                
            else:
                customer_database.readline()	#skipped pin
                print("Current balance : ",customer_database.readline())		#got balance
            flag = 1
            break
        
        else:
            for index in range(11):
                fetched_line = customer_database.readline()
                if( fetched_line!= None):
                    continue
                else:
                    break
    if(flag==0):
        print("\n# No account associated with the entered account number exists! #")
        
def delete_customer_account(id):
    customer_database = open("./database/Customer/customerDatabase.txt")
    data_collector = ""
    flag = 0
    for line in customer_database:
        if(id == line.replace("\n", "")):
            flag = 1
            for index in range(11):
                line_ToBeSkipped = customer_database.readline()
        else:
            data_collector += line
            for index in range(11):
                data_collector += customer_database.readline()
    customer_database = open("./database/Customer/customerDatabase.txt","w")
    customer_database.write(data_collector)
    if(flag==1):
        print("\n# Account with account no.",id,"closed successfully!")
    else:
        print("# Account not found :(")
        
def create_admin_account():
    admin_database = open("./database/Admin/adminDatabase.txt","a")
    admin_id = ""
    while True:
        admin_id = str(input("Enter id : "))
        if(check_credentials(admin_id, "DO_NOT_CHECK_ADMIN", 1, False)):
            print("# Admin id is already in use #\n Try new id !")
        else:
            break
        
    admin_password = ""
    while True:
        admin_password = str(input("Enter password : "))
        admin_password_confirm = str(input("Confirm password : "))
        if(admin_password == admin_password_confirm):
            break
        else:
            print("# Password didn't match #")
            
    append_data("./database/Admin/adminDatabase.txt", admin_id + "\n" + admin_password + "\n" + "*\n")
    print("# Admin account created successfully !")
    
def delete_admin_account(id):
    admin_database = open("./database/Admin/adminDatabase.txt")
    data_collector = ""
    flag = 0
    for line in admin_database:
        if(id == line.replace("\n", "")):
            flag = 1
            for index in range(2):
                line_ToBeSkipped = admin_database.readline()
        else:
            data_collector += line
            for index in range(2):
                data_collector += admin_database.readline()
    admin_database = open("./database/Admin/adminDatabase.txt","w")
    admin_database.write(data_collector)
    if(flag==1):
        print("\n# Account with account id",id,"closed successfully!")
    else:
        print("# Account not found :(")
        
def change_PIN(id,new_PIN):
    customer_database = open("./database/Customer/customerDatabase.txt")
    data_collector = ""
    balance = 0
    for line in customer_database:
        if(id == line.replace("\n", "")):
            data_collector += line	#ID
            data_collector += str(new_PIN) + "\n"	#PIN changed
            line_ToBeSkipped = customer_database.readline()		#skipping PIN
            for index in range(10):
                data_collector += customer_database.readline()
        else:
            data_collector += line
            for index in range(11):
                data_collector += customer_database.readline()
    customer_database.close()
    customer_database = open("./database/Customer/customerDatabase.txt","w")
    customer_database.write(data_collector)
    print("# PIN changed successfully.")
    
def banker_functions():
    choice = 0
    while True:
        print("\nChoose the number corresponding to function :")
        print("1. Create a bank account")
        print("2. Display Account summary")
        print("3. Close bank account")
        print("4. Create an admin account")
        print("5. Delete an admin account")
        print("6. Return to main menu")
        choice = int(input("\n\tChoice : "))
        
        if(choice == 1):
            create_customer_account()
            
        elif(choice == 2):
            id = str(input("\nPlease enter account number whose data is to be displayed: "))
            if(not is_valid(id)):
                display_account_summary(id,1)
            else:
                print("\n# No account associated with the entered account number exists! #")
                
        elif(choice == 3):
            id = str(input("\nPlease enter account number whose data is to be deleted: "))
            if(not is_valid(id)):
                delete_customer_account(id)
            else:
                print("\n# No account associated with the entered account number exists! #")
                
        elif(choice == 4):
            create_admin_account()
            
        elif(choice == 5):
            id = str(input("\nPlease enter admin id whose data is to be deleted: "))
            if(id == "admin"):
                print("Default admin cannot be deleted :(")
                continue
            password = str(input("Please enter admin password: "))
            if(check_credentials(id, password, 1, True)):
                delete_admin_account(id)
            else:
                print("\n# Please enter valid credentials! #")
                
        elif(choice ==  6):
            break
        
        else:
            print("\n# Invalid Choice.")
def transaction(id,amount,choice):		#choice 1 for deposit; choice 2 for withdraw
    customer_database = open("./database/Customer/customerDatabase.txt")
    data_collector = ""
    balance = 0
    for line in customer_database:
        if(id == line.replace("\n", "")):
            data_collector += line	#ID
            data_collector += customer_database.readline()	#PIN
            balance = int(customer_database.readline().replace("\n", ""))
            if(choice==2 and balance-amount<0):
                return -1
            else:
                if(choice==1):
                    balance += amount
                else:
                    balance -= amount
            data_collector += str(balance) + "\n"
            for index in range(9):
                data_collector += customer_database.readline()
        else:
            data_collector += line
            for index in range(11):
                data_collector += customer_database.readline()
                
    customer_database.close()
    customer_database = open("./database/Customer/customerDatabase.txt","w")
    customer_database.write(data_collector)
    return balance

def customer_functions(id):
    choice = 0
    while True:
        print("\nChoose the number corresponding to function :")
        print("1. Deposit money")
        print("2. Withdraw money")
        print("3. Change PIN")
        print("4. Show account balance")
        print("5. Close bank account")
        print("6. Return to main menu")
        choice = int(input("\n\tChoice : "))
        
        if(choice == 1):
            amount = 25001
            while(amount>25000):
                amount = int(input("Enter amount to be deposit : "))
                if(amount<25000):
                    break
                else:
                    print("\n# Sorry, you cannot deposit more than Rs. 25000 at a time. \nPlease try with smaller amount depositions. #")
            output = transaction(id, amount, 1)
            if(output ==  -1):
                print("#Transaction failed :(")
            else:
                print("Amount of rupees",amount,"deposited successfully.\nUpdated balance : ",output)
                
        elif(choice == 2):
            amount = 25001
            while(amount>25000):
                amount = int(input("Enter amount to be deposit : "))
                if(amount<25000):
                    break
                else:
                    print("\n# Sorry, you cannot withdraw more than Rs. 25000 at a time. \nPlease try with smaller amount to withdraw. #")
            output = transaction(id, amount, 2)
            if(output ==  -1):
                print("#Not enough balance :(")
            else:
                print("Amount of rupees",amount,"withdrawn successfully.\nUpdated balance : ",output)
                
        elif(choice == 3):
            new_PIN = 0
            while True : 
                new_PIN = int(input("Enter new PIN : "))
                confirm_new_PIN = int(input("Confirm new PIN : "))
                if(new_PIN == confirm_new_PIN and str(new_PIN).__len__() == 4):
                    break
                else:
                    if(new_PIN != confirm_new_PIN):
                        print("# PIN didn't matched :(")
                    if(str(new_PIN).__len__() != 4):
                        print("# PIN length must be 4 :(")
            change_PIN(id,new_PIN)
            
        elif(choice == 4):
            display_account_summary(id,2)
            
        elif(choice == 5):
            print()
            if(int(input("Are you sure ? : \n[1.] YES\n[2.] NO\nEnter choice : ")) == 1):	#insert pop-up here.
                delete_customer_account(id)
            else:
                print("Thank god !")
                
        elif(choice ==  6):
            break
        
        else:
            print("\n# Invalid Choice.")
            
def banker():
    print("Hello Banker!")
    
def customer():
    print("Hello Customer!")
    
def check_credentials(id,password,choice,admin_access):		#checks credentials of admin/customer and returns True or False 
    folder_name = "./database/Admin" if (choice==1) else "./database/Customer"
    file_name = "/adminDatabase.txt" if (choice==1) else "/customerDatabase.txt"
    
    try:
        os.makedirs(folder_name, exist_ok=True)
        database = open(folder_name+file_name,"r")
    except FileNotFoundError:
        print("#",folder_name[2:],"database doesn't exists!\n# New",folder_name[2:],"database created automatically.")
        database = open(folder_name + file_name, "a")
        if(choice==1):
            database.write("admin\nadmin@123\n*\n")
    else:
        is_credentials_correct = False
        for line in database:
            id_fetched = line.replace("\n", "")
            password_fetched = database.__next__().replace("\n", "")
            if(id_fetched == id):
                if((password=="DO_NOT_CHECK_ADMIN" and choice==1 and admin_access==False) or (password=="DO_NOT_CHECK" and choice==2 and admin_access==True) or password_fetched == password):
                    is_credentials_correct = True
                    database.close()
                    return True
                    break
            if(choice==1):		#skips unnecessary lines in admin database.
                sign = database.__next__()
            else:				#skips unnecessary lines in customer database.
                for index in range(10):
                    fetched_line = database.readline()
                    if( fetched_line!= None):
                        continue
                    else:
                        break
    database.close()
    return False
#Backend python functions code ends.

# Tkinter GUI code starts :  
class welcomeScreen:
    def __init__(self, top=None):
        self.master = top
        top.geometry("600x450+383+106")
        top.minsize(120, 1)
        top.maxsize(1370, 749)
        top.resizable(0, 0)
        top.title("Welcome to NIRMA BANK")
        top.configure(background="#023047")
        top.configure(cursor="arrow")

        self.Canvas1 = tk.Canvas(top, background="#ffb703", borderwidth="0", insertbackground="black", relief="ridge",
                                 selectbackground="blue", selectforeground="white")
        self.Canvas1.place(relx=0.190, rely=0.228, relheight=0.496, relwidth=0.622)

        self.Button1 = tk.Button(self.Canvas1, command=self.selectEmployee, activebackground="#ececec",
                                 activeforeground="#000000", background="#023047", disabledforeground="#a3a3a3",
                                 foreground="#fbfbfb", borderwidth="0", highlightbackground="#d9d9d9",
                                 highlightcolor="black", pady="0",
                                 text='''EMPLOYEE''')
        self.Button1.configure(font="-family {Segoe UI} -size 10 -weight bold")
        self.Button1.place(relx=0.161, rely=0.583, height=24, width=87)

        self.Button2 = tk.Button(self.Canvas1, command=self.selectCustomer, activebackground="#ececec",
                                 activeforeground="#000000", background="#023047", disabledforeground="#a3a3a3",
                                 foreground="#f9f9f9", borderwidth="0", highlightbackground="#d9d9d9",
                                 highlightcolor="black", pady="0",
                                 text='''CUSTOMER''')
        self.Button2.configure(font="-family {Segoe UI} -size 10 -weight bold")
        self.Button2.place(relx=0.617, rely=0.583, height=24, width=87)

        self.Label1 = tk.Label(self.Canvas1, background="#ffb703", disabledforeground="#a3a3a3",
                               font="-family {Segoe UI} -size 13 -weight bold", foreground="#000000",
                               text='''Please select your role''')
        self.Label1.place(relx=0.241, rely=0.224, height=31, width=194)

    def selectEmployee(self):
        self.master.withdraw()
        adminLogin(Toplevel(self.master))

    def selectCustomer(self):
        self.master.withdraw()
        customerLogin(Toplevel(self.master))


class adminLogin:
    def __init__(self, top=None):
        self.master = top
        top.geometry("743x494+338+92")
        top.minsize(120, 1)
        top.maxsize(1370, 749)
        top.resizable(0, 0)
        top.title("New Toplevel")
        top.configure(background="#ffff00")

        self.Canvas1 = tk.Canvas(top, background="#ffffff", insertbackground="black", relief="ridge",
                                 selectbackground="blue", selectforeground="white")
        self.Canvas1.place(relx=0.108, rely=0.142, relheight=0.715, relwidth=0.798)

        self.Label1 = tk.Label(self.Canvas1, background="#ffffff", disabledforeground="#a3a3a3",
                               font="-family {Segoe UI} -size 14 -weight bold", foreground="#00254a",
                               text="Admin Login")
        self.Label1.place(relx=0.135, rely=0.142, height=41, width=154)

        self.Label2 = tk.Label(self.Canvas1, background="#ffffff", disabledforeground="#a3a3a3", foreground="#000000")
        self.Label2.place(relx=0.067, rely=0.283, height=181, width=233)
        global _img0
        _img0 = tk.PhotoImage(file="./images/adminLogin1.png")
        self.Label2.configure(image=_img0)

        self.Entry1 = tk.Entry(self.Canvas1, background="#e2e2e2", borderwidth="2", disabledforeground="#a3a3a3",
                               font="TkFixedFont", foreground="#000000", highlightbackground="#b6b6b6",
                               highlightcolor="#004080", insertbackground="black")
        self.Entry1.place(relx=0.607, rely=0.453, height=20, relwidth=0.26)

        self.Entry1_1 = tk.Entry(self.Canvas1, show='*', background="#e2e2e2", borderwidth="2",
                                 disabledforeground="#a3a3a3", font="TkFixedFont", foreground="#000000",
                                 highlightbackground="#d9d9d9", highlightcolor="#004080", insertbackground="black",
                                 selectbackground="blue", selectforeground="white")
        self.Entry1_1.place(relx=0.607, rely=0.623, height=20, relwidth=0.26)

        self.Label3 = tk.Label(self.Canvas1, background="#ffffff", disabledforeground="#a3a3a3", foreground="#000000")
        self.Label3.place(relx=0.556, rely=0.453, height=21, width=34)
        global _img1
        _img1 = tk.PhotoImage(file="./images/user1.png")
        self.Label3.configure(image=_img1)

        self.Label4 = tk.Label(self.Canvas1, background="#ffffff", disabledforeground="#a3a3a3", foreground="#000000")
        self.Label4.place(relx=0.556, rely=0.623, height=21, width=34)
        global _img2
        _img2 = tk.PhotoImage(file="./images/lock1.png")
        self.Label4.configure(image=_img2)

        self.Label5 = tk.Label(self.Canvas1, background="#ffffff", disabledforeground="#a3a3a3", foreground="#000000")
        self.Label5.place(relx=0.670, rely=0.142, height=71, width=74)
        global _img3
        _img3 = tk.PhotoImage(file="./images/bank1.png")
        self.Label5.configure(image=_img3)

        self.Button = tk.Button(self.Canvas1, text="Login", borderwidth="0", width=10, background="#ffff00",
                                foreground="#00254a",
                                font="-family {Segoe UI} -size 10 -weight bold", command= lambda:self.login(self.Entry1.get(),self.Entry1_1.get()))
        self.Button.place(relx=0.665, rely=0.755)

    def login(self,admin_id,admin_password):
        if(check_credentials(admin_id, admin_password, 1,True)):
            self.master.withdraw()
            adminMenu(Toplevel(self.master))
        else:
            print("\n# Please enter valid credentials! #")


class customerLogin:
    def __init__(self, top=None):
        self.master = top
        top.geometry("743x494+338+92")
        top.minsize(120, 1)
        top.maxsize(1370, 749)
        top.resizable(0, 0)
        top.title("New Toplevel")
        top.configure(background="#00254a")

        self.Canvas1 = tk.Canvas(top, background="#ffffff", insertbackground="black", relief="ridge",
                                 selectbackground="blue", selectforeground="white")
        self.Canvas1.place(relx=0.108, rely=0.142, relheight=0.715, relwidth=0.798)

        self.Label1 = tk.Label(self.Canvas1, background="#ffffff", disabledforeground="#a3a3a3",
                               font="-family {Segoe UI} -size 14 -weight bold", foreground="#00254a",
                               text="Customer Login")
        self.Label1.place(relx=0.135, rely=0.142, height=41, width=154)

        self.Label2 = tk.Label(self.Canvas1, background="#ffffff", disabledforeground="#a3a3a3", foreground="#000000")
        self.Label2.place(relx=0.067, rely=0.283, height=181, width=233)
        global _img0
        _img0 = tk.PhotoImage(file="./images/customer.png")
        self.Label2.configure(image=_img0)

        self.Entry1 = tk.Entry(self.Canvas1, background="#e2e2e2", borderwidth="2", disabledforeground="#a3a3a3",
                               font="TkFixedFont", foreground="#000000", highlightbackground="#b6b6b6",
                               highlightcolor="#004080", insertbackground="black")
        self.Entry1.place(relx=0.607, rely=0.453, height=20, relwidth=0.26)

        self.Entry1_1 = tk.Entry(self.Canvas1, show='*', background="#e2e2e2", borderwidth="2",
                                 disabledforeground="#a3a3a3", font="TkFixedFont", foreground="#000000",
                                 highlightbackground="#d9d9d9", highlightcolor="#004080", insertbackground="black",
                                 selectbackground="blue", selectforeground="white")
        self.Entry1_1.place(relx=0.607, rely=0.623, height=20, relwidth=0.26)

        self.Label3 = tk.Label(self.Canvas1, background="#ffffff", disabledforeground="#a3a3a3", foreground="#000000")
        self.Label3.place(relx=0.556, rely=0.453, height=21, width=34)

        global _img1
        _img1 = tk.PhotoImage(file="./images/user1.png")
        self.Label3.configure(image=_img1)

        self.Label4 = tk.Label(self.Canvas1)
        self.Label4.place(relx=0.556, rely=0.623, height=21, width=34)
        global _img2
        _img2 = tk.PhotoImage(file="./images/lock1.png")
        self.Label4.configure(image=_img2)

        self.Label5 = tk.Label(self.Canvas1, background="#ffffff", disabledforeground="#a3a3a3", foreground="#000000")
        self.Label5.place(relx=0.670, rely=0.142, height=71, width=74)
        global _img3
        _img3 = tk.PhotoImage(file="./images/bank1.png")
        self.Label5.configure(image=_img3)

        self.Button = tk.Button(self.Canvas1, text="Login", borderwidth="0", width=10, background="#00254a",
                                foreground="#ffffff",
                                font="-family {Segoe UI} -size 10 -weight bold", command= lambda: self.login(self.Entry1.get(),self.Entry1_1.get()))
        self.Button.place(relx=0.665, rely=0.755)

    def login(self,customer_account_number,customer_PIN):
        if(check_credentials(customer_account_number, customer_PIN, 2,False)):
            self.master.withdraw()
            customerMenu(Toplevel(self.master))
        else:
            print("\n# Please enter valid credentials! #")


class adminMenu:
    def __init__(self, window=None):
        self.master = window
        window.geometry("743x494+329+153")
        window.minsize(120, 1)
        window.maxsize(1370, 749)
        window.resizable(0, 0)
        window.title("Admin Section")
        window.configure(background="#ffff00")

        self.Labelframe1 = tk.LabelFrame(window, relief='groove', font="-family {Segoe UI} -size 13 -weight bold",
                                         foreground="#001c37", text="Select your option", background="#fffffe")
        self.Labelframe1.place(relx=0.081, rely=0.081, relheight=0.415, relwidth=0.848)

        self.Button1 = tk.Button(self.Labelframe1, activebackground="#ececec", activeforeground="#000000",
                                 background="#00254a", borderwidth="0", disabledforeground="#a3a3a3",
                                 font="-family {Segoe UI} -size 11", foreground="#fffffe",
                                 highlightbackground="#d9d9d9", highlightcolor="black", pady="0",
                                 text="Close bank account", command=self.closeAccount)
        self.Button1.place(relx=0.667, rely=0.195, height=34, width=181, bordermode='ignore')

        self.Button2 = tk.Button(self.Labelframe1, activebackground="#ececec", activeforeground="#000000",
                                 background="#00254a", borderwidth="0", disabledforeground="#a3a3a3",
                                 font="-family {Segoe UI} -size 11", foreground="#fffffe",
                                 highlightbackground="#d9d9d9", highlightcolor="black", pady="0",
                                 text="Create bank account", command=self.createCustaccount)
        self.Button2.place(relx=0.04, rely=0.195, height=34, width=181, bordermode='ignore')

        self.Button3 = tk.Button(self.Labelframe1, activebackground="#ececec", activeforeground="#000000",
                                 background="#00254a", borderwidth="0", disabledforeground="#a3a3a3",
                                 font="-family {Segoe UI} -size 11", foreground="#fffffe",
                                 highlightbackground="#d9d9d9", highlightcolor="black", pady="0", text="Exit",
                                 command=self.exit)
        self.Button3.place(relx=0.667, rely=0.683, height=34, width=181, bordermode='ignore')

        self.Button4 = tk.Button(self.Labelframe1, activebackground="#ececec", activeforeground="#000000",
                                 background="#00254a", borderwidth="0", disabledforeground="#a3a3a3",
                                 font="-family {Segoe UI} -size 11", foreground="#fffffe",
                                 highlightbackground="#d9d9d9", highlightcolor="black", pady="0",
                                 text="Create admin account", command=self.createAdmin)
        self.Button4.place(relx=0.04, rely=0.439, height=34, width=181, bordermode='ignore')

        self.Button5 = tk.Button(self.Labelframe1, activebackground="#ececec", activeforeground="#000000",
                                 background="#00254a", borderwidth="0", disabledforeground="#a3a3a3",
                                 font="-family {Segoe UI} -size 11", foreground="#fffffe",
                                 highlightbackground="#d9d9d9", highlightcolor="black", pady="0",
                                 text="Close admin account", command=self.deleteAdmin)
        self.Button5.place(relx=0.667, rely=0.439, height=34, width=181, bordermode='ignore')

        self.Button6 = tk.Button(self.Labelframe1, activebackground="#ececec", activeforeground="#000000",
                                 background="#00254a", foreground="#fffffe", borderwidth="0",
                                 disabledforeground="#a3a3a3", font="-family {Segoe UI} -size 11",
                                 highlightbackground="#d9d9d9", highlightcolor="black", pady="0",
                                 text="Check account summary")
        self.Button6.place(relx=0.04, rely=0.683, height=34, width=181, bordermode='ignore')

        self.Frame1 = tk.Frame(window, relief='groove', borderwidth="2", background="#fffffe")
        self.Frame1.place(relx=0.081, rely=0.547, relheight=0.415, relwidth=0.848)

    def closeAccount(self):
        self.master.withdraw()
        closeAccountByAdmin(Toplevel(self.master))

    def createCustaccount(self):
        self.master.withdraw()
        createCustomerAccount(Toplevel(self.master))

    def createAdmin(self):
        self.master.withdraw()
        createAdmin(Toplevel(self.master))

    def deleteAdmin(self):
        self.master.withdraw()
        deleteAdmin(Toplevel(self.master))
        
    def showAccountSummary():
        
        print()

    def exit(self):
        self.master.withdraw()
        adminLogin(Toplevel(self.master))


class closeAccountByAdmin:
    def __init__(self, window=None):
        self.master = window
        window.geometry("411x117+498+261")
        window.minsize(120, 1)
        window.maxsize(1370, 749)
        window.resizable(1, 1)
        window.title("Close account")
        window.configure(background="#f2f3f4")

        self.Label1 = tk.Label(window, background="#f2f3f4", disabledforeground="#a3a3a3",
                               text='''Enter account number:''')
        self.Label1.place(relx=0.232, rely=0.220, height=20, width=120)

        self.Entry1 = tk.Entry(window, background="#cae4ff", disabledforeground="#a3a3a3", font="TkFixedFont",
                               foreground="#000000", insertbackground="black")
        self.Entry1.place(relx=0.536, rely=0.220, height=20, relwidth=0.232)

        self.Button1 = tk.Button(window, activebackground="#ececec", activeforeground="#000000", borderwidth="0",
                                 background="#004080", disabledforeground="#a3a3a3", foreground="#ffffff",
                                 highlightbackground="#d9d9d9", highlightcolor="black", pady="0", text="Back",
                                 command=self.back)
        self.Button1.place(relx=0.230, rely=0.598, height=24, width=67)

        self.Button2 = tk.Button(window, activebackground="#ececec", activeforeground="#000000", background="#004080",
                                 borderwidth="0", disabledforeground="#a3a3a3", foreground="#ffffff",
                                 highlightbackground="#d9d9d9", highlightcolor="black", pady="0", text="Proceed")
        self.Button2.place(relx=0.598, rely=0.598, height=24, width=67)

    def back(self):
        self.master.withdraw()
        adminMenu(Toplevel(self.master))


class createCustomerAccount:
    def __init__(self, window=None):
        self.master = window
        window.geometry("411x366+450+210")
        window.minsize(120, 1)
        window.maxsize(1370, 749)
        window.resizable(1, 1)
        window.title("Create account")
        window.configure(background="#f2f3f4")

        self.Entry1 = tk.Entry(window, background="#cae4ff", disabledforeground="#a3a3a3", font="TkFixedFont",
                               foreground="#000000", insertbackground="black")
        self.Entry1.place(relx=0.511, rely=0.062, height=20, relwidth=0.302)

        self.Label1 = tk.Label(window, background="#f2f3f4", disabledforeground="#a3a3a3", foreground="#000000",
                               text='''Account number:''')
        self.Label1.place(relx=0.219, rely=0.057, height=23, width=120)

        self.Label2 = tk.Label(window, activebackground="#f9f9f9", activeforeground="black", background="#f2f3f4",
                               cursor="fleur", disabledforeground="#a3a3a3", foreground="#000000",
                               highlightbackground="#d9d9d9", highlightcolor="black", text='''Full name:''')
        self.Label2.place(relx=0.316, rely=0.142, height=24, width=75)

        self.Entry2 = tk.Entry(window, background="#cae4ff", disabledforeground="#a3a3a3", font="TkFixedFont",
                               foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black",
                               insertbackground="black", selectbackground="blue", selectforeground="white")
        self.Entry2.place(relx=0.511, rely=0.153, height=20, relwidth=0.302)

        self.Label3 = tk.Label(window, background="#f2f3f4", disabledforeground="#a3a3a3", foreground="#000000",
                               text='''Account type:''')
        self.Label3.place(relx=0.292, rely=0.227, height=23, width=84)

        self.Radiobutton1 = tk.Radiobutton(window, activebackground="#ececec", activeforeground="#000000",
                                           background="#f2f3f4", disabledforeground="#a3a3a3", foreground="#000000",
                                           highlightbackground="#d9d9d9", highlightcolor="black", justify='left',
                                           text='''Savings''')
        self.Radiobutton1.place(relx=0.511, rely=0.238, relheight=0.057, relwidth=0.151)
        self.Radiobutton1.deselect()

        self.Radiobutton2 = tk.Radiobutton(window, activebackground="#ececec", activeforeground="#000000",
                                           background="#f2f3f4", disabledforeground="#a3a3a3", foreground="#000000",
                                           highlightbackground="#d9d9d9", highlightcolor="black", justify='left',
                                           text='''Current''')
        self.Radiobutton2.place(relx=0.706, rely=0.238, relheight=0.057, relwidth=0.175)
        self.Radiobutton2.deselect()

        self.Label4 = tk.Label(window, activebackground="#f9f9f9", activeforeground="black", background="#f2f3f4",
                               disabledforeground="#a3a3a3", foreground="#000000", highlightbackground="#d9d9d9",
                               highlightcolor="black", text='''Mobile number:''')
        self.Label4.place(relx=0.275, rely=0.397, height=19, width=85)

        self.Label5 = tk.Label(window, activebackground="#f9f9f9", activeforeground="black", background="#f2f3f4",
                               disabledforeground="#a3a3a3", foreground="#000000", highlightbackground="#d9d9d9",
                               highlightcolor="black", text='''Birth date:''')
        self.Label5.place(relx=0.326, rely=0.312, height=23, width=75)

        self.Entry3 = tk.Entry(window, background="#cae4ff", disabledforeground="#a3a3a3", font="TkFixedFont",
                               foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black",
                               insertbackground="black", selectbackground="blue", selectforeground="white")
        self.Entry3.place(relx=0.511, rely=0.397, height=20, relwidth=0.302)

        self.Entry4 = tk.Entry(window, background="#cae4ff", disabledforeground="#a3a3a3", font="TkFixedFont",
                               foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black",
                               insertbackground="black", selectbackground="blue", selectforeground="white")
        self.Entry4.place(relx=0.511, rely=0.312, height=20, relwidth=0.302)

        self.Label6 = tk.Label(window, activebackground="#f9f9f9", activeforeground="black", background="#f2f3f4",
                               disabledforeground="#a3a3a3", foreground="#000000", highlightbackground="#d9d9d9",
                               highlightcolor="black", text='''Gender:''')
        self.Label6.place(relx=0.35, rely=0.482, height=12, width=65)

        self.Radiobutton3 = tk.Radiobutton(window, activebackground="#ececec", activeforeground="#000000",
                                           background="#f2f3f4", disabledforeground="#a3a3a3", foreground="#000000",
                                           highlightbackground="#d9d9d9", highlightcolor="black", justify='left',
                                           text='''Male''')
        self.Radiobutton3.place(relx=0.487, rely=0.482, relheight=0.054, relwidth=0.175)
        self.Radiobutton3.deselect()

        self.Radiobutton4 = tk.Radiobutton(window, activebackground="#ececec", activeforeground="#000000",
                                           background="#f2f3f4", disabledforeground="#a3a3a3", foreground="#000000",
                                           highlightbackground="#d9d9d9", highlightcolor="black", justify='left',
                                           text='''Female''')
        self.Radiobutton4.place(relx=0.706, rely=0.482, relheight=0.054, relwidth=0.175)
        self.Radiobutton4.deselect()

        self.Label7 = tk.Label(window, activebackground="#f9f9f9", activeforeground="black", background="#f2f3f4",
                               disabledforeground="#a3a3a3", foreground="#000000", highlightbackground="#d9d9d9",
                               highlightcolor="black", text='''Nationality:''')
        self.Label7.place(relx=0.314, rely=0.555, height=18, width=75)

        self.Entry5 = tk.Entry(window, background="#cae4ff", disabledforeground="#a3a3a3", font="TkFixedFont",
                               foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black",
                               insertbackground="black", selectbackground="blue", selectforeground="white")
        self.Entry5.place(relx=0.511, rely=0.555, height=20, relwidth=0.302)

        self.Entry6 = tk.Entry(window, background="#cae4ff", disabledforeground="#a3a3a3", font="TkFixedFont",
                               foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black",
                               insertbackground="black", selectbackground="blue", selectforeground="white")
        self.Entry6.place(relx=0.511, rely=0.64, height=20, relwidth=0.302)

        self.Entry7 = tk.Entry(window, background="#cae4ff", disabledforeground="#a3a3a3", font="TkFixedFont",
                               foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black",
                               insertbackground="black", selectbackground="blue", selectforeground="white")
        self.Entry7.place(relx=0.511, rely=0.725, height=20, relwidth=0.302)

        self.Entry8 = tk.Entry(window, background="#cae4ff", disabledforeground="#a3a3a3", font="TkFixedFont",
                               foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black",
                               insertbackground="black", selectbackground="blue", selectforeground="white")
        self.Entry8.place(relx=0.511, rely=0.81, height=20, relwidth=0.302)

        self.Label8 = tk.Label(window, activebackground="#f9f9f9", activeforeground="black", background="#f2f3f4",
                               disabledforeground="#a3a3a3", foreground="#000000", highlightbackground="#d9d9d9",
                               highlightcolor="black", text='''PIN:''')
        self.Label8.place(relx=0.414, rely=0.64, height=18, width=35)

        self.Label9 = tk.Label(window, activebackground="#f9f9f9", activeforeground="black", background="#f2f3f4",
                               cursor="fleur", disabledforeground="#a3a3a3", foreground="#000000",
                               highlightbackground="#d9d9d9", highlightcolor="black", text='''Re-enter PIN:''')
        self.Label9.place(relx=0.307, rely=0.725, height=18, width=75)

        self.Label10 = tk.Label(window, activebackground="#f9f9f9", activeforeground="black", background="#f2f3f4",
                                disabledforeground="#a3a3a3", foreground="#000000", highlightbackground="#d9d9d9",
                                highlightcolor="black", text='''Initial balance:''')
        self.Label10.place(relx=0.297, rely=0.81, height=18, width=75)

        self.Button1 = tk.Button(window, activebackground="#ececec", activeforeground="#000000", background="#004080",
                                 borderwidth="0", disabledforeground="#a3a3a3", foreground="#ffffff",
                                 highlightbackground="#d9d9d9", highlightcolor="black", pady="0", text='''Back''',
                                 command=self.back)
        self.Button1.place(relx=0.219, rely=0.907, height=24, width=67)

        self.Button2 = tk.Button(window, activebackground="#ececec", activeforeground="#000000", background="#004080",
                                 borderwidth="0", disabledforeground="#a3a3a3", foreground="#ffffff",
                                 highlightbackground="#d9d9d9", highlightcolor="black", pady="0", text='''Proceed''',command = lambda:create_acc(self.Entry1.get(),self.Entry2.get(),self.Entry3.get(),self.Entry4.get(),self.Entry5.get(),self.Entry6.get(),self.Entry7.get(),self.Entry8.get(),self.Entry2.get(),self.Entry2.get()))
        self.Button2.place(relx=0.633, rely=0.907, height=24, width=67)

    def back(self):
        self.master.withdraw()
        adminMenu(Toplevel(self.master))
        
    def create_acc(self,customer_account_number,name,account_type,date_of_birth,mobile_number,gender,nationality,PIN,confirm_PIN,initial_balance,date_of_account_creation,KYC_document):
        self.master.withdraw()
        print("Customer account created successfully !")
        adminMenu(Toplevel(self.master))


class createAdmin:
    def __init__(self, window=None):
        self.master = window
        window.geometry("411x150+512+237")
        window.minsize(120, 1)
        window.maxsize(1370, 749)
        window.resizable(1, 1)
        window.title("Create admin account")
        window.configure(background="#f2f3f4")

        self.Label1 = tk.Label(window, background="#f2f3f4", disabledforeground="#a3a3a3", foreground="#000000",
                               text='''Enter admin ID:''')
        self.Label1.place(relx=0.219, rely=0.067, height=27, width=104)

        self.Label2 = tk.Label(window, background="#f2f3f4", disabledforeground="#a3a3a3", foreground="#000000",
                               text='''Enter password:''')
        self.Label2.place(relx=0.219, rely=0.267, height=27, width=104)

        self.Entry1 = tk.Entry(window, background="#cae4ff", disabledforeground="#a3a3a3", font="TkFixedFont",
                               foreground="#000000", insertbackground="black")
        self.Entry1.place(relx=0.487, rely=0.087, height=20, relwidth=0.326)

        self.Entry2 = tk.Entry(window, background="#cae4ff", disabledforeground="#a3a3a3", font="TkFixedFont",
                               foreground="#000000", insertbackground="black")
        self.Entry2.place(relx=0.487, rely=0.287, height=20, relwidth=0.326)

        self.Label3 = tk.Label(window, activebackground="#f9f9f9", activeforeground="black", background="#f2f3f4",
                               disabledforeground="#a3a3a3", foreground="#000000", highlightbackground="#d9d9d9",
                               highlightcolor="black", text='''Confirm password:''')
        self.Label3.place(relx=0.195, rely=0.467, height=27, width=104)

        self.Entry3 = tk.Entry(window, background="#cae4ff", disabledforeground="#a3a3a3", font="TkFixedFont",
                               foreground="#000000", insertbackground="black")
        self.Entry3.place(relx=0.487, rely=0.487, height=20, relwidth=0.326)

        self.Button1 = tk.Button(window, activebackground="#ececec", activeforeground="#000000", background="#004080",
                                 borderwidth="0", disabledforeground="#a3a3a3", foreground="#ffffff",
                                 highlightbackground="#d9d9d9", highlightcolor="black", pady="0", text="Proceed")
        self.Button1.place(relx=0.598, rely=0.733, height=24, width=67)

        self.Button2 = tk.Button(window, activebackground="#ececec", activeforeground="#000000", background="#004080",
                                 borderwidth="0", disabledforeground="#a3a3a3", foreground="#ffffff",
                                 highlightbackground="#d9d9d9", highlightcolor="black", pady="0", text="Back",
                                 command=self.back)
        self.Button2.place(relx=0.230, rely=0.733, height=24, width=67)

    def back(self):
        self.master.withdraw()
        adminMenu(Toplevel(self.master))


class deleteAdmin:
    def __init__(self, window=None):
        self.master = window
        window.geometry("411x117+504+268")
        window.minsize(120, 1)
        window.maxsize(1370, 749)
        window.resizable(0, 0)
        window.title("Delete admin account")
        window.configure(background="#f2f3f4")

        self.Entry1 = tk.Entry(window, background="#cae4ff", disabledforeground="#a3a3a3", font="TkFixedFont",
                               foreground="#000000", insertbackground="black")
        self.Entry1.place(relx=0.487, rely=0.092, height=20, relwidth=0.277)

        self.Label1 = tk.Label(window, background="#f2f3f4", disabledforeground="#a3a3a3", foreground="#000000",
                               text='''Enter admin ID:''')
        self.Label1.place(relx=0.219, rely=0.092, height=21, width=104)

        self.Label2 = tk.Label(window, background="#f2f3f4", disabledforeground="#a3a3a3", foreground="#000000",
                               text='''Enter password:''')
        self.Label2.place(relx=0.209, rely=0.33, height=21, width=109)

        self.Entry1_1 = tk.Entry(window, background="#cae4ff", disabledforeground="#a3a3a3", font="TkFixedFont",
                                 foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black",
                                 insertbackground="black", selectbackground="blue", selectforeground="white")
        self.Entry1_1.place(relx=0.487, rely=0.33, height=20, relwidth=0.277)

        self.Button1 = tk.Button(window, activebackground="#ececec", activeforeground="#000000", background="#004080",
                                 borderwidth="0", disabledforeground="#a3a3a3", foreground="#ffffff",
                                 highlightbackground="#d9d9d9", highlightcolor="black", pady="0", text='''Back''',
                                 command=self.back)
        self.Button1.place(relx=0.243, rely=0.642, height=24, width=67)

        self.Button2 = tk.Button(window, activebackground="#ececec", activeforeground="#000000", background="#004080",
                                 borderwidth="0", disabledforeground="#a3a3a3", foreground="#ffffff",
                                 highlightbackground="#d9d9d9", highlightcolor="black", pady="0", text='''Proceed''')
        self.Button2.place(relx=0.608, rely=0.642, height=24, width=67)

    def back(self):
        self.master.withdraw()
        adminMenu(Toplevel(self.master))


class customerMenu:
    def __init__(self, window=None):
        self.master = window
        window.geometry("743x494+329+153")
        window.minsize(120, 1)
        window.maxsize(1370, 749)
        window.resizable(0, 0)
        window.title("New Toplevel")
        window.configure(background="#00254a")

        self.Labelframe1 = tk.LabelFrame(window, relief='groove', font="-family {Segoe UI} -size 13 -weight bold",
                                         foreground="#000000", text='''Select your option''', background="#fffffe")
        self.Labelframe1.place(relx=0.081, rely=0.081, relheight=0.415, relwidth=0.848)

        self.Button1 = tk.Button(self.Labelframe1, command=self.selectWithdraw, activebackground="#ececec",
                                 activeforeground="#000000", background="#39a9fc", borderwidth="0",
                                 disabledforeground="#a3a3a3", font="-family {Segoe UI} -size 11", foreground="#fffffe",
                                 highlightbackground="#d9d9d9", highlightcolor="black", pady="0", text='''Withdraw''')
        self.Button1.place(relx=0.667, rely=0.195, height=34, width=181, bordermode='ignore')

        self.Button2 = tk.Button(self.Labelframe1, command=self.selectDeposit, activebackground="#ececec",
                                 activeforeground="#000000", background="#39a9fc", borderwidth="0",
                                 disabledforeground="#a3a3a3", font="-family {Segoe UI} -size 11", foreground="#fffffe",
                                 highlightbackground="#d9d9d9", highlightcolor="black", pady="0", text='''Deposit''')
        self.Button2.place(relx=0.04, rely=0.195, height=34, width=181, bordermode='ignore')

        self.Button3 = tk.Button(self.Labelframe1, command=self.exit, activebackground="#ececec",
                                 activeforeground="#000000",
                                 background="#39a9fc",
                                 borderwidth="0", disabledforeground="#a3a3a3", font="-family {Segoe UI} -size 11",
                                 foreground="#fffffe", highlightbackground="#d9d9d9", highlightcolor="black", pady="0",
                                 text='''Exit''')
        self.Button3.place(relx=0.667, rely=0.683, height=34, width=181, bordermode='ignore')

        self.Button4 = tk.Button(self.Labelframe1, command=self.selectChangePIN, activebackground="#ececec",
                                 activeforeground="#000000", background="#39a9fc", borderwidth="0",
                                 disabledforeground="#a3a3a3", font="-family {Segoe UI} -size 11", foreground="#fffffe",
                                 highlightbackground="#d9d9d9", highlightcolor="black", pady="0", text='''Change PIN''')
        self.Button4.place(relx=0.04, rely=0.439, height=34, width=181, bordermode='ignore')

        self.Button5 = tk.Button(self.Labelframe1, command=self.selectCloseAccount, activebackground="#ececec",
                                 activeforeground="#000000", background="#39a9fc", borderwidth="0",
                                 disabledforeground="#a3a3a3", font="-family {Segoe UI} -size 11", foreground="#fffffe",
                                 highlightbackground="#d9d9d9", highlightcolor="black", pady="0",
                                 text='''Close account''')
        self.Button5.place(relx=0.667, rely=0.439, height=34, width=181, bordermode='ignore')

        self.Button6 = tk.Button(self.Labelframe1, activebackground="#ececec", activeforeground="#000000",
                                 background="#39a9fc", borderwidth="0", disabledforeground="#a3a3a3",
                                 font="-family {Segoe UI} -size 11", foreground="#fffffe",
                                 highlightbackground="#d9d9d9", highlightcolor="black", pady="0",
                                 text='''Check your balance''')
        self.Button6.place(relx=0.04, rely=0.683, height=34, width=181, bordermode='ignore')

        self.Frame1 = tk.Frame(window, relief='groove', borderwidth="2", background="#fffffe")
        self.Frame1.place(relx=0.081, rely=0.547, relheight=0.415, relwidth=0.848)

    def selectDeposit(self):
        self.master.withdraw()
        depositMoney(Toplevel(self.master))

    def selectWithdraw(self):
        self.master.withdraw()
        withdrawMoney(Toplevel(self.master))

    def selectChangePIN(self):
        self.master.withdraw()
        changePIN(Toplevel(self.master))

    def selectCloseAccount(self):
        self.master.withdraw()
        closeAccount(Toplevel(self.master))

    def exit(self):
        self.master.withdraw()
        customerLogin(Toplevel(self.master))


class depositMoney:
    def __init__(self, window=None):
        self.master = window
        window.geometry("411x117+519+278")
        window.minsize(120, 1)
        window.maxsize(1370, 749)
        window.resizable(0, 0)
        window.title("Deposit money")
        p1 = PhotoImage(file='./images/deposit_icon.png')
        window.iconphoto(True, p1)
        window.configure(borderwidth="2")
        window.configure(background="#f2f3f4")

        self.Label1 = tk.Label(window, background="#f2f3f4", disabledforeground="#a3a3a3",
                               font="-family {Segoe UI} -size 9", foreground="#000000", borderwidth="0",
                               text='''Enter amount to deposit :''')
        self.Label1.place(relx=0.146, rely=0.171, height=21, width=164)

        self.Entry1 = tk.Entry(window, background="#cae4ff", disabledforeground="#a3a3a3", font="TkFixedFont",
                               foreground="#000000", insertbackground="black", selectforeground="#ffffffffffff")
        self.Entry1.place(relx=0.535, rely=0.171, height=20, relwidth=0.253)

        self.Button1 = tk.Button(window, activebackground="#ececec", activeforeground="#000000", background="#004080",
                                 disabledforeground="#a3a3a3", borderwidth="0", foreground="#ffffff",
                                 highlightbackground="#000000",
                                 highlightcolor="black", pady="0", text='''Proceed''')
        self.Button1.place(relx=0.56, rely=0.598, height=24, width=67)

        self.Button2 = tk.Button(window, activebackground="#ececec", activeforeground="#000000", background="#004080",
                                 disabledforeground="#a3a3a3", font="-family {Segoe UI} -size 9", foreground="#ffffff",
                                 highlightbackground="#d9d9d9", borderwidth="0", highlightcolor="black", pady="0",
                                 text='''Back''',
                                 command=self.back)
        self.Button2.place(relx=0.268, rely=0.598, height=24, width=67)

    def back(self):
        self.master.withdraw()
        customerMenu(Toplevel(self.master))


class withdrawMoney:
    def __init__(self, window=None):
        self.master = window
        window.geometry("411x117+519+278")
        window.minsize(120, 1)
        window.maxsize(1370, 749)
        window.resizable(0, 0)
        window.title("Withdraw money")
        p1 = PhotoImage(file='./images/withdraw_icon.png')
        window.iconphoto(True, p1)
        window.configure(borderwidth="2")
        window.configure(background="#f2f3f4")

        self.Label1 = tk.Label(window, background="#f2f3f4", disabledforeground="#a3a3a3",
                               font="-family {Segoe UI} -size 9", foreground="#000000",
                               text='''Enter amount to withdraw :''')
        self.Label1.place(relx=0.146, rely=0.171, height=21, width=164)

        self.Entry1 = tk.Entry(window, background="#cae4ff", disabledforeground="#a3a3a3", font="TkFixedFont",
                               foreground="#000000", insertbackground="black", selectforeground="#ffffffffffff")
        self.Entry1.place(relx=0.535, rely=0.171, height=20, relwidth=0.253)

        self.Button1 = tk.Button(window, activebackground="#ececec", activeforeground="#000000", background="#004080",
                                 disabledforeground="#a3a3a3", borderwidth="0", foreground="#ffffff",
                                 highlightbackground="#000000",
                                 highlightcolor="black", pady="0", text='''Proceed''')
        self.Button1.place(relx=0.56, rely=0.598, height=24, width=67)

        self.Button2 = tk.Button(window, activebackground="#ececec", activeforeground="#000000", background="#004080",
                                 disabledforeground="#a3a3a3", borderwidth="0", font="-family {Segoe UI} -size 9",
                                 foreground="#ffffff",
                                 highlightbackground="#d9d9d9", highlightcolor="black", pady="0", text='''Back''',
                                 command=self.back)
        self.Button2.place(relx=0.268, rely=0.598, height=24, width=67)

    def back(self):
        self.master.withdraw()
        customerMenu(Toplevel(self.master))


class changePIN:
    def __init__(self, window=None):
        self.master = window
        window.geometry("411x111+505+223")
        window.minsize(120, 1)
        window.maxsize(1370, 749)
        window.resizable(0, 0)
        window.title("Change PIN")
        window.configure(background="#f2f3f4")

        self.Label1 = tk.Label(window, background="#f2f3f4", disabledforeground="#a3a3a3", foreground="#000000",
                               text='''Enter new PIN:''')
        self.Label1.place(relx=0.243, rely=0.144, height=21, width=93)

        self.Label2 = tk.Label(window, background="#f2f3f4", disabledforeground="#a3a3a3", foreground="#000000",
                               text='''Confirm PIN:''')
        self.Label2.place(relx=0.268, rely=0.414, height=21, width=82)

        self.Entry1 = tk.Entry(window, background="#cae4ff", disabledforeground="#a3a3a3", font="TkFixedFont",
                               foreground="#000000", insertbackground="black")
        self.Entry1.place(relx=0.528, rely=0.144, height=20, relwidth=0.229)

        self.Entry2 = tk.Entry(window, background="#cae4ff", disabledforeground="#a3a3a3", font="TkFixedFont",
                               foreground="#000000", insertbackground="black")
        self.Entry2.place(relx=0.528, rely=0.414, height=20, relwidth=0.229)

        self.Button1 = tk.Button(window, activebackground="#ececec", activeforeground="#000000", background="#004080",
                                 disabledforeground="#a3a3a3", foreground="#ffffff", borderwidth="0",
                                 highlightbackground="#d9d9d9",
                                 highlightcolor="black", pady="0", text='''Proceed''')
        self.Button1.place(relx=0.614, rely=0.721, height=24, width=67)

        self.Button2 = tk.Button(window, activebackground="#ececec", activeforeground="#000000", background="#004080",
                                 disabledforeground="#a3a3a3", foreground="#ffffff", borderwidth="0",
                                 highlightbackground="#d9d9d9",
                                 highlightcolor="black", pady="0", text="Back", command=self.back)
        self.Button2.place(relx=0.214, rely=0.721, height=24, width=67)

    def back(self):
        self.master.withdraw()
        customerMenu(Toplevel(self.master))


class closeAccount:
    def __init__(self, window=None):
        self.master = window
        window.geometry("411x117+498+261")
        window.minsize(120, 1)
        window.maxsize(1370, 749)
        window.resizable(0, 0)
        window.title("New Toplevel")
        window.configure(background="#f2f3f4")

        self.Label1 = tk.Label(window, background="#f2f3f4", disabledforeground="#a3a3a3", foreground="#000000",
                               text='''Enter your PIN:''')
        self.Label1.place(relx=0.268, rely=0.256, height=21, width=94)

        self.Entry1 = tk.Entry(window, show="*", background="#cae4ff", disabledforeground="#a3a3a3", font="TkFixedFont",
                               foreground="#000000", insertbackground="black")
        self.Entry1.place(relx=0.511, rely=0.256, height=20, relwidth=0.229)

        self.Button1 = tk.Button(window, activebackground="#ececec", activeforeground="#000000", background="#004080",
                                 disabledforeground="#a3a3a3", foreground="#ffffff", borderwidth="0",
                                 highlightbackground="#d9d9d9",
                                 highlightcolor="black", pady="0", text='''Proceed''')
        self.Button1.place(relx=0.614, rely=0.712, height=24, width=67)

        self.Button2 = tk.Button(window, activebackground="#ececec", activeforeground="#000000", background="#004080",
                                 disabledforeground="#a3a3a3", foreground="#ffffff", borderwidth="0",
                                 highlightbackground="#d9d9d9",
                                 highlightcolor="black", pady="0", text="Back", command=self.back)
        self.Button2.place(relx=0.214, rely=0.712, height=24, width=67)

    def back(self):
        self.master.withdraw()
        customerMenu(Toplevel(self.master))


root = tk.Tk()
top = welcomeScreen(root)
root.mainloop()

# Tkinter GUI code ends.