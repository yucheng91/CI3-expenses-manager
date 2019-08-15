from flask import Flask, render_template, request, redirect, url_for
import os
import pymysql

connection = pymysql.connect(
    host='localhost', # IP address of the database; localhost means "the local machine"
    user="yucheng91",  #the mysql user
    password="coconuty", #the password for the user
    database="expenses" #the name of database we want to use
)

#if PHP doesn't show, perform $ sudo apt-get install --reinstall libapache2-mod-php7.2

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
def addtransaction():
    
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    sql = "SELECT * FROM mode"
    # fetch all genres and store it in a list
    cursor.execute(sql)
    mode = []
    for r in cursor:
        mode.append({
            'id' : r['id'],
            'name': r['mname']
        })
        
    # fetch all media type and store it in a list
    sql = "SELECT * FROM categories"
    cursor.execute(sql)
    categories = []
    for r in cursor:
        categories.append({
            'id':r['id'],
            'name': r['cname']
        })
    
    # fetch all media type and store it in a list
    sql = "SELECT * FROM account"
    cursor.execute(sql)
    account = []
    for r in cursor:
        account.append({
            'id':r['id'],
            'name': r['aname']
        })
    
    return render_template('new_transaction.html', mode=mode, categories=categories, account=account)
    
# @app.route('/new-transaction/', methods=["POST"])
# def process_addtransaction():
#     transaction_name = request.form.get("transaction")
#     category_name = request.form.get("category")
#     mode_name = request.form.get("mode")
#     by_name = request.form.get("by")
#     debit_name = request.form.get("debit")
#     credit_name = request.form.get("credit")
#     cursor = connection.cursor(pymysql.cursors.DictCursor)

#     connection.commit() 
    
#     return "Transaction record has been added"

# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)