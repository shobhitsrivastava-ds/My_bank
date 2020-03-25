from flask import Flask,render_template,redirect,url_for,request
import wed
from database import bank
import sqlite3
import random
obj = bank()



app=Flask(__name__,template_folder='template')

@app.route("/")
def home():
	return(render_template("home.html"))

# For the bank details
@app.route("/bank_details",methods=["POST","GET"])
def form():
	return(render_template("details.html"))
# For creating the account
@app.route("/create_account",methods=["POST","GET"])
def create_account():
	return(render_template("create_acc.html"))
# For depositing the amount
@app.route("/deposite_amount",methods =["POST","GET"])
def deposite_amount():
	return(render_template("deposite_amt.html"))
# For withdrawing the amount
@app.route("/withdraw_amount",methods =["POST","GET"])
def withdraw_amount():
	return(render_template("withdraw_amt.html"))
# For the account details
@app.route("/account_details",methods =["POST","GET"])
def account_details():
	return(render_template("account_det.html"))

#@app.route("/success")
#def success(data):
#	return(render_template("success.html",data=data))

@app.route("/new_account",methods=["GET","POST"])
def new_account():
	if(request.method=="POST"):
		name = request.form["name"]
		name =str(name)
		sex = request.form["sex"]
		sex=str(sex)
		age = request.form["age"]
		age =int(age)
		acc_type = request.form["type"]
		acc_type=str(acc_type)
		amt = request.form["amt"]
		amt =round(float(amt),2)

		conn = sqlite3.connect("bank.db")
		c= conn.cursor()
		li=[]
		while True:
			n= random.randint(100000,999999)
			if n not in li:
				li.append(n)
				break
			else :
				continue
		with conn:
			c.execute("INSERT INTO Bank18 VALUES(:acc_n,:name,:sex,:age,:type,:bal)",{"acc_n":n,"name":name,"sex":sex,"age":age,"type":acc_type,"bal":amt}) 
		#with conn:
		#	c.execute("CREATE TABLE Bank18 (Acc_no integer,Name text,Sex text, Age integer, Type text,Amount float)")
		#n= obj.get_new_account(name,sex,age,acc_type,amt,conn,c)
		data ={"Acc_num":n}
	return render_template("success.html",data=data)

@app.route("/amt_withdraw",methods=["GET","POST"])
def withdraw_amt():
	if(request.method=="POST"):
		conn = sqlite3.connect("bank.db")
		c= conn.cursor()
		acc_no = request.form["acc_no"]
		name = request.form["name"]
		sex = request.form["sex"]
		age = request.form["age"]
		acc_type = request.form["type"]
		amt = request.form["amt"]
		amt =float(amt)
		c.execute("SELECT Amount FROM Bank18 WHERE Acc_no=:no",{"no":acc_no})
		bal = c.fetchall()
		bal = float(bal[0][0])
		if(bal>amt):
			new_bal =bal-amt
			c.execute("UPDATE Bank14 SET Amount =:nam WHERE Acc_no=:an",{"nam":new_bal,"an":acc_no})
			data = round(new_bal,2)
		else:
			data = "[INFO]!! Insufficient Amount"
		#n = obj.withdraw_amt(acc_no,amt)
	return render_template("withdraw_succ.html",data=data)

@app.route("/amt_deposite",methods=["GET","POST"])
def deposite_amt():
	if(request.method=="POST"):
		conn = sqlite3.connect("bank.db")
		c= conn.cursor()
		acc_no = request.form["acc_no"]
		acc_no =int(acc_no)
		name = request.form["name"]
		sex = request.form["sex"]
		age = request.form["age"]
		acc_type = request.form["type"]
		amt = request.form["amt"]
		amt =float(amt)
		#n = obj.deposite_amt(acc_no,amt)
		with conn:
			c.execute("SELECT Amount FROM Bank18 WHERE Acc_no=:no",{"no":acc_no})
			bal = c.fetchall()
			bal = float(bal[0][0])
			new_bal =bal+amt
			c.execute("UPDATE Bank18 SET Amount =:nb WHERE Acc_no=:an",{"nb":new_bal,"an":acc_no})
			data = round(new_bal,2)
	return render_template("deposite_succ.html",data=data)

@app.route("/acc_details",methods=["GET","POST"])
def account_det():
	if(request.method=="POST"):
		acc_no = request.form["acc_no"]
		acc_no = int(acc_no)
		#data = obj.get_emp_det(acc_no)
		conn = sqlite3.connect("bank.db")
		c= conn.cursor()
		c.execute("SELECT * FROM Bank18 WHERE Acc_no =:name",{"name":acc_no})
		det = c.fetchall()
		acc_n =det[0][0]
		name = det[0][1]
		sex =det[0][2]
		age = det[0][3]
		type_acc= det[0][4]
		bal = det[0][5]
		data = {"acc_n":acc_n, "name":name, "sex":sex, "age":age, "type_acc":type_acc, "balance":bal}
	return render_template("holder_det.html",data=data)

def delete_account():
	if(request.method=="POST"):
		acc_no = request.form["acc_no"]
		acc_no =int(acc_no)
		name = request.form["name"]
		sex = request.form["sex"]
		age = request.form["age"]
		acc_type = request.form["type"]
		amt = request.form["amt"]
		obj.delete_account(acc_no)
	return render_template("success.html",data=data)


if __name__=="__main__":
	app.run(debug=True)

"""app1=wea(str(city))
		data = app1.find_data()
	return render_template("success.html",data=data)"""
