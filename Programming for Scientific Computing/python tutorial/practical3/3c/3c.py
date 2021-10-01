#!/usr/bin/env python3

"""
testcases -> file which contains test cases		[format : id,velocity]
answers -> storing output		[format : id,velocity,breaking distance]
summary -> storing AVERAGE VELOCIY and TOTAL DISTANCE.
"""

from scipy.constants import g

def compute_d(initial_velocity,friction_coeff):
	return ((1/2)*(initial_velocity**2)/(friction_coeff*g))


testcases = open("Testcases.txt") 	#opening testcases.txt in read mode
tests = [] 		#list for storing testcases.txt's data
test = []		#list for storing individual test
row = 0		#counter for rows in testcases
col = 0		#counter for columns in testcases [fixed to 2]
data = ""	#for storing each value in testcases

#reading data from testcases.txt.
while(1):
	char  = testcases.read(1)
#	print(char,col,row,data,test,tests)
	if(char == ',' or char == '\n'):
		test.append(data)
		data = ""
		col += 1
		if(col == 2):
			col = 0
			row += 1
			tests.append(test)
			test = []
	elif(char != ' '):
		data += char
	if not char:
		test.append(data)
		tests.append(test)
		break

testcases.close()
#printing extracted data from testcases.txt
#print(tests)

answers = open("Answers.txt",'w') 		#opening answers file for writing answers
friction_coeff = 0.3 		#setting friction coefficient

final_tests = []		#storing data format : id,velocity,distance
final_test = []

#calculating answers.
print("Calculated breaking distances : ")
for i in range(len(tests)):
	final_test = []
	final_test.append(tests[i][0])
	final_test.append(tests[i][1])
	final_test.append(str(round(compute_d(int(tests[i][1]), friction_coeff),2)))
	final_tests.append(final_test)
	write_str = "ID :" + " " + tests[i][0].ljust(10) + " " +  "VELOCITY : " + " " + tests[i][1].ljust(10) + " " + "DISTANCE : " + " " + final_test[2] + "\n"
	print(write_str)
	answers.write(write_str)
	
#print(final_tests)


set_of_tests = {}		#stores in format => id : [total_vel,total_dis,count]
total_dis = 0
avg_vel = 0
count_vel = 0
for i in range(len(final_tests)):
#	if set_of_tests.has_key(final_tests[i][0]) :
	if final_tests[i][0] in set_of_tests :
		set_of_tests[final_tests[i][0]][0] += int(final_tests[i][1]) #adding velocity
		set_of_tests[final_tests[i][0]][1] += float(final_tests[i][2]) #adding distance
		set_of_tests[final_tests[i][0]][2] += 1 #increasing counter
	else:
#		set_of_tests[final_tests[i][0]] = 0,0,1
		set_of_tests[final_tests[i][0]] = {0:int(final_tests[i][1]),1:float(final_tests[i][2]),2:1}

#print(set_of_tests)


summary = open("Summary.txt",'w')		#opening summary.txt in writing mode.
write_str = "ID".ljust(10) + "AVG-VELOCITY".ljust(15) + "TOTAL-DISTANCE\n" + "".ljust(40,"-") + "\n"
summary.write(write_str) 		#defining heading.

#writing data
for test in set_of_tests:
	write_str = str(test).ljust(10) + str(round(set_of_tests[test][0]/set_of_tests[test][2],2)).ljust(15) + str(round(set_of_tests[test][1],2)) + "\n"
	summary.write(write_str)
	
	"""
	DO NOT ADD EXTRA '\n' at the end of the Testcases.txt file.
	"""