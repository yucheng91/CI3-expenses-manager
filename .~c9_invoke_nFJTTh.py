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
def index():
     cursor = connection.cursor(pymysql.cursors.DictCursor)
     sql = 'SELECT * FROM transaction JOIN categories ON transaction.categoriesid = categories.id JOIN mode ON transaction.modeid = mode.id JOIN account on transaction.accountid = account.id'
     cursor.execute(sql)
     results = []
     for r in cursor:
         results.append(r)
     print(results)
     return render_template('index.html', data=results)
     
def new_transaction():
     cursor = connection.cursor(pymysql.cursors.DictCursor)
     sql = 'SELECT * FROM transaction JOIN categories ON transaction.categoriesid = categories.id JOIN mode ON transaction.modeid = mode.id JOIN account on transaction.accountid = account.id'
     cursor.execute(sql)
     results = []
     for r in cursor:
         results.append(r)
     print(results)
     return render_template('index.html', data=results)

# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)