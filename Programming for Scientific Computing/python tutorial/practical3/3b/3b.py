#!/usr/bin/env python3
#giving input file name in command line arguments as File1.txt and File2.txt
import sys
try : #exception handling
	file1 = open(sys.argv[1])		#By default in read mode.
except IOError:
	print("Cannot find file.\nReading data from default file...")
	file1 = open("File1.txt")
flag = 1 
matrix1 = []		#2D array for storing file1's data.
matrix2 = []		#2D array for storing file1's data.
data = ""	#var for storing each word
row1 = 0	#counter for rows of file1
row2 = 0	#counter for rows of file2
col = 0
mat_list = []		#1D array for storing each line's data.

while 1:
	#reading file character by character.
	char = file1.read(1)	#reading one char at a time
	if(char == ',' or char == '\n'):	#current data ended indicator
		mat_list.append(data)		#appending data to line's data
		data = ""		#erasing current word
		col += 1		#going to new data
		if(col==3):		#current line ended indicator [for increasing row value].
			col = 0		#going to new data in new line
			row1 += 1	#going to new row
			matrix1.append(mat_list)		#appending  line's data in the matrix
			mat_list = []		#erasing line's data as it is  stored in matrix now.
	elif(char != ' '):		#current data is still being read
		data += char		#collecting chars for current data
	if not char:		#if  end  of line reached then exit the while loop
		break

#printing data
print("Data extracted from file 1 : ")
for i in range(row1):
	print("\t",end="")
	for j in range(3):
		print(matrix1[i][j],end=" ")
	print()
	
file1.close()		#closing file1


try : #exception handling
	file2 = open(sys.argv[2])		#By default in read mode.
except IOError:
	print("Cannot find file.\nReading data from default file...")
	file2 = open("File2.txt")
	
#reading file2
while 1:
	#reading file character by character.
	char = file2.read(1)	#reading one char at a time
	if(char == ',' or char == '\n'):	#current data ended indicator
		if(char=='\n' and data == ""):
			mat_list.append("NA")		#if data is not available then simply writing NA in that field
		else:
			mat_list.append(data)		#appending data to line's data
		data = ""		#erasing current word
		col += 1		#going to new data
		if(col==2):		#current line ended indicator [for increasing row value].
			col = 0		#going to new data in new line
			row2 += 1	#going to new row
			matrix2.append(mat_list)		#appending  line's data in the matrix
			mat_list = []		#erasing line's data as it is  stored in matrix now.
	elif(char != ' '):		#current data is still being read
		data += char		#collecting chars for current data
	if not char:		#if  end  of line reached then exit the while loop
		if(col==1 and data == ""):
			mat_list.append("NA")
		else:
			mat_list.append(data)
		matrix2.append(mat_list)
		row2 += 1
		break

#printing data
print("\nData extracted from file 2 : ")
for i in range(row2):
	print("\t",end="")
	for j in range(2):
		print(matrix2[i][j],end=" ")
	print()

file2.close()		#closing file2


file3 = open("File3.txt",'w') #File for storing calculated wages
write_str = "ID".ljust(5) + "NAME".ljust(16) + "WAGES" + "\n" + "".ljust(30,"-") + "\n"  #writing heading in the file3

#printing salary along with writing it in File3.txt
print("\nCalculated monthly wages : ")
file3.write(write_str)
for i in range(row1):
	if(matrix2[i][1] == "NA"):
		print("\t",matrix1[i][0],matrix1[i][1].ljust(15),"NA")
		write_str = matrix1[i][0] + " " + matrix1[i][1].ljust(15) + " " + "NA" + "\n"
		file3.write(write_str)
	else:
		print("\t",matrix1[i][0],matrix1[i][1].ljust(15),int(matrix1[i][2])*int(matrix2[i][1]))
		write_str = matrix1[i][0] + " " + matrix1[i][1].ljust(15) + " " + str(int(matrix1[i][2])*int(matrix2[i][1])) + "\n"
		file3.write(write_str)
	
file3.close()

"""
Insert extra '\n' at the end of the file1.txt and do not insert any extra '\n' at the end of the file2.txt

command line arguments : File1.txt File2.txt
"""