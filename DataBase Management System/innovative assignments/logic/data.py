#!/usr/bin/env python3

DATA 

#real data
mycursor.execute("SELECT * from branch;")
output = mycursor.fetchall()

for list_item in output:
	tv.insert(parent='', index="end", text="Parent", values=(str(list_item[0]), str(list_item[1])))