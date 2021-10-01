#!/usr/bin/env python3

#Pass by value and Pass by Reference in  python

def add(list):	#pass by ref
	list.append("B")
	print("Inside add() : ",list)
	return list
def change(list):	#pass by val
	list = ["B"]
	print("Inside change() : ",list)
	return list

if __name__ == "__main__":
	mylist= ["X"]
	print("Before add() : ",mylist)
	add(mylist)
	print("After add() : ",mylist)
	mylist= ["X"]
	print("Before change() : ",mylist)
	change(mylist)
	print("After change() : ",mylist)
	