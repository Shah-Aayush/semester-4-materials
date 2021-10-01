#!/usr/bin/env python3

#As you know, a magic square is a matrix all of whose row sums, column sums and the sums of the two diagonals are the same. (One diagonal of a matrix goes from the top left to the bottom right, the other diagonal goes from top right to bottom left.) Show by direct computation that if the matrix A is given by
#A=np.array([[17, 24, 1, 8, 15], [23, 5, 7, 14, 16],
#	[ 4, 6, 13, 20, 22], [10, 12, 19, 21, 3], [11, 18, 25, 2, 9]])
#The matrix A has 5 row sums (one for each row), 5 column sums (one for each column) and two diagonal sums. These 12 sums should all be exactly the same, and you could verify that they are the same by printing them and “seeing” that they are the same. It is easy to miss small differences among so many numbers, though. Instead, verify that A is a magic square by constructing the 5 column sums and computing the maximum and minimum values of the column sums. Do the same for the 5 row sums, and compute the two diagonal sums. Check that these six values are the same. If the maximum and minimum values are the same, the flyswatter principle says that all values are the same.

import numpy

def is_magicSQ(sq_matrix,size):
	min_sum_of_rows,max_sum_of_rows = 1e9,0
	
	#min and max of sum_of_elements_in_rows
	for row in range(size):
		row_sum = 0
		for column in range(size):
			row_sum += sq_matrix[row][column]
		min_sum_of_rows = min(min_sum_of_rows,row_sum)
		max_sum_of_rows = max(max_sum_of_rows,row_sum)
		
	if(min_sum_of_rows != max_sum_of_rows):
		return False
	
	min_sum_of_cols,max_sum_of_cols = 1e9,0
	
	#min and max of sum_of_elements_in_cols
	for column in range(size):
		col_sum = 0
		for row in range(size):
			col_sum += sq_matrix[row][column]
		min_sum_of_cols = min(min_sum_of_cols,col_sum)
		max_sum_of_cols = max(max_sum_of_cols,col_sum)
	
	if(min_sum_of_cols != max_sum_of_cols):
		return False
	
	
	principal_diagonal_sum,secondary_diagonal_sum =  0,0
	
	#checking diagonal sums 
	for row_col in range(size):
		principal_diagonal_sum += sq_matrix[row_col][row_col]
		secondary_diagonal_sum += sq_matrix[size-row_col-1][size-row_col-1]
	
	if(principal_diagonal_sum != secondary_diagonal_sum):
		return False
	
	if(min_sum_of_rows == max_sum_of_rows ==  min_sum_of_cols == max_sum_of_cols == principal_diagonal_sum == secondary_diagonal_sum):
		return True
	return False

def is_magicSQ_short(sq_matrix,size):
	min_sum_of_rows = min(numpy.sum(sq_matrix, axis = 0))
	max_sum_of_rows = max(numpy.sum(sq_matrix, axis = 0))
	min_sum_of_cols = min(numpy.sum(sq_matrix, axis = 1))
	max_sum_of_cols = max(numpy.sum(sq_matrix, axis = 1))
	principal_diagonal_sum = sum(numpy.diagonal(sq_matrix))
	secondary_diagonal_sum = sum(numpy.fliplr(sq_matrix).diagonal())
	if(min_sum_of_rows == max_sum_of_rows ==  min_sum_of_cols == max_sum_of_cols == principal_diagonal_sum == secondary_diagonal_sum):
		return True
	else:
		return False

if __name__ == "__main__":
	
	#MANUAL PROCESS [takes input from user]
#	size = int(input("Enter size of the square matrix : "))
#	sq_matrix = numpy.zeros((size,size))
#	
#	for row in range(size):
#		for column in range(size):
#			str_for_input = "Enter value for matrix[" + str(row+1) + "][" + str(column+1) + "] : "
#			sq_matrix[row,column] = int(input(str_for_input))
	
	
	#Pre-defined [matrix as per question]
	sq_matrix = numpy.array([[17, 24, 1, 8, 15], [23, 5, 7, 14, 16],[ 4, 6, 13, 20, 22], [10, 12, 19, 21, 3], [11, 18, 25, 2, 9]])
	size = numpy.shape(0)
	
	if(is_magicSQ_short(sq_matrix, size)):
		print("\nGiven matrix is a magic square :)")
	else:
		print("\nGiven matrix is not a magic square :(")