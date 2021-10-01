#!/usr/bin/env python3

# Design a python program which implements the bisection and false positioning method.

def calculate_value(x):
	return sum([float(a)*pow(float(x),float(b)) for a,b in zip(coeff_list,power_list)])

def bisection(a,b):
	if calculate_value(a)*calculate_value(b)>=0:
		return False,0
	
	c = a
	while (b-a)>=0.01:
		c = (a+b)/2
		if calculate_value(c)==0.0:
			return True,c
		if calculate_value(c)*calculate_value(a)<0:
			b=c
		else:
			a=c
	return True,c

number_of_terms = int(input("How many terms are there in the equation : "))
coeff_list = []
power_list = []
for index in range(number_of_terms):
	coeff = float(input(f"\n\tEnter coefficient for term {index+1} : "))
	power = float(input(f"\tEnter power for term {index+1} : "))
	coeff_list.append(coeff)
	power_list.append(power)
print("\nEntered formula : ",end="")
for index in range(number_of_terms-1):
	print(f"{coeff_list[index]}x^({power_list[index]})",end=" + ")
print(f"{coeff_list[number_of_terms-1]}x^({power_list[number_of_terms-1]})")

while True:
	a = float(input("Enter a : "))
	b = float(input("Enter b : "))
	
	choice,answer = bisection(a, b)
	if choice:
		print("Solution is :",round(answer,5))
		break
	else:
		print("You have not assumed right a and b")
		a = float(input("Enter a : "))
		b = float(input("Enter b : "))
	
	
	
	

#def calculate_value(x,coeff_list,power_list):		
#	counter = 0
#	for i in range(len(coeff_list)):
#		counter += coeff_list[index] * pow(float(x),float(power_list[index]))
#	return counter