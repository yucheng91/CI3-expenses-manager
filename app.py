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

@app.route('/view-all')
def viewall():
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    sql = "SELECT * FROM transaction JOIN categories ON transaction.categoriesid = categories.id JOIN mode ON transaction.modeid = mode.id JOIN account on transaction.accountid = account.id"
    cursor.execute(sql)
    results = []
    for r in cursor:
         results.append(r)
         
    sql = "SELECT SUM(debit) AS totaldebit FROM transaction"
    cursor.execute(sql)
    totaldebit = cursor.fetchone()
    
    sql = "SELECT SUM(credit) AS totalcredit FROM transaction"
    cursor.execute(sql)
    totalcredit = cursor.fetchone()

    sql = "SELECT (SELECT SUM(debit) AS sumdebit FROM transaction) - (SELECT SUM(credit) AS sumcredit FROM transaction) AS balance FROM transaction"
    cursor.execute(sql)
    balance = cursor.fetchone()

    return render_template('transaction_overview.html', data=results, totaldebit = totaldebit, totalcredit = totalcredit,balance=balance)
     
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
        
    sql = "SELECT * FROM tag"
    cursor.execute(sql)
    tag = []
    for r in cursor:
        tag.append({
            'id':r['id'],
            'name': r['tname']
        })
    
    return render_template('new_transaction.html', mode=mode, categories=categories, account=account, tag=tag)
    
@app.route('/new-transaction/', methods=["POST"])
def process_addtransaction():
    transaction_name = request.form.get("transaction")
    category_name = request.form.get("category")
    mode_name = request.form.get("mode")
    by_name = request.form.get("by")
    debit_name = request.form.get("debit")
    if request.form.get("debit") == "":
        debit_name = "0"
        
    credit_name = request.form.get("credit")
    if request.form.get("credit") == "":
        credit_name = "0"
        
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    
    sql = "INSERT INTO transaction (description,categoriesid,modeid,accountid,debit,credit) VALUE (%s,%s,%s,%s,%s,%s)"
    cursor.execute(sql,[transaction_name,category_name,mode_name,by_name,debit_name,credit_name])
    
    transactionid = cursor.lastrowid
    tagid = request.form.getlist("tag")
    for t in tagid:
        sql = "INSERT INTO transactiontag (transactionid,tagid) VALUE (%s,%s)"
        cursor.execute(sql,[transactionid,t])
    
    connection.commit() 
    return redirect(url_for('viewall'))

# Edit transaction
@app.route('/view-all/edit/<id>')
def edit_transaction(id):
    
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    sql = "SELECT * FROM transaction JOIN transactiontag ON transaction.id = transactiontag.transactionid JOIN tag ON transactiontag.tagid = tag.id WHERE transaction.id = {}".format(id)
    cursor.execute(sql)
    transaction = cursor.fetchone()
    
    sql = "DELETE FROM transactiontag WHERE transactiontag.transactionid = {}".format(id)
    cursor.execute(sql)

    sql = "SELECT * FROM mode"
    cursor.execute(sql)
    mode = []
    for r in cursor:
        mode.append({
            'id' : r['id'],
            'name': r['mname']
        })
        
    sql = "SELECT * FROM categories"
    cursor.execute(sql)
    categories = []
    for r in cursor:
        categories.append({
            'id':r['id'],
            'name': r['cname']
        })
    
    sql = "SELECT * FROM account"
    cursor.execute(sql)
    account = []
    for r in cursor:
        account.append({
            'id':r['id'],
            'name': r['aname']
        })
        
    sql = "SELECT * FROM tag"
    cursor.execute(sql)
    tag = []
    for r in cursor:
        tag.append({
            'id':r['id'],
            'name': r['tname']
        })
        
    return render_template('edit_transaction.html', transaction = transaction, mode=mode, categories=categories, account=account, tag=tag)

@app.route('/view-all/edit/<id>', methods=['POST'])
def update_transaction(id):
    transaction_name = request.form.get("transaction")
    category_name = request.form.get("category")
    mode_name = request.form.get("mode")
    by_name = request.form.get("by")
    debit_name = request.form.get("debit")
    if request.form.get("debit") == "":
        debit_name = "0"
        
    credit_name = request.form.get("credit")
    if request.form.get("credit") == "":
        credit_name = "0"
        
    cursor = connection.cursor(pymysql.cursors.DictCursor)

    cursor.execute("UPDATE transaction SET description = '{}',categoriesid = '{}',modeid = '{}',accountid = '{}',debit = '{}',credit = '{}' WHERE id = {}".format(transaction_name,category_name,mode_name,by_name,debit_name,credit_name,id))
    
    tagid = request.form.getlist("tag")
    for t in tagid:
        sql = "INSERT INTO transactiontag (transactionid,tagid) VALUE (%s,%s)"
        cursor.execute(sql,[id,t])
        
    connection.commit() 
    return redirect(url_for('viewall'))
    
@app.route('/view-all/delete/<id>')
def confirm_delete_transaction(id):
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    sql = "SELECT * FROM transaction JOIN categories ON transaction.categoriesid = categories.id JOIN mode ON transaction.modeid = mode.id JOIN account on transaction.accountid = account.id WHERE transaction.id = {}".format(id)
    cursor.execute(sql)
    transaction = cursor.fetchone()
    
    return render_template('delete_transaction.html', transaction = transaction)

@app.route('/view-all/delete/<id>', methods=['POST'])
def delete_transaction(id):
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    sql = "DELETE FROM transactiontag WHERE transactiontag.transactionid = {}".format(id)
    cursor.execute(sql)
    
    sql = "DELETE FROM transaction WHERE transaction.id = {}".format(id)
    cursor.execute(sql)
    
    connection.commit()
    return redirect(url_for('viewall'))
    
# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)