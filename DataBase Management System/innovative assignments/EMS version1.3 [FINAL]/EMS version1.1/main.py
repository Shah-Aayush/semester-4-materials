"""
This code is written by :

1. 19BCE237 - Sakshi Sanghavi
2. 19BCE238 - Harshil Sanghvi
3. 19BCE245 - Aayush Shah

"""

import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", passwd="123password", database="innovative_assignment")
mycursor = mydb.cursor()

def add_student():
    print()
def add_exam():
    print()
def add_subject():
    print()
def add_result():
    print()
def add_attendance():
    print()
def add_branch():
    print()
    
def modify_student():
    print()
def modify_exam():
    print()
def modify_subject():
    print()
def modify_result():
    print()
def modify_attendance():
    print()
def modify_branch():
    print()
    
def delete_student():
    print()
def delete_exam():
    print()
def delete_subject():
    print()
def delete_result():
    print()
def delete_attendance():
    print()
def delete_branch():
    print()
    
def display_table(choice):          #1=student; 2=exam; 3=subject; 4=result; 5=attendance; 6=branch
    if choice==1:
        mycursor.execute("select * from attendance")
        data = mycursor.fetchall()
        return data 
    elif choice==2:
        print()
    elif choice==3:
        print()
    elif choice==4:
        print()
    elif choice==5:
        print()
    elif choice==6:
        print()
    else:
        return False

def student_table():
    print()
    while True:
        print("[0.] Exit")
        print("[1.] Display")
        print("[2.] Add")
        print("[3.] Modify")
        print("[4.] Delete")
        choice = int(input("Enter choice : "))
        if choice==0:
            break
        elif choice==1:
            display_table(1)
        elif choice==2:
            addStudent()
        elif choice==3:
            modifyStudent()
        elif choice==4:
            deleteStudent()
    
def exam_table():
    print()

def subject_table():
    print()

def result_table():
    print()
    
def attendance_table():
    print()
    
def branch_table():
    print()

def custom_table():
    print()

if __name__ == "__main__":
    mycursor.execute("select * from attendance")
    data = mycursor.fetchall()
    print(data)
    #1=student; 2=exam; 3=subject; 4=result; 5=attendance; 6=branch
    while True:
        print("Select a table :")
        print("\t[0.] Exit")
        print("\t[1.] Student")
        print("\t[2.] Exam")
        print("\t[3.] Subject")
        print("\t[4.] Result")
        print("\t[5.] Attendance")
        print("\t[6.] Branch")
        choice = int(input("Enter choice : "))
        if choice==1:
            studentTable()
        elif choice==2:
            examTable()
        elif choice==3:
            subjectTable()
        elif choice==4:
            resultTable()
        elif choice==5:
            attendanceTable()
        elif choice==6:
            branchTable()
        elif choice==0:
            print("Thank you for using EXAM DATABASE SOFTWARE!")
            break
        else:
            print("Invalid choice")    