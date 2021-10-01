#!/usr/bin/env python3

#Write a function areaTriangle that takes the lengths of three sides of the triangle as input parameters and returns the area of the triangle as an output. Also, assert that the sum of the length of any two sides is higher than the third side. Write a main function that accepts as command-line arguments and computes the area of a triangle using the function areaTriangle.
import sys 

def assertion(s1,s2,s3):
	return s1+s2>s3 or s1+s3>s2 or s2+s3>s1
	
def areaTriangle(s1,s2,s3):
	s = (s2 + s2 + s3) / 2  
	area = (s*(s-s1)*(s-s2)*(s-s3)) ** 0.5  
	return s
	
if __name__ == "__main__":
	s1 = int(sys.argv[1])
	s2 = int(sys.argv[2])
	s3 = int(sys.argv[3]) 
	area = areaTriangle(s1, s2, s3)
	print('Assertion : ' , assertion(s1, s2, s3))   
	print('Area of triangle : %0.2f' %area)
