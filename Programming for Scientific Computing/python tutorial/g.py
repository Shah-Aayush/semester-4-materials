#!/usr/bin/env python3

#Write a function that takes a number as n input parameter and returns the corresponding text in words; for example, on input 452, the function should return ‘Four Five Two’. Use a dictionary for mapping to digits to their string representation. [+ number to words]

from num2words import num2words

"""
the below function will only work after installing num2words.
We can easily install num2words using pip.  
pip install num2words
"""

def numberToWords(number):
	words_of_number = num2words(number)
	words_of_number = words_of_number.replace('-', ' ')
	return words_of_number

def numberToWords2(number):
	lengthOfString = len(number)
	digit = {'0': 'zero', '1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five', '6': 'six', '7': 'seven',
			'8': 'eight', '9': 'nine'}
	place = {4: 'thousand', 3: 'hundred', 2: 'two', 1: ''}
	tens = {'0': '', '1': 'one', '2': 'twenty', '3': 'thirty', '4': 'forty', '5': 'fifty', '6': 'sixty', '7': 'seventy',
			'8': 'eighty', '9': 'ninety'}
	one = {'0': 'ten', '1': 'eleven', '2': 'twelve', '3': 'thirteen', '4': 'fourteen', '5': 'fifteen', '6': 'sixteen',
			'7': 'seventeen', '8': 'eighteen', '9': 'nineteen'}
	
			

def numberToString(number):
	string_of_number = str()
	temp_number = number
	while(temp_number!=0):
		temp_rem = temp_number%10
		string_of_number += ""
		switcher  =  {
			0 : "zero",
			1 : "one",
			2 : "two",
			3 : "three",
			4 : "four",
			5 : "five",
			6 : "six",
			7 : "seven",
			8 : "eight",
			9 : "nine",
		}
		string_of_number = switcher.get(temp_rem) + " " + string_of_number
		temp_number=temp_number // 10
	return string_of_number

if __name__ == "__main__":
	number = int(input("Enter the number : "))
	print("Number to string : ",numberToString(number))
	print("Number to words : ",numberToWords(number))
#	print("Number to words 2 : ")
#	numberToWords2(str(number))
	
	"""
	for i in lengthOfString:
		if(i==0):
			if(number[i]=='0' and lengthOfString==1):
				if(lengthOfString==1):
					print(digit[number[i]],end="")
					break
				else:
					print(tens[number[i+1]],end=" ")
					continue
			elif(number[i]=='1' and lengthOfString==2):
				if(lengthOfString==2):
					print(one[number[i]])
					break
				
			print(digit[number[i]],end="")
			
				
		elif(i==1):
		
		elif(i==2):
		
		elif(i==3):
			
		else:
			print("Not available :(")
			
			if(lengthOfString>1)
	"""