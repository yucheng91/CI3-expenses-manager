# Family Expense Tracker

[Click here for website](https://yc-expensetracker.herokuapp.com/)

_Developed By Yu Cheng_

## Index
1. Introduction
2. UI/UX
3. Technologies Used
4. Features
5. Future Features
6. Testing
7. Known bug/issue
8. Deployment
9. Credit

## Introduction
This project is developed as an expense tracker for a family for better management of the budget.  

In this scenario, the site is set up to manage the expenses between the parents & their only child. 

It provides a simple and clear chart interface at the main page and pre-set users are able to add/view/modify/delete any of their input at any point in time.

## UI/UX 
### Design
- Bootstrap is used in the development of the site as it provides a framework for a mobile responsive site. Buttons & table are all based on the same Bootstrap framework to ensure consistency in design.
- Users are determined upon initial set up in MySQL to ensure that the records added are exclusively for the selected user (for example, the family of 3)
- Collapsible navbar is used to ensure that the navbar will not be blocking additional screen estate on smaller screen size.
- Certain information for input (such as payment mode, categories) are also pre-set for the user for ease of use and standardise the information in the database.

### User Stories
Several user stories have been considered during the development and set up
- _As the user, I would like to have the breakdown of every information at first glance in the website_
- _As the user, I should be able to navigate the page with ease with the use of icon and buttons_
- _As the user, adding and editing information should be made simple for me_

### Wireframe
_Please refer to wireframe folder_

## Technologies Used
1. HTML/CSS
2. Bootstrap
3. Flask
4. MySQL & PhpMyAdmin (for database creation, refer to wireframe for the ER Diagram for this project)
5. ClearDB (for database deployment on Heroku)
5. JavaScript (for Chart.JS)
6. Chart.JS (for visualization purposes)
7. FontAwesome (for the icon)
8. Google Fonts (for consistency of font in the different platform)
9. Heroku (for deployment)

## Features
- Main page: Overview of all the income/expenses/balance via Chart.JS
- Add Transaction: Enable users to add in their transaction easily.
- History: View all the transaction history.
- Edit Transaction: Enable users to edit an existing transaction, do take note that the tags have to be selected again in case the description is changed.
- Delete Transaction: Enable users to delete a transaction that may have been entered by mistake.
- Tags search: users are able to view the transaction based on the tag they have selected as in input. Tagging is optional hence the edit/delete feature only available in History as it contains all the records with/without tagging.
- Chart.JS will auto-update based on the value changed during each creates/modify/delete of transaction

## Future Features
- Enable user sign up to make this expenses tracker into a personal application that caters to individual needs.
- Enable users to form a custom group (such as family, roommates) and combine/sync their personal result into one bigger database.
- Generate more graph for more details visualization.
- Enable tag to add/edit/delete for further flexibility in tagging.
- Create a filter by dates, due to the SQL date based on auto-created date, the data are limited at this moment.

## Testing
The layout has been tested on Windows laptop/MacBook /iPad Mini(2018) /Pixel 2 XL/iPhone SE covering various screen-size. Browsers used for testing are Microsoft Edge, Google Chrome & Apple Safari.
As this is a website based on data input by users to the database through the CRUD approach, automated testing is not used hence all the testing has been done manually.

The following are the test result:
- Keying in negative value (eg: -2000) in either debit/credit will directly subtract the amount from their respective field. However taking into consideration in a scenario where we received any cashback/reimbursement/discount (eg: spent $1000 and received $100 cashback for same purchase in a later time), it is not considered as additional income so it should be subtracted under the credit amount itself. 
- For the chart.js, information is passed from app.py to index.html through the flask. As those figures are necessary for the chart, the script for chart.js is included in the index.html itself for the chart visualization purposes.
- Tables are only mobile responsive until a certain width where content can never fit into the limited width anymore. In order to prevent excessive overflow scrolling and preserve readability, certain column is hidden to show only the important information in the limited screen width.

Test Case:
- No contribution for expenses/income - refer to Sam (Result: Pass)
- Negative value due to cashback/discount – refer to the transaction for “Dyson V10 & 10% cashback “(Result: Pass)
- Able to show transaction under multiple tags – refer to “Grocery” with tags Fairprice/Capitaland/Grocery (Result: Pass)

## Known Bug/Issue (from testing)
- Any update on ClearDB data through the Heroku site may have a slight delay. If changes did not appear, refresh the page while clearing caches will be able to solve the problem.
- Despite hidden column, the table's width is still too wide for small screen devices such as iPhone 5 (4" 16:9 screen), overflow scrolling has been enabled for the left to right scrolling in these devices.
- Inputting single quote symbol ' would potentially affect the SQL input command (example: ```INSERT ('ABC's') INTO database```) will cause a syntax error. Hence I have limited the description input to be alphanumeric along with certain symbol such as #$%(): only.
- The date may have difference due to the on Heroku being defaulted on UTC.  We may proceed to change the timezone on Heroku from our app config page or login into Heroku cil and perform a ```heroku config: add TZ=”<your timezone name based on tz database >”``` to ensure that time reflected are correct.

## Deployment
Most of the development has been developed on GitHub and deployed on Heroku as final product.
[Click here for website](https://yc-expensetracker.herokuapp.com/)

The site is deployed using following methods:
- install Heroku via command ```sudo snap install --classic heroku```
- Login through bash ```heroku login -i```
- Create the app (deployment repo on heroku) through ```heroku create <app_name>```
- followed by ```git remote -v```
- Install gunicorn via ```pip3 install gunicorn```
- Created file called Procfile under root of the folder and add this line ```web gunicorn <python file without .py>:app```
- Create requirements file with ```pip3 freeze --local > requirement.txt```
- followed by ```git add```, ```git commit -m "<message>"``` and ```git push heroku master``` to push it to heroku site

Database from MySQL has been downloaded and imported to ClearDB as MYSQL is not supported natively on Heroku. User can use ClearDB MySQL directly as an Add-on in Heroku and connect it via SQL client such as Dbeaver and add field based on MySQL syntax.
The method of linking MySQL to ClearDB are as following:
- install ClearDB ```heroku addons:create cleardb:ignite``` (take note that ignite is the only free tier for ClearDB)
- perform ```heroku config``` to get the string consists of all the host/user/password/url for ClearDB
- The string will then be breakdown to the following: 
```
The syntax is mysql://<clear_db_user>:<clear_db_password>@<clear_db_host>/<reconnect_url> ?reconnect = true
Example: mysql://b80f8d428xxxxx:f48exxxx@us-cdbr-iron-east-02.cleardb.net/heroku_586 32fb6debxxxx?reconnect=true

# clear_db_host will be: us-cdbr-iron-east-02.cleardb.net 
# clear_db_user will be: B80f8d428xxxxx
# clear_db_password will be: F48exxxx
# reconnect URL will be: heroku_58632fb6debxxxx
```
- ```sudo mysqldump -uroot your_database_name_here > database.sql``` to generate a database in the system and name it database.sql
- Proceed to .bashrc (shown hidden file), and key in the following ``` export CLEARDB_DATABASE_URL="<your ClearDB string which you get when you type in heroku config at the CLI>"```
- Save and restart all terminals
- In app.py, proceed to add the following after last import:
```
import urllib.parse
from urllib.parse import urlparse
urllib.parse.uses_netloc.append('mysql')
```
- Replace the original pymysql.connect to the following so that it will connect to ClearDB directly:
```
url = urlparse(os.environ['CLEARDB_DATABASE_URL') name = url.path[1:]
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
    return connection)
```
- Take note to input ```connection = connect()``` and ```connection.close()``` under the app.route in app.py to prevent timeout error in Heroku deployment, example
```
@app.route('/history')
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
```

## Credit

Images & Background 
- icons8.com - Financial icon as the logo
- webgradients.com - Providing CSS code for the background gradient

Acknowledgements 
- inspiration for this project is from mobile expenses management such as Monefy- Money Manager,Goodbudget
