from flask import Flask, render_template, request, redirect, url_for
import os
import pymysql
import urllib.parse
from urllib.parse import urlparse

urllib.parse.uses_netloc.append('mysql')

url = urlparse(os.environ['CLEARDB_DATABASE_URL']) 
name = url.path[1:]
user = url.username
password= url.password
host = url.hostname
port= url.port

def connect():
    connection = pymysql.connect(
        host=host,
        user=user,
        password=password,
        port=port,
        database=name
    )
    return connection

app = Flask(__name__,template_folder='templates',static_folder='static')

@app.route('/')
def home():
    connection = connect()
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    sql = "SELECT SUM(debit) AS totaldebit FROM transaction"
    cursor.execute(sql)
    totaldebit = cursor.fetchone()
    cursor.close()
    
    cursor = connection.cursor(pymysql.cursors.DictCursor)    
    sql = "SELECT SUM(credit) AS totalcredit FROM transaction"
    cursor.execute(sql)
    totalcredit = cursor.fetchone()
    cursor.close()

    cursor = connection.cursor(pymysql.cursors.DictCursor)
    sql = "SELECT (SELECT SUM(debit) AS sumdebit FROM transaction) - (SELECT SUM(credit) AS sumcredit FROM transaction) AS balance FROM transaction"
    cursor.execute(sql)
    balance = cursor.fetchone()
    cursor.close()
    
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    sql = "SELECT aname FROM account WHERE id = 1"
    cursor.execute(sql)
    name1 = cursor.fetchone()
    cursor.close()

    cursor = connection.cursor(pymysql.cursors.DictCursor)
    sql = "SELECT aname FROM account WHERE id = 2"
    cursor.execute(sql)
    name2 = cursor.fetchone()

    cursor = connection.cursor(pymysql.cursors.DictCursor)
    sql = "SELECT aname FROM account WHERE id = 3"
    cursor.execute(sql)
    name3 = cursor.fetchone()
    cursor.close()
    
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    sql = "SELECT SUM(debit) AS debit1 FROM transaction WHERE accountid = 1"
    cursor.execute(sql)
    debit1 = cursor.fetchone()
    cursor.close()
    
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    sql = "SELECT SUM(debit) AS debit2 FROM transaction WHERE accountid = 2"
    cursor.execute(sql)
    debit2 = cursor.fetchone()
    cursor.close()

    cursor = connection.cursor(pymysql.cursors.DictCursor)    
    sql = "SELECT SUM(debit) AS debit3 FROM transaction WHERE accountid = 3"
    cursor.execute(sql)
    debit3 = cursor.fetchone()
    cursor.close()
  
    cursor = connection.cursor(pymysql.cursors.DictCursor)  
    sql = "SELECT SUM(credit) AS credit1 FROM transaction WHERE accountid = 1"
    cursor.execute(sql)
    credit1 = cursor.fetchone()
    cursor.close()

    cursor = connection.cursor(pymysql.cursors.DictCursor)  
    sql = "SELECT SUM(credit) AS credit2 FROM transaction WHERE accountid = 2"
    cursor.execute(sql)
    credit2 = cursor.fetchone()
    cursor.close()

    cursor = connection.cursor(pymysql.cursors.DictCursor)    
    sql = "SELECT SUM(credit) AS credit3 FROM transaction WHERE accountid = 3"
    cursor.execute(sql)
    credit3 = cursor.fetchone()
    cursor.close()
    connection.close()
    
    return render_template('index.html',totaldebit = totaldebit, totalcredit = totalcredit,balance=balance,debit1 = debit1,debit2 = debit2,debit3 = debit3,credit1=credit1,credit2=credit2,credit3=credit3, name1=name1, name2=name2, name3=name3)

@app.route('/view-all')
def viewall():
    connection = connect()
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    sql = "SELECT * FROM transaction JOIN categories ON transaction.categoriesid = categories.id JOIN mode ON transaction.modeid = mode.id JOIN account on transaction.accountid = account.id ORDER BY transaction.id"
    cursor.execute(sql)
    results = []
    for r in cursor:
         results.append(r)
         
    cursor.close()
    connection.close()
    return render_template('transaction_overview.html', data=results)
     
@app.route('/new-transaction/', methods=["GET"])
def addtransaction():
    connection = connect()
    
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    sql = "SELECT * FROM mode"
    cursor.execute(sql)
    mode = []
    for r in cursor:
        mode.append({
            'id' : r['id'],
            'name': r['mname']
        })
    cursor.close()
        
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    sql = "SELECT * FROM categories"
    cursor.execute(sql)
    categories = []
    for r in cursor:
        categories.append({
            'id':r['id'],
            'name': r['cname']
        })
    cursor.close()
    
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    sql = "SELECT * FROM account"
    cursor.execute(sql)
    account = []
    for r in cursor:
        account.append({
            'id':r['id'],
            'name': r['aname']
        })
    cursor.close()

    cursor = connection.cursor(pymysql.cursors.DictCursor)        
    sql = "SELECT * FROM tag"
    cursor.execute(sql)
    tag = []
    for r in cursor:
        tag.append({
            'id':r['id'],
            'name': r['tname']
        })
    cursor.close()
    connection.close()
    return render_template('new_transaction.html', mode=mode, categories=categories, account=account, tag=tag)
    
@app.route('/new-transaction/', methods=["POST"])
def process_addtransaction():
    connection = connect()
    transaction_name = request.form.get("transaction")
    category_name = request.form.get("category")
    mode_name = request.form.get("mode")
    by_name = request.form.get("by")
    
    debit_name = request.form.get("debit")
    if debit_name == "":
        debit_name = 0
        
    credit_name = request.form.get("credit")
    if credit_name == "":
        credit_name = 0
        
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    
    sql = "INSERT INTO transaction (description,categoriesid,modeid,accountid,debit,credit) VALUE (%s,%s,%s,%s,%s,%s)"
    cursor.execute(sql,[transaction_name,category_name,mode_name,by_name,debit_name,credit_name])
    
    transactionid = cursor.lastrowid
    tagid = request.form.getlist("tag")
    for t in tagid:
        sql = "INSERT INTO transactiontag (transactionid,tagid) VALUE (%s,%s)"
        cursor.execute(sql,[transactionid,t])
    
    connection.commit()
    cursor.close()
    connection.close()
    return redirect(url_for('viewall'))
    
# Edit transaction
@app.route('/view-all/edit/<id>')
def edit_transaction(id):
    
    connection = connect()
    
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    sql = "SELECT * FROM transaction WHERE id = {}".format(id)
    cursor.execute(sql)
    transaction = cursor.fetchone()
    cursor.close()
    
    cursor = connection.cursor(pymysql.cursors.DictCursor)    
    sql = "SELECT * FROM mode"
    cursor.execute(sql)
    mode = []
    for r in cursor:
        mode.append({
            'id' : r['id'],
            'name': r['mname']
        })
    cursor.close()
        
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    sql = "SELECT * FROM categories"
    cursor.execute(sql)
    categories = []
    for r in cursor:
        categories.append({
            'id':r['id'],
            'name': r['cname']
        })
    cursor.close()
        
    cursor = connection.cursor(pymysql.cursors.DictCursor)  
    sql = "SELECT * FROM account"
    cursor.execute(sql)
    account = []
    for r in cursor:
        account.append({
            'id':r['id'],
            'name': r['aname']
        })
    cursor.close()
        
    cursor = connection.cursor(pymysql.cursors.DictCursor)        
    sql = "SELECT * FROM tag"
    cursor.execute(sql)
    tag = []
    for r in cursor:
        tag.append({
            'id':r['id'],
            'name': r['tname']
        })
    cursor.close()
    
    connection.close()
    
    return render_template('edit_transaction.html', transaction = transaction, mode=mode, categories=categories, account=account, tag=tag)

@app.route('/view-all/edit/<id>', methods=['POST'])
def update_transaction(id):
    connection = connect()
    
    #Delete previous tag due to editing
    cursor = connection.cursor(pymysql.cursors.DictCursor)    
    sql = "DELETE FROM transactiontag WHERE transactionid = {}".format(id)
    cursor.execute(sql)
    cursor.close()
    
    transaction_name = request.form.get("transaction")
    category_name = request.form.get("category")
    mode_name = request.form.get("mode")
    by_name = request.form.get("by")
    
    debit_name = request.form.get("debit")
    if debit_name == "":
        debit_name = 0
        
    credit_name = request.form.get("credit")
    if credit_name == "":
        credit_name = 0
        
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    cursor.execute("UPDATE transaction SET description = '{}',categoriesid = '{}',modeid = '{}',accountid = '{}',debit = '{}',credit = '{}' WHERE id = {}".format(transaction_name,category_name,mode_name,by_name,debit_name,credit_name,id))
    cursor.close()
        
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    tagid = request.form.getlist("tag")
    for t in tagid:
        sql = "INSERT INTO transactiontag (transactionid,tagid) VALUE (%s,%s)"
        cursor.execute(sql,[id,t])
        
    connection.commit() 
    cursor.close()
    connection.close()
    return redirect(url_for('viewall'))
    
@app.route('/view-all/delete/<id>')
def confirm_delete_transaction(id):
    connection = connect()
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    sql = "SELECT * FROM transaction JOIN categories ON transaction.categoriesid = categories.id JOIN mode ON transaction.modeid = mode.id JOIN account on transaction.accountid = account.id WHERE transaction.id = {}".format(id)
    cursor.execute(sql)
    transaction = cursor.fetchone()
    cursor.close()
    connection.close()
    return render_template('delete_transaction.html', transaction = transaction)

@app.route('/view-all/delete/<id>', methods=['POST'])
def delete_transaction(id):
    connection = connect()
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    sql = "DELETE FROM transactiontag WHERE transactiontag.transactionid = {}".format(id)
    cursor.execute(sql)
    cursor.close()
        
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    sql = "DELETE FROM transaction WHERE transaction.id = {}".format(id)
    cursor.execute(sql)
    
    connection.commit()
    cursor.close()
    connection.close()
    return redirect(url_for('viewall'))

@app.route('/tags',methods=['GET'])
def tags():
    connection = connect()
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    
    sql = "SELECT * FROM tag"
    cursor.execute(sql)
    tag = []
    for r in cursor:
        tag.append({
            'id':r['id'],
            'name': r['tname']
        })
    
    cursor.close()
    
    cursor = connection.cursor(pymysql.cursors.DictCursor)
        
    tagid = request.args.get('tag')
    if tagid == None:
        tagid = 0
        
    sql = "SELECT * FROM tag JOIN transactiontag ON tag.id = transactiontag.tagid JOIN transaction ON transactiontag.transactionid = transaction.id JOIN categories ON categories.id = transaction.categoriesid JOIN mode ON mode.id = transaction.modeid JOIN account ON account.id = transaction.accountid WHERE tagid={}".format(tagid)
    cursor.execute(sql)
    results = []
    for r in cursor:
         results.append(r)
    cursor.close()
        
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    sql ="SELECT * FROM tag WHERE id={}".format(tagid)
    cursor.execute(sql)
    currenttag = cursor.fetchone()
    
    cursor.close()
    connection.close()
    return render_template('searchtags.html', tag=tag, data=results, currenttag = currenttag)
    
# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)