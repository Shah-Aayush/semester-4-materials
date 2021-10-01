#!/usr/bin/env python3

"""
This code is written by :

1. 19BCE237 - Sakshi Sanghavi
2. 19BCE238 - Harshil Sanghvi
3. 19BCE245 - Aayush Shah

"""

import os	#for creating directories Admin/Customer if it is not exists.
from datetime import date		#for date of account creation when new customer account is created.

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
			numOfDays = mon[month - 1];
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


#Class Main : which has main method from which the execution starts
if __name__ == "__main__":
	print("\n*** Welcome to Nirma Bank, Nirma University Branch! ***")
	
	while True :
		#Asking user to elect the role(Banker/Customer)
		print("\n-------------------------")
		print("\tEnter your choice:")
		print("-------------------------")
		print("1. Banker")
		print("2. Customer")
		print("3. Exit")
		choice = int(input("\n\tChoice: "))
		
		#According the choice of user calling methods from project class using the objects declared above.
		if(choice == 1):	#If user chooses to operate as a banker
			id = str(input("\nPlease enter admin id : "))
			password = str(input("Please enter admin password : "))
			if(check_credentials(id, password, 1,True)):
				banker_functions()
			else:
				print("\n# Please enter valid credentials! #")
				
		elif(choice == 2):	#If user chooses to operate as a customer
			id = str(input("\nPlease enter account number : "))
			password = str(input("Please enter PIN : "))
			if(check_credentials(id, password, 2,False)):
				customer_functions(id)
			else:
				print("\n# Please enter valid credentials! #")
			
		elif(choice == 3):	
			print("\n*** Thank you ***")
			break
		
		else:		#If user enters invalid choice, then the following message is displayed
			print("# Invalid choice :(")