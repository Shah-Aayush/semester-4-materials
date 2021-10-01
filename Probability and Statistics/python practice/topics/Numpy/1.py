#!/usr/bin/env python3

#run this in python 2

import numpy as np

if __name__ == "__main__":
	
	#creating arrays : 
	arr = np.array([1,2,3])
	print ("Array with Rank 1 : ",arr )
	arr = np.array([[1,2,3],[4,5,6]])
	print ("Array with Rank 2 : ",arr )
	arr = np.array((1,2,3))
	print ("Array with passed tuples : " , arr)
	
	#Accessing the array index : 
	arr = np.array([[-1, 2, 0, 4],
			[4, -0.5, 6, 0],
			[2.6, 0, 7, 8],
			[3, -7, 4, 2.0]])
	print ("Initial Array: \n" , arr)
	
	sliced_arr = arr[:2,:3]
	print ("Applying slicing method on arrays : \n" , sliced_arr)
	sliced_arr = arr[:2,::2]
	print ("Applying slicing method on arrays : \n" , arr[:2,::2])
	
	index_arr = arr[[1, 1, 0, 3], 
		[3, 2, 1, 0]]
	print ("Accessing arr via indices : \n" , index_arr)
	print ("Accessing Specific index : " , arr[[2],[3]])
	
	#Array operations : 
	a = np.array([[1,2],[3,4]])
	b = np.array([[5,6],[7,8]])
	print ("Adding 1 to every element of a : \n" , a+1)
	print ("Subtracting 1 from every element of b : \n" , b-1)
	print ("Sum of all array element of a : " , a.sum())
	print ("Sum of all array element of b : " , b.sum())
	print ("Array sum a + b : \n" , a+b)

	#sorting array
	a = np.array([[1,4,2],[3,4,6],[0,-1,5]])
	print("Row-wise sorted array : " , np.sort(a))
	
	#shaping
	arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
	print(arr.shape)
	
	#concate
	arr1 = np.array([1, 2, 3])
	arr2 = np.array([4, 5, 6])
	arr = np.concatenate((arr1, arr2))
	print(arr)