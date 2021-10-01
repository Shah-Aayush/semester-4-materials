import math
# these are comments

#String
string = "Aayush"
print(string)
print(string[0])
print(string[2:])
print(string[:3])
print(string*2)
print(string + " Shah")

#List
List = [1,2,3,4,5,6,7,8,9,10]
months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
for index in months: 
	print(index, end=" ")
print()
for index in List: 
	print(index, end="  ")
	#List operations
del List[3]
print(List)
print(len([1,2,3]))
print([1,2,3] + [4,5,6])
print(['Hi!']*4)
print(2 in [1,2,3])
for x in [1,2,3]:
	print(x)
List2 = [1,2,3,4,5,6,7,8,9,10]
print(len(List2))
print(max(List2))
print(min(List2))
tuple_into_list = (22,33,44)
List3 = list(tuple_into_list)	#converts tuple into list
print(tuple_into_list)
print(List3)
List4 = List3.copy()
print(List4)
List4.append("Aayush")
List4.append("Aayush")
print(List4)
print(List4.count("Aayush"))
print(List4)
List4.extend(tuple_into_list)		#can append list and tuples as well.
List4.extend(List2)
print(List4)
print(List4.index("Aayush"))		#returns the lowest index of the specific obj in the list
List4.insert(0, "shah")
print(List4)
List4.pop()		#pops the last value in the list.
print(List4)
List4.remove("Aayush")		#removes the largest index obj. AND gives error when obj is not present in the list.
print(List4)
List4.reverse()
print(List4)
List2.sort()
print(List2)

#Tuple
making_tuple = ('aayush',1234, 23.45,'shah')
print(making_tuple)
print(making_tuple[0])
print(making_tuple[0:3])
print(making_tuple[:2])
print(making_tuple[2:])

#Dictionary
making_dictionary = {'name':"Aayush", 'year':2, 1423:23.34}
print(making_dictionary)
print(making_dictionary["name"])
print(making_dictionary[1423])
print(making_dictionary.keys())
print(making_dictionary.values())

#Matrices
matrix = [[1,2,3],[4,5,6]]
print(matrix)
print(matrix[0])
print(matrix[1])
print(matrix[1][0])
matrix[0] = [11,22,33]
matrix[0] = [21,32,43]
print(matrix)
print(matrix[0])
print(matrix[1])

#OPERATORS 
	
	#Arithmatic Operators
a = 10
b = 2
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a**b)
print(a//b)
print(a%b)
	#Comaparison Operators
a = 10
b = 10
print(a==b)
print(a!=b)
print(a>b)
print(a<b)
print(a<=b)
print(a>=b)
	#Assignment Operators
a = 10 
b = 2 
c = a + b
c = a - b
c += a		#is equal to c=c+a
c -= a		#is equal to c=c-a
c *= a
c /= a
c %= a
c **= a
c //= a
	#Bitwise Operators
c = a & b	#and
c = a | b	#or
c = a ^ b	#xor
c = ~a		#not
c = a<<2	#leftShift
c = a>>2	#rightShift
	#Logical Operators
c = a and b		#answers in boolean
c = a or b		
c =	not a 		
	#Membership Operators
c = 'Jan' in  months
c = 'Sun' not in  months
	#Identity Operators
c = a is b		#compares memory locations of two objects
c = a is not b		
	#Precedence of Python Operators : 
"""
**							Exponentiation
~ + -						Complement, unary plus and minus
* / % //					Multiply, divide, modulo and floor division
+ - 						Addition and subtraction
>> <<						Right and left bitwise shift
& 							Bitwise 'AND'
^ | 						Bitwise exculsive 'OR' and regular 'OR'
<= < > >=					Comparison operators
< > == !=					Equality operators
= %= /= //= -= += *= **=	Assignment operators
is is not					Identity operators
in not in 					Membership operators
not or and 					Logical operators 
"""

#Decision making
var1 = 10
var2 = True
if var1>100:
	c = a+b
	print("greater",c)
elif var1<100:
	c = a-b
	print("lesser",c)
else :
	c = a*b
	print("equal",c)
	if var1:
		print("yes")
	else:
		print("no")

#Loops
count = 1
while(count<10):
	print("The count is : ",count)
	count+=1
for month in months:
	print(month)
for i in range(10):
	print(i , end = ", ")
print()

#Numbers
	#Number type conversion
x = int(23.34)
print(x)
y = float(123)
print(y)
z = complex(12)
print(z)
z = complex(12,34)
print(z)
	#Mathematical functions
print(abs(10-20))
print(math.ceil(1.10))
print(math.floor(1.10))
print(math.exp(3))
print(math.log(3))		#value, base=e
print(math.log(9,3))	#value, base
print(math.log10(10))	#value, base=10
print(max(1,2,3))
print(min(1,2,3))
print(pow(5,2))
print(round(12.123456789,4))
print(math.sqrt(9))

#String
str = "aayush umeshbhai shah"
print(str.capitalize())
print(str.isalnum())		#returns true if string has at least 1 character and all characters are alphanumeric AND False otherwise.
print("1234asdf".isalnum())
print(str.isalpha())		#returns true if string has atleast 1 character and all characters are alphabetic AND false otherwise.
print(str.isdigit())		##returns true if string has atleast 1 character and all characters are numeric AND false otherwise.
print(str.islower())
print(str.isupper())
print(str.isspace())
print(str.lower())
print(str.upper())
print(len(str))
print(max(str))		#returns the max alphabetical character from the string
print(min(str))		#returns the min alphabetical character from the string

#Variables and Input statements
x,y,z = input("Enter values of x, y, z :").split();
print("values are : x={}, y={}, z={}".format(x,y,z))
a = int(input("Enter value of a : "))
b = int(input("Enter value of b : "))
print("{} + {} = {}".format(a,b,a+b))
print(a,b)
print("a = {} , b = {}".format(a,b))
