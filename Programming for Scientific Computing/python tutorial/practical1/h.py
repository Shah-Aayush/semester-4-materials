#!/usr/bin/env python3

#Write a recursive function that takes x value as an input parameter and print x-digit strictly in increasing number. [i.e. x = 6 than output 67891011]

def printInc(x,count):
	if(count==0):
		return
	print(x, end="")
	printInc(x+1,count-1)
	
#Driver code
if __name__ == "__main__":
	x = int(input("Enter number : "))
	printInc(x, x)