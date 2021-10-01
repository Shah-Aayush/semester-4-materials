#!/usr/bin/env python3

#Write a program which scans marks of n (scan n from the user) students in P & S. Assuming that the students are to be graded on 5 grade-scale (A, B, C, D, and F), display marks and grade of each student. Fit Gaussian distribution to the data. Repeat the exercise if students are to be graded on 7 grade-scale (A, B, C+, C, C-, D, F). Also display bar chart for both the cases.

"""
used this for practical 5
For more than 30 students in a course, the statistical method shall be used, with marginal adjustment for natural cut-off. The mean(X) and the standard deviation(SD) of marks obtained of all the students in a course shall be calculated and grades shall be awarded to a student depending upon the marks and the standard deviation as per table given below:
A+ > X+1.5SD
X+1.0SD < A <= X +1.5 SD
X+0.5SD < B+ <= X+1.0SD
X < B <= X+0.5SD
X-0.5SD < C <= X
X-1.0SD < D <= X-0.5SD
X-1.5SD < F <=X -1.5SD
"""


"""
(a) Write a program which scans marks of n (scan n from the user)
	students in P & S. Assuming that the students are to be graded on
	5 grade-scale (A, B, C, D, and F), display marks and grade of each
	student. Fit Gaussian distribution to the data. Repeat the exercise
	if students are to be graded on 7 grade-scale (A, B, C+, C, C-, D,
	F). Also display bar chart for both the cases.
(b) Change the above program further in 2 different ways: (1) Scan
	number of grades and z-score range for each of the grades to be
	used to grade students (2) Scan number of grades and number of
	students instructor wants to put in each grade.
	In (b), apart from the modifications suggested, other requirements and
	instructions are same as in (a).
"""
	
import math
import random
import numpy as np
import matplotlib.pyplot as plt
	
def gaussFunction(s, x, m):
	return (1 / (s * math.sqrt(2 * math.pi))) * math.exp((-1 / 2) * math.pow((x - m) / s, 2))

def cal_grade_5scale(marks,mean,standard_deviation):
	if (marks > (mean + 1.5 * standard_deviation)):
		return 'A'
	elif (mean + standard_deviation < marks <= mean + 1.5 * standard_deviation):
		return 'B'
	elif (mean + 0.5 * standard_deviation < marks <= mean + standard_deviation):
		return 'C'
	elif (mean < marks <= mean + 0.5 * standard_deviation):
		return 'D'
	else:
		return 'F'
	
def cal_grade_7scale(marks,mean,standard_deviation):
	if (marks > (mean + 1.5 * standard_deviation)):
		return 'A+'
	elif (mean + standard_deviation < marks <= mean + 1.5 * standard_deviation):
		return 'A'
	elif (mean + 0.5 * standard_deviation < marks <= mean + standard_deviation):
		return 'B+'
	elif (mean < marks <= mean + 0.5 * standard_deviation):
		return 'B'
	elif (mean - 0.5 * standard_deviation < marks <= mean + standard_deviation):
		return 'C'
	elif (mean - standard_deviation < marks <= mean - 0.5 * standard_deviation):
		return 'D'
	else:
		return 'F'
	
def cal_grade_custom(marks,z_score_ranges):
	grade = 'A'
	for grade_index in range(np.shape(z_score_ranges)[0]):
		if (z_score_ranges[grade_index][0] < marks <= z_score_ranges[grade_index][1]):
			return grade
		else:
			grade = chr(ord(grade) + 1)
			continue
	return 'F'		#by deafaul grade

if __name__ == "__main__":
	n = int(input("Enter number of students : "))
	marks = [random.randint(0, 100) for i in range(n)]		#generating random marks
	
	mean = np.mean(marks)
	standard_deviation = np.std(marks)
	
	grades5 = [cal_grade_5scale(mark, mean, standard_deviation) for mark in marks]
	
	print("\n\nGRADES by 5-scale\nMARKS\tGRADES")
	for index in range(n):
		print(str(marks[index]).ljust(5),"  ",grades5[index].ljust(5))
	
	grades7 = [cal_grade_7scale(mark, mean, standard_deviation) for mark in marks]

	print("\n\nGRADES by 7-scale\nMARKS\tGRADES")
	for index in range(n):
		print(str(marks[index]).ljust(5),"  ",grades7[index].ljust(5))
		
	total_grades = int(input("\nEnter total number of grades : "))
	print("Enter z-score range for each grade one by one : ")
	z_score_ranges = np.zeros(shape=(total_grades,2))
	
	for index in range(total_grades):
		z_score_ranges[index][0] = float(input("\tEnter LOWER limit of z-score for GRADE {} : ".format(chr(index+65))))
		z_score_ranges[index][1] = float(input("\tEnter UPPER limit of z-score for GRADE {} : ".format(chr(index+65))))
		print()
		
	z_score = [((mark - np.mean(marks)) / np.std(marks)) for mark in marks]
	
	grades_custom = [cal_grade_custom(z_score_ind, z_score_ranges) for z_score_ind in z_score]
	print(grades_custom)
	
	print("\n\nGRADES by CUSTOM\nMARKS\tGRADES")
	for index in range(n):
		print(str(marks[index]).ljust(5),"  ",grades_custom[index].ljust(5))
	
	count5 = []
	count7 = []
	counter = 0
	
	scale_5_grades = ['A','B','C','D','F']
	scale_7_grades = ['A','A+','B+','B','C','D','F']
	
	for grade_main in scale_5_grades:
		counter = 0
		for grade_cal in grades5:
			if(grade_cal == grade_main):
				counter+=1
		count5.append(counter)	
		
	for grade_main in scale_7_grades:
		counter = 0
		for grade_cal in grades7:
			if(grade_cal == grade_main):
				counter+=1
		count7.append(counter)
		
	
	
	plt.subplot(1,3,1)
	plt.plot(sorted(marks) , [gaussFunction(standard_deviation, mark, mean) for mark in sorted(marks)])
	plt.title("Gaussian Distribution")
	plt.xlabel("Marks")
	plt.ylabel("Probability Density Function")
	
	plt.subplot(1,3,2)
	plt.bar(['A','B','C','D','F'],count5)
	plt.title("GRADE by scale-5")
	plt.xlabel("Grades")
	plt.ylabel("Number of Students")
	
	plt.subplot(1,3,3)
	plt.bar(['A+','A','B+','B','C','D','F'],count7)
	plt.title("GRADE by scale-7")
	plt.xlabel("Grades")
	plt.ylabel("Number of Students")
	
	plt.show()