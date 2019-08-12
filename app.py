from flask import Flask, render_template, request, redirect, url_for
import os
import pymysql

connection = pymysql.connect(
    host='localhost', # IP address of the database; localhost means "the local machine"
    user="yucheng91",  #the mysql user
    password="coconuty", #the password for the user
    database="expenses" #the name of database we want to use
)

app = Flask(__name__)

@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/viewall')
def viewall():
     cursor = connection.cursor(pymysql.cursors.DictCursor)
     sql = 'SELECT * FROM transaction JOIN categories ON transaction.categoriesid = categories.id JOIN mode ON transaction.modeid = mode.id JOIN account on transaction.accountid = account.id'
     cursor.execute(sql)
     results = []
     for r in cursor:
         results.append(r)
     print(results)
     return render_template('transaction_overview.html', data=results)
     
@app.route('/new-transaction/', methods=["GET"])
def new_supplier():
    return render_template('new_transaction.html')
    
@app.route('/new-transaction/', methods=["POST"])
def addtransaction():
    transaction_name = request.form.get("transaction")
    category_name = request.form.get("category")
    mode_name = request.form.get("mode")
    by_name = request.form.get("by")
    debit_name = request.form.get("debit")
    credit_name = request.form.get("credit")
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    sql = "INSERT INTO transaction (description) VALUES ('{}')".format(transaction_name);
    "INSERT INTO categories (name) VALUES ('{}')".format(category_name);
    "INSERT INTO mode (description) VALUES ('{}')".format(mode_name);
    "INSERT INTO account (description) VALUES ('{}')".format(by_name);
    "INSERT INTO transaction (debit) VALUES ('{}')".format(debit_name);
    "INSERT INTO transaction (credit) VALUES ('{}')".format(credit_name);

    cursor.execute(sql)
    connection.commit() 
    
    return "Transaction record has been added"

# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)