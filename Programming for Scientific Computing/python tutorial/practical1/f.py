#!/usr/bin/env python3

#Write a function that takes a string as a parameter and returns a string with every successive repetitive character replaced with a star(*). For Example, ‘balloon’ is returned as ‘bal*o*n’. [+ add this code : any letter is covered before it should also be changed to '*'.]


def modifyStringType1(original_string):
	'''
	If any repeated character is found in the string then it will be replaced by '*'
	'''
	alphabets = dict()
	new_string = original_string[0]
	for index in range(0,26):
		alphabets[chr(index+97)] = False
	alphabets[original_string[0]] = True
	for index in range(1,len(original_string)):
		if(alphabets[original_string[index]]==False):
			new_string += original_string[index]
			alphabets[original_string[index]] = True
		else:
			new_string += '*'
	return new_string

def modifyStringType2(original_string):
	'''
	If any repeated consecutive character is found in the string then it will be replaced by '*'
	'''
	new_string = original_string[0];
	for index in range(1,len(original_string)):
		if(original_string[index]==original_string[index-1]):
			new_string += '*'
		else:
			new_string += original_string[index]
	return new_string
		
#Driver code
if __name__ == "__main__":
	original_string = str(input("Enter string : "))
	print("String modification after type 1 : ",modifyStringType1(original_string.lower()))
	print("String modification after type 2 : ",modifyStringType2(original_string.lower()))