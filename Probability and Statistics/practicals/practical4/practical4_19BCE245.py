#!/usr/bin/env python3

# Write a program which reads 500 real values and computes and displays their (i) mean (ii) variance (iii) standard deviation. The program should also output z-score for each value. The program should furthermore display (i) scatter plot (ii) histograms for these numbers for n bins where n is read from the user and (iii) density plot assuming Gaussian as the probability density function.


import numpy as np;
import pandas as pd;
import matplotlib.pyplot as plt;

arr1 = []		#for storing 1st list
arr2 = []		#for storing 2nd list

total_size = int(input("Enter the size of the array : "))
size = int(total_size/2)

temp_number = float()

print("Enter first",size,"elements for array 1 : ")
for i in range(size):
	temp_number = float(input("\tEnter element no.{} : ".format(i+1)))
	arr1.append(temp_number)

sum_of_arr1 = sum(arr1)
mean_of_arr1 = float(sum_of_arr1/size)
print("For arr1, Sum is",sum_of_arr1,"and Mean is",mean_of_arr1)

print("Enter last",size,"elements for array 2 : ")
for i in range(size):
	temp_number = float(input("\tEnter element no.{} : ".format(size + i + 1)))
	arr2.append(temp_number)
	
sum_of_arr2 = sum(arr2)
mean_of_arr2 = float(sum_of_arr2/size)
print("For arr2, Sum is",sum_of_arr2,"and Mean is",mean_of_arr2)

#calculating variance
arr1_diff = []
arr2_diff = []
sq_sum_of_arr1 = 0
sq_sum_of_arr2 = 0

for i in range(size):
	arr1_diff.append(float(arr1[i]-mean_of_arr1))
	sq_sum_of_arr1 += float(arr1_diff[i]**2)

variance1 = float(sq_sum_of_arr1/size)

print("For arr1, Variance is",variance1)

for i in range(size):
	arr2_diff.append(float(arr2[i]-mean_of_arr2))
	sq_sum_of_arr2 += float(arr2_diff[i]**2)
	
variance2 = float(sq_sum_of_arr2/size)

print("For arr2, Variance is",variance2)

#displaying scatterplot.
plt.subplot(211)
plt.scatter(arr1_diff, arr2_diff)
plt.xlabel('arr1')
plt.ylabel('arr2')
plt.title('Scatter plot')

#displaying histograms 
plt.subplot(212)
plt.hist(arr1_diff,arr2_diff,histtype="bar",rwidth=0.8)
plt.xlabel('X axis')
plt.ylabel("Y axis")
plt.title("Histogram")

plt.tight_layout()		#improves subplot spacings 
plt.show()

