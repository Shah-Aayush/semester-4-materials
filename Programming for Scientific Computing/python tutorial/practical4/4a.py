#!/usr/bin/env python3

class Bank:
	def __init__(self, name, accountNum, type, amount):
		self.name = name
		self.accountNum = accountNum
		self.type = type
		self.amount = amount
		self.interest = self.findInterest()
		
	def deposit(self, dep_money):
		self.amount += dep_money
		
	def withdrawal(self, wit_money):
		self.amount -= wit_money
		
	def findInterest(self):
		if(self.amount < 100000):
			return (self.amount*.03)
		elif(self.amount < 300000):
			return (self.amount*.05)
		elif(self.amount < 500000):
			return (self.amount*.07)
		else:
			return (self.amount*.08)
	
	def details(self):
		print("Name : ",self.name)
		print("Account number : ",self.accountNum)
		print("Account type : ",self.type)
		print("Interest : ",self.interest)

if __name__ == "__main__":
	customer1 = Bank("Aayush", 1234, "Savings", 200000)
	customer1 = Bank(str(input("Enter name : ")), int(input("Enter account number : ")), str(input("Enter account type : ")), int(input("Enter amount : ")))
#	print("Customer name : ",customer1.name)
#	print("Customer account number : ",customer1.accountNum)
#	print("Customer type : ",customer1.type)
#	print("Customer amount : ",customer1.amount)
#	print("Customer interest : ",customer1.interest)
	
#	customer1.deposit(1000)
#	print("Money after deposit of 1000 rs. : ",customer1.amount)
#	customer1.withdrawal(2000)
#	print("Money after withdrawal of 2000 rs. : ",customer1.amount)

	while (True):
		print("MENU : ")
		print("\t[1.] Account details")
		print("\t[2.] Check Balance")
		print("\t[3.] Deposit amount")
		print("\t[4.] Withdraw amount")
		print("\t[5.] Exit")
		choice = int(input("Enter choice : "))
		if(choice == 1):
			customer1.details()
		elif(choice == 2):
			print("Current Balance : ",customer1.amount)
		elif(choice == 3):
			customer1.deposit(float(input("Enter amount : ")))
			print("Updated balance : ",customer1.amount)
		elif(choice == 4):
			customer1.withdrawal(float(input("Enter amount : ")))
			print("Updated balance : ",customer1.amount)
		elif(choice == 5):
			print("Thank you!")
			break
		else:
			print("Invalid choice :(")