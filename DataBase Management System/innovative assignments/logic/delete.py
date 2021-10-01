#!/usr/bin/env python3

DELETE

	def select_modify(self):
		if(tv.focus() != ""):
			BranchModify(Toplevel(self.master))
		else:
			messagebox.showerror("Please select a row to be modified")  
			
	def select_delete(self):
		try:
#            row_id = int(tv.focus().replace("I", ""))
			item = tv.item(tv.focus())
			tv.delete(tv.focus())
			sql_query = "DELETE FROM branch WHERE branch_id=" + str(item['values'][0]) + ";"
			try:
				mycursor.execute(sql_query)                                     #executing query
			except (mysql.connector.Error, mysql.connector.Warning) as e:       #fetching error
				messagebox.showerror(str(e))                                    #displaying error
			
		except:
			messagebox.showerror("showerror", "Please select a row to be deleted")
		mydb.commit()
		
		
	def select_add(self):
		BranchAdd(Toplevel(self.master))