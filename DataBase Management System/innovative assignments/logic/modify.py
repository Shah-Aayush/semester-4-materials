#!/usr/bin/env python3

MODIFY

def select_back(self):
	self.master.withdraw()
	
def select_modify(self,branch_id,branch_name):
	try:
		sql_query = "UPDATE branch SET branch_id=" + str(self.Entry1_1.get()) + ", branch_name='" + str(self.Entry1_2.get()) + "' WHERE branch_id=" + str(item_modifyBranch[0]) + ";"
		try:
			mycursor.execute(sql_query)                                     #executing query
			tv.item(tv.focus(), text="", values=(str(self.Entry1_1.get()),self.Entry1_2.get()))
		except (mysql.connector.Error, mysql.connector.Warning) as e:       #fetching error
			messagebox.showerror(str(e))                                    #displaying error
		
	except:
		messagebox.showerror("showerror", "Modification failed")
	mydb.commit()
	self.master.withdraw()