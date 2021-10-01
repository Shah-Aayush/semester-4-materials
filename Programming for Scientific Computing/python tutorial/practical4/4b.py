#!/usr/bin/env python3

#Define a base class Person, having attributes name, birthdate and city. Define the class Student that derives from Person class which is having attributes like rollno, branch, totalMarks and year as data member. The class should contain the instance method __init__ and the abstract method percentage. Define two classes Grad and PostGrad which inherit from the base class Student. Both the classes should define their __init__ method which asks user t enter totalMarks value and should override the abstract method percentage of the superclass. Note that totalMarks obtained are out of 600 and 400 for Grad and PostGrad classes respectively.

import abc

class Person():
	def __init__(self, name, birthdate, city):
		self.name = name
		self.birthdate = birthdate
		self.city = city
	def percentage(self):
		pass
		
class Student(Person,abc.ABC):
	def __init__(self,name,birthdate,city,rollno,branch,year,marks):
		self.rollno = rollno
		self.branch = branch
		self.year = year
		self.marks = marks
		super().__init__(name, birthdate, city)
		
	@abc.abstractmethod
	def percentage(self):
		pass

class Grad(Student):
	def __init__(self,name,birthdate,city,rollno,branch,year,marks):
		super().__init__(name,birthdate,city,rollno,branch,year,marks)
		self.total_marks = 600
	def percentage(self):
#		str_for_input = "Enter total marks out of " + str(self.total_marks) + " : "
#		marks = float(input(str_for_input))
		return ((self.marks/self.total_marks)*100)
		
class PostGrad(Student):
	def __init__(self,name,birthdate,city,rollno,branch,year,marks):
		super().__init__(name,birthdate,city,rollno,branch,year,marks)
		self.total_marks = 400
	def percentage(self):
#		str_for_input = "Enter total marks out of " + str(self.total_marks) + " : "
#		marks = float(input(str_for_input))
		return ((self.marks/self.total_marks)*100)
		
if __name__ == "__main__":
	list_of_student = []
	while True:
		print("\nMENU : ")
		print("[1.] Add Student of PostGrad")
		print("[2.] Add Student of Grad")
		print("[3.] Show data")
		print("[4.] Exit")
		choice = int(input("Enter choice : "))
		if (choice == 1):
			student = PostGrad(str(input("Enter name : ")), str(input("Enter birthdate : ")), str(input("Enter city : ")), str(input("Enter roll number : ")), str(input("Enter branch : ")), int(input("Enter year of study : ")), float(input("Enter total_marks obtained out of 400 : ")))
			list_of_student.append(student)
		elif (choice == 2):
			student = Grad(str(input("Enter name : ")), str(input("Enter birthdate : ")), str(input("Enter city : ")), str(input("Enter roll number : ")), str(input("Enter branch : ")), int(input("Enter year of study : ")), float(input("Enter total_marks obtained out of 600 : ")))
			list_of_student.append(student)
		elif(choice == 3):
			print("Stored data : ")
			for student in list_of_student:
				print("Name : ",student.name)
				print("BirthDate  : ",student.birthdate)
				print("City : ",student.city)
				print("Roll Number : ",student.rollno)
				print("Branch : ",student.branch)
				print("Year : ",student.year,)
				print("Percentage : ",round(student.percentage(),2),"\n")
		elif(choice == 4):
			print("Thank you !")
			break
		else:
			print("Invalid choice :(")
			