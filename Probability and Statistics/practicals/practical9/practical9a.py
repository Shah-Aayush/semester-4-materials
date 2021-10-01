#!/usr/bin/env python3

import random
import matplotlib.pyplot as plt

#user input
size_of_data = int(input("Enter size of data you wanted : "))
starting_range = int(input("Enter starting limit of data : "))
ending_range = int(input("Enter ending limit of data : "))

#random data generating
independent_data = random.sample(range(starting_range,ending_range),size_of_data)
dependent_data = random.sample(range(starting_range,ending_range),size_of_data)

#sorting data
independent_data.sort()
dependent_data.sort()

x = independent_data
y = dependent_data

#calculating intercept and slope
n=len(x)
E_y=sum(y)
E_x=sum(x)
E_xy=sum([i*j for i,j in zip(x,y)]) 
E_x2=sum([i*i for i in x])
E_y2=sum([i*i for i in y]) 
intercept=(E_y*E_x2-E_x*E_xy)/(E_x2-E_x**2)
slope=(n*E_xy-E_x*E_y)/(n*E_x2-E_x**2)

#generating graph
x_val=list(range(80));
y_val=[intercept+slope*i for i in x_val]; 
print(f"\nIntercept = {round(intercept,2)}\nSlope = {round(slope,2)}")
plt.plot(x,y)
plt.plot(x_val,y_val)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Linear Regression")
plt.show()