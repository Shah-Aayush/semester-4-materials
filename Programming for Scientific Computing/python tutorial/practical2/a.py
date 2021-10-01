#!/usr/bin/env python3

import math

def cal_gaussian(s,x,m):
	answer = float(1)
	answer /= (s*math.sqrt(2*math.pi))
	answer *= math.exp((-1/2)*(((x-m)/s)**2))
	return answer

s = float(0)
while(s<1):
	s = float(input("Enter s : "))
	if(s<1):
		print("Value of s must be greater than zero.")
x = float(input("Enter x : "))
m = float(input("Enter m : "))
print("The answer is : " , cal_gaussian(s, x, m))
