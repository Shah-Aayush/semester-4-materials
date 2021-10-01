#!/usr/bin/env python3

#Create scientific calculator using numpy API.

import numpy

def addition(n1,n2):
	return (n1+n2)

def subtraction(n1,n2):
	return (n1-n2)

def multiplication(n1,n2):
	return (n1*n2)

def division(n1,n2):
	while (n2==0):
		n2 = float(input("Denominator must be non-zero :(\nEnter again : "))
	return (n1/n2)

def modulo(n1,n2):
	return (n1%n2)

def power(n1,n2):
	return n1**n2

def qube_root(n1):
	while (n1<0):
		n1 = float(input("Non-negative value expected :(\nEnter again :"))
	return n1**(1/3)

def square_root(n1):
	while (n1<0):
		n1 = float(input("Non-negative value expected :(\nEnter again :"))
	return numpy.sqrt(n1)

def sine(n1):
	return numpy.sin(n1)

def a_sine(n1):
	return numpy.arcsine(n1)

def cos(n1):
	return numpy.cos(n1)

def a_cos(n1):
	return numpy.arccos(n1)

def tan(n1):
	return numpy.tan(n1)

def a_tan(n1):
	return numpy.arctan(n1)

def log_base10(n1):
	return numpy.log10(n1)

def log_baseE(n1):
	return numpy.log(n1)

def degree_to_rad(n1):
	return numpy.deg2rad(n1)

if __name__ == "__main__":
	while True:
		print("OPTIONS : ")
		print("\t[0. ] Exit")
		print("\t[1. ] Addition")
		print("\t[2. ] Subtraction")
		print("\t[3. ] Multiplication")
		print("\t[4. ] Division")
		print("\t[5. ] Modulo")
		print("\t[6. ] Power")
		print("\t[7. ] Degree to Radians")
		print("\t[8. ] Square root")
		print("\t[9. ] Qube root")
		print("\t[10.] Sine")
		print("\t[11.] aSine")
		print("\t[12.] Cos")
		print("\t[13.] aCos")
		print("\t[14.] Tan")
		print("\t[15.] aTan")
		print("\t[16.] Log")
		print("\t[17.] ln")
		choice = int(input("CHOICE : "))
		if(choice == 0):
			print("THANK YOU for using SCIENTIFIC CALCULATOR !")
			break
		elif(choice == 1):
			n1 = float(input("Enter first number : "))
			n2 = float(input("Enter second number : "))
			print(n1,"+",n2,"=",addition(n1,n2))
		elif(choice == 2):
			n1 = float(input("Enter first number : "))
			n2 = float(input("Enter second number : "))
			print(n1,"-",n2,"=",subtraction(n1,n2))
		elif(choice == 3):
			n1 = float(input("Enter first number : "))
			n2 = float(input("Enter second number : "))
			print(n1,"*",n2,"=",multiplication(n1,n2))
		elif(choice == 4):
			n1 = float(input("Enter first number : "))
			n2 = float(input("Enter second number : "))
			print(n1,"/",n2,"=",division(n1,n2))
		elif(choice == 5):
			n1 = float(input("Enter first number : "))
			n2 = float(input("Enter second number : "))
			print(n1,"%",n2,"=",modulo(n1,n2))
		elif(choice == 6):
			n1 = float(input("Enter base : "))
			n2 = float(input("Enter power : "))
			print(n1,"^(",n2,") =",power(n1,n2))
		elif(choice == 7):
			n1 = float(input("Enter degree : "))
			print("radians of",n1," : ",degree_to_rad(n1))
		elif(choice == 8):
			n1 = float(input("Enter number : "))
			print("square root of",n1,"=",square_root(n1))
		elif(choice == 9):
			n1 = float(input("Enter value : "))
			print("qube of",n1,"=",qube_root(n1))
		elif(choice == 10):
			n1 = float(input("Enter value : "))
			print("a sine of",n1,"=",sine(n1))
		elif(choice == 11):
			n1 = float(input("Enter value : "))
			print("a sine of",n1,"=",a_sine(n1))
		elif(choice == 12):
			n1 = float(input("Enter value : "))
			print("a cos of",n1,"=",cos(n1))
		elif(choice == 13):
			n1 = float(input("Enter value : "))
			print("a acos of",n1,"=",a_cos(n1))
		elif(choice == 14):
			n1 = float(input("Enter value : "))
			print("a tan of",n1,"=",tan(n1))
		elif(choice == 15):
			n1 = float(input("Enter value : "))
			print("a atan of",n1,"=",a_tan(n1))
		elif(choice == 16):
			n1 = float(input("Enter value : "))
			print("a log10 of",n1,"=",log_base10(n1))
		elif(choice == 17):
			n1 = float(input("Enter value : "))
			print("a logE of",n1,"=",log_baseE(n1))
		else:
			print("Invalid choice :(")