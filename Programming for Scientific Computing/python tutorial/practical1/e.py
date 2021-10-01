#!/usr/bin/env python3

def findGCD(number1,number2):
	if(number2==0):
		return number1
	return findGCD(number2, number1%number2)
def isCoPrime(number1,number2):
	if(findGCD(number1, number2)==1):
		return True
	return False

#Driver code
number1 = int(input("Enter first number : "))
number2 = int(input("Enter second number : "))
if(isCoPrime(number1, number2)):
	print("The number ",number1," and ",number2," are CO-PRIME.")
else:
	print("The number ",number1," and ",number2," are NOT CO-PRIME.")
	
# example : 5 and 6 -> CO-PRIME
# example : 8 and 16 -> NOT CO-PRIME