# PSC LPW
# 19BCE245 | SHAH AAYUSH
"""
create a billing System
create a random list of price with the commodities
the customer can view the availability of items
create the billing for daily sales
plot the graph of daily sale for the items
find the 5 most selling items
give discount of 20% during happy hours (3:00 pm - 5:00 pm)
"""

import random
from prettytable import PrettyTable
import matplotlib.pyplot as plt
from datetime import datetime

global top_selling_items
top_selling_items = []

def list_items(commodities_list,isAvailable):
	counter = 0
	if isAvailable:
		print(f"List of available items : ")
	else:
		print(f"List of {len(commodities_list)} items : ")
	for commodity in commodities_list:
		if isAvailable:
			if commodity['Quantity']>0:
				print("Item",counter+1,":")
				print("\tName :",commodity['Name'])
				print("\tPrice :",commodity['Price'])
				print("\tAvailable Quantity :",commodity['Quantity'],"\n")
		else:
			print("Item",counter+1,":")
			print("\tName :",commodity['Name'])
			print("\tPrice :",commodity['Price'])
			print("\tAvailable Quantity :",commodity['Quantity'],"\n")
		counter+=1

def purchase(commodities_list):
	number = int(input("Enter the number of items you want to purchase : "))
	purchased_list = []
	for i in range(number):
		print(f"For purchase of item no {i+1} : ")
		id = int(input(f"\tEnter item id [1-{len(commodities_list)}] :"))
		if id<0 or id>len(commodities_list):
			print("\t\tITEM DOESN'T EXISTS.")
			continue
		if commodities_list[id-1]['Quantity']>0:
			qty = int(input("\tEnter quantity : "))
			if qty<=commodities_list[id-1]['Quantity']:
				print("\t\tITEM ADDED TO CART.")
				item = {'ID':id-1,'QTY':qty}
				purchased_list.append(item)
				
				commodities_list[id-1]['Quantity']-=item['QTY'] 
			else:
				print("\t\tNOT ENOUGH ITEMS AVAILABLE.")				
		else:
			print(f"\t\t{commodities_list[id-1]['Name']} is not available.")
	
	Bill = PrettyTable(["Item Name", "Price per unit", "Quantity", "Total Price"])
	
	print("\n\nFINAL BILL : ")
	total_price = 0
	total_qty = 0
	for item in purchased_list:
		item_name = commodities_list[item['ID']]['Name']
		item_qty = item['QTY']
		item_price = commodities_list[item['ID']]['Price']
		item_total_price = item_qty*item_price
		Bill.add_row([item_name, item_price, item_qty, item_total_price])
		
		total_price += item_total_price
		total_qty += item_qty
		
		global top_selling_items
		top_selling_items[item['ID']] += item['QTY']
	
	final_amount = PrettyTable(["TOTAL QUANTITY",total_qty])
	final_amount.add_row(["TOTAL PRICE",total_price])
	
	
	now = datetime.now()	
	current_time = now.strftime("%H:%M:%S")
	
	final_amount.add_row(["TIME OF PURCHASE",current_time])
	
#	print("CURRENT HOUR : ",int(current_time.split(':')[0]))
	
	if int(current_time.split(':')[0])>=15 and int(current_time.split(':')[0])<=17:
		final_amount.add_row(["HAPPY HOURS | DISCOUNT APPLIED (20%)",round(total_price*0.2,2)])
		final_amount.add_row(["FINAL PRICE",round(total_price*0.8,2)])
		
#	print(purchased_list)
#	print(top_selling_items)
	print(Bill)
	print(final_amount)

def GenerateGraph(commodities_list):
	Quantity=[]
	Name=[]
	for i in range(len(commodities_list)):
		Quantity.append(commodities_list[i]['Quantity'])
		Name.append(commodities_list[i]['Name'])
	plt.figure(figsize = (15,8))
	plt.plot(Name,Quantity,color="r")
	plt.xlabel('Item Name')
	plt.ylabel('Quantity')
	plt.show()

def GenerateGraphTop(top_items):
	Quantity=[]
	Name=[]
	for i in range(len(top_items)):
		Quantity.append(top_items[i]['Quantity Sold'])
		Name.append(top_items[i]['Name'])
	plt.figure(figsize = (15,8))
	plt.plot(Name,Quantity,color="r")
	plt.xlabel('Item Name')
	plt.ylabel('Quantity Sold')
	plt.show()

def topSelling():
	print("TOP SELLING ITEMS : ")
	top_table = PrettyTable(["Item Name", "Quantity sold", "Income"])
	
	global top_selling_items
	
	top_items = []
	for i in range(len(top_selling_items)):
		item = {
			'Name':commodities_list[i]['Name'],
			'Quantity Sold':top_selling_items[i],
			'Income':commodities_list[i]['Price']*top_selling_items[i]
		}
		top_items.append(item)
	
	top_items = sorted(top_items, key = lambda i: i['Quantity Sold'],reverse=True)
	
	counter=0
	for item in top_items:
		counter+=1
		top_table.add_row([item['Name'],item['Quantity Sold'],item['Income']])
		if counter==5:
			break
		
	print(top_table)
	GenerateGraphTop(top_items[0:6])
	
#	copy_top_selling = top_selling_items
#	
#	top_items = []
#	max_val = 0
#	for i in range(5):
#		top_table = PrettyTable(["Item Name", "Quantity sold", "Income"])
#		max_val = max(copy_top_selling)
#		for i in range(12):
#			if max_val==copy_top_selling[i]:
#				top_table.add_row([commodities_list[i]['Name'],copy_top_selling[i],commodities_list[i]['Price']*copy_top_selling[i]])
#		
#		print(f"TOP {i+1} :\n",top_table)
		

if __name__ == "__main__":
	commodities_list = [
		{
			'Name':'Coffee',
			'Price':random.randrange(20, 200, 3),
			'Quantity':random.randrange(0, 10, 1)
		},
		{
			'Name':'Mango',
			'Price':random.randrange(20, 200, 3),
			'Quantity':random.randrange(0, 10, 1)
		},
		{
			'Name':'Apple',
			'Price':random.randrange(20, 200, 3),
			'Quantity':random.randrange(0, 10, 1)
		},
		{
			'Name':'Cotton',
			'Price':random.randrange(20, 200, 3),
			'Quantity':random.randrange(0, 10, 1)
		},
		{
			'Name':'Oil',
			'Price':random.randrange(20, 200, 3),
			'Quantity':random.randrange(0, 10, 1)
		},
		{
			'Name':'Gas',
			'Price':random.randrange(20, 200, 3),
			'Quantity':random.randrange(0, 10, 1)
		},
		{
			'Name':'Corn',
			'Price':random.randrange(20, 200, 3),
			'Quantity':random.randrange(0, 10, 1)
		},
		{
			'Name':'Wheat',
			'Price':random.randrange(20, 200, 3),
			'Quantity':random.randrange(0, 10, 1)
		},
		{
			'Name':'Oranges',
			'Price':random.randrange(20, 200, 3),
			'Quantity':random.randrange(0, 10, 1)
		},
		{
			'Name':'Gold',
			'Price':random.randrange(20, 200, 3),
			'Quantity':random.randrange(0, 10, 1)
		},
		{
			'Name':'Uranium',
			'Price':random.randrange(20, 200, 3),
			'Quantity':random.randrange(0, 10, 1)
		},
		{
			'Name':'Cloths',
			'Price':random.randrange(20, 200, 3),
			'Quantity':random.randrange(0, 10, 1)
		}
	]
	
	for i in range(len(commodities_list)):
		top_selling_items.append(0)
#	print(top_selling_items)		# contains total sells of qty of items
		
	
	print("**** WELCOME TO BILLING SYSTEM ****")
	
	#print(len(commodities_list))
	
	
	while(True):
		print("MENU : ")
		print("\t[1.] List of all items ")
		print("\t[2.] List of all available items ")
		print("\t[3.] Purchase ")
		print("\t[4.] Generate graph for daily sales ")
		print("\t[5.] Top selling items ")
		print("\t[6.] Exit ")
		choice = int(input("Enter choice : "))
		
		if choice==1:
			list_items(commodities_list,False)
		elif choice==2:
			list_items(commodities_list,True)
		elif choice==3:
			purchase(commodities_list)
		elif choice==4:
			GenerateGraph(commodities_list)
		elif choice==5:
			topSelling()
		elif choice==6:
			print("Thank you for shopping :)")
			break




#print(commodities_list[2]['Price'])

#print(commodities)
#for i in range(5):
#	item, price = random.choice(list(commodities.items()))
#	print(item,price)
	
	