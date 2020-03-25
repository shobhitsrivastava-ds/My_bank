import sqlite3
import random
class bank:
	def __init__(self):
		pass
		#self.li =[]
	def create_table(self,conn,c):
		#li.append(n)
		with conn:
			c.execute("CREATE TABLE Bank18 (Acc_no integer,Name text,Sex text, Age integer, Type text,Amount float)")
	def get_new_account(self,name,sex,age,type_a,balance,conn,c):
		n= random.randint(100000,999999)
		with conn:
			c.execute("INSERT INTO Bank18 VALUES(:acc_n,:name,:sex,:age,:type,:bal)",{"acc_n":n,"name":name,"sex":sex,"age":age,"type":type_a,"bal":balance}) 
		return(n)
	def get_emp_det(self, n):
		c.execute("SELECT * FROM Bank18 WHERE Acc_no =:name",{"name":n})
		det = c.fetchall()
		acc_n =det[0][0]
		name = det[0][1]
		sex =det[0][2]
		age = det[0][3]
		type_ac= det[0][4]
		bal = det[0][5]
		acc_det = {"acc_n":acc_n, "name":name, "sex":sex, "age":age, "type_ac":type_acc, "balance":bal}
		return(acc_det)
	def withdraw_amt(self, acc_n, amt):
			c.execute("SELECT Amount FROM Bank14 WHERE Acc_no=:no",{"no":acc_n})
			bal = c.fetchall()
			bal = float(bal[0][0])
			if(bal>amt):
				new_bal =bal-amt
				c.execute("UPDATE Bank14 SET Amount =:nam WHERE Acc_no=:an",{"nam":new_bal,"an":acc_n})
				return(new_bal)
			else:
				return("[INFO]!! Insufficient Amount")
	def deposite_amt(self, acc_n, amt):
		with conn:
			c.execute("SELECT Amount FROM Bank14 WHERE Acc_no=:no",{"no":acc_n})
			bal = c.fetchall()
			bal = float(bal[0][0])
			new_bal =bal+amt
			c.execute("UPDATE Bank14 SET Amount =:nb WHERE Acc_no=:an",{"nb":new_bal,"an":acc_n})
			return(new_bal)
	def delete_account(self, acc_n):
		with conn:
			c.execute("DELETE FROM Bank14 WHERE Acc_no =={}".format(acc_n))
	
