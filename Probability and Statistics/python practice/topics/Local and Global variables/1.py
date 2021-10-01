#!/usr/bin/python

#global variable in python

#global variable
def global_var():
	print("Global var : ",string1)
	
#global variable with local variable
def local_var():
	string1 = "I am not Aayush"
	print("Local var : ",string1)
	
#global variable inside function
def global_in_fun():
	global string1
	print("Before fun : ",string1)
	string1 = "I am Aayush"
	print("After fun : ",string1)
	
if __name__ == "__main__":
	string1 = "I am Aayush Shah"
	global_var()
	local_var()
	global_in_fun()
	print("Final : ",string1)

	