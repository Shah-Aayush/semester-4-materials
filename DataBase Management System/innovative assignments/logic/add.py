#!/usr/bin/env python3

ADD

def select_back(self):
	self.master.withdraw()
	
def select_add(self, branch_id, branch_name):
	if branch_id.isnumeric() and len(branch_id)!=0:
		if len(branch_name)!=0:
			
			sql_query = "INSERT INTO branch VALUES(" + branch_id + ", '" + branch_name + "');"
			try:
				mycursor.execute(sql_query)                                     #executing query
				tv.insert(parent='', index='end', text="Parent", values=(str(branch_id), branch_name))
				print("inside try : ",mycursor.fetchall())
			except (mysql.connector.Error, mysql.connector.Warning) as e:       #fetching error
				messagebox.showerror("ERROR MESSAGE :\n" + str(e)) 
				print("inside except : ",mycursor.fetchall())                             #displaying error
			
		else:
			messagebox.showerror("Enter branch name")
	else:
		messagebox.showerror("Enter proper branch id")
	print(branch_id,branch_name)
	self.master.withdraw()
	mydb.commit()