#!/usr/bin/env python3

#total,highest,avg =>Histogram

import random
from random import randrange
import array as arr

#a = arr.array('i', [])
matrix = []

#Generating unique ids through set
set_of_ids = set()
while len(set_of_ids)<11:
	set_of_ids.add(random.randint(1, 999999))

# Here -1 is for NA.
	
#avg_and_max_of_all = []

#ID i1 i2 i3 i4 i5 i6 i7 i8 i9 i10 Total avg Max <50 (50,100) (100,150) (150,200)
	
#generating 10 innings data
for i in range(11):          # A for loop for row entries 
	a = ['P' + str(set_of_ids.pop()).zfill(6)]
	count = 0;
	count_less_than_50 = 0
	count_less_than_100 = 0
	count_less_than_150 = 0
	count_less_than_200 = 0
	total_score = 0;
	max_score = 0;
	matches_played = 0;
	for j in range(1,11):      # A for loop for column entries 
		number = random.randint(-1, 200)
		while (count>=2 and number==-1):
			number = random.randint(-1, 200)
			
		if(number != -1):
			if(number<50):
				count_less_than_50 += 1
			elif(number<100):
				count_less_than_100 += 1
			elif(number<150):
				count_less_than_150 += 1
			else:
				count_less_than_200 += 1
				
			total_score += number
			matches_played += 1
			if(max_score<number):
				max_score = number
		else:
			count+=1
		a.append(number) 
	
	a.append(total_score)	#appending total
	a.append(round(total_score/matches_played,1))	#appending avg
	a.append(max_score)	#appending max
	a.append(count_less_than_50)
	a.append(count_less_than_100)
	a.append(count_less_than_150)
	a.append(count_less_than_200)
	
#	avg_and_max = []
#	avg_and_max.append(total_score/matches_played)
#	avg_and_max.append(max_score)
#	avg_and_max_of_all.append(avg_and_max)
	matrix.append(a) 



#Printing data
print("ID      I1  I2  I3  I4  I5  I6  I7  I8  I9  I10  | Total  Avg    Max <50 <100 <150 <200")
for i in range(11): 
	for j in range(18): 
		if (matrix[i][j]==-1):
			print("NA", end = "  ") 
		else:
			if(j==12):
				print(str(matrix[i][j]).zfill(5), end = "  ") 
			elif(j==11):
				print(" | ",str(matrix[i][j]).zfill(4), end = "  ") 
			else:
				print(str(matrix[i][j]).zfill(3), end = " ") 
	print()
	
#Printing avg and max data
#print("\n\nAVERAGE  |  MAX")
#for i in range(11):
#	print(str(round(avg_and_max_of_all[i][0],1)).zfill(5),end = "       ")
#	print(str(round(avg_and_max_of_all[i][1],2)).zfill(3),end = "")
#	print()

#Top 6 players : 
print("\n\nPlayers in their avg. score's increasing order : \n")
matrix = sorted(matrix, key = lambda a_entry:a_entry[11])
print("ID      I1  I2  I3  I4  I5  I6  I7  I8  I9  I10  | Total  Avg    Max <50 <100 <150 <200")
for i in range(11): 
	for j in range(18): 
		if (matrix[i][j]==-1):
			print("NA", end = "  ") 
		else:
			if(j==12):
				print(str(matrix[i][j]).zfill(5), end = "  ") 
			elif(j==11):
				print(" | ",str(matrix[i][j]).zfill(4), end = "  ") 
			else:
				print(str(matrix[i][j]).zfill(3), end = " ") 
	print()
	
#Top 6 players :
print("\nTop players : \nID        Avg.")
for i in range(5,11):
	print(matrix[i][0] , " " , str(matrix[i][12]).zfill(4))