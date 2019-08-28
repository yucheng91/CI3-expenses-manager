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
This project is developed as a expense tracker for a family for better management of family budget.  

In this scenario, the site is set up to manage the expenses between the parents & their only child. 

It provide a simple and clear chart interface at the main page and preset users are able to add/view/modify/delete any of their input at any point in time.

## UI/UX 
### Design
- Bootstrap is used in the development of the site as it provide framework for mobile responsive site. Buttons & table are all based on same Bootstrap framework to ensure consistentcy in design.
- Users are determined upon initial set up in mysql to ensure that the records added are exclusively for the selected user (for example, the family of 3)
- Collapsable nav bar is used to ensure that the navbar will not be blocking additional screen estate on smaller screen size.
- Certain information for input (such as payment mode,categories) are also preset for the user for ease of use and standardise the information in the database.

### User Stories
Several user stories have been considered during the development and set up
- _As the user, I would like to have the breakdown of every information at first glance in the website_
- _As the user, I should be able to navigate the page with ease with the use of icon and buttons_
- _As the user, adding and editing information should be made simple for me_


### Technologies Used
1. HTML/CSS
2. Bootstrap
3. Flask
4. MySQL & PhpMyAdmin (for database creation)
5. ClearDB (for database deployment on Heroku)
5. Javascript (for Chart.JS)
6. Chart.JS (for visualization purposes)
7. FontAwesome (for icon)
8. Google Fonts (for consistency of font in different platform)
9. Heroku (for deployment)

### Features
- Main page : Overview of all the income/expenses/balance via Chart.JS
- Add Transaction : Enable users to add in their transaction easily
- History : View all the transaction history, along with the ability to edit/delete them
- Tag search : users are able to view the transaction based on the tag they have selected as in input. Tagging is optional hence the edit/delete feature only available in History as it contains all the records with/without tagging.
- Chart.JS will auto-update based on the value changed during each create/modify/delete of transaction

### Future Features
- Enable user sign up to make this expenses tracker into a personal application that cater to individual needs.
- Generate more graph for more details visualization.
- Enable tag add/edit/delete for further flexiblility in tagging.

### Testing
The layout has been tested on Windows laptop/Macbook /iPad Mini(2018) /Pixel 2 XL/iPhone SE covering various screen-size. Browsers used for testing are Microsoft Edge, Google Chrome & Apple Safari.
As this is a website based on data input by users to the database through CRUD approach, automated testing is not used hence all the testing has been done manually.  

The following are the test result:
- Keying in negative value (eg: -2000) in either debit/credit will directly substract the amount from their respective field. However taking into consideration in scenario where we received any cashback/reimbusement/discount (eg: spent $1000 and received $100 cashback for same purchase in later time), it is not considered as additional income so it should be substracted under the credit amount itself. 
- For the chart.js, information are passed from app.py to index.html through flask. As those figures are necessary for the chart, the script for chart.js are included in the index.html itself for the chart visualization purposes.
- Tables are only mobile responsive until a certain width where content can never fit into the limited width anymore. In order to prevent excessive overflow scrolling and preserve readability, certain column are hidden to show only the important information in the limited screen width.

### Known Bug/Issue (from testing)
- Any update on ClearDB data through the Heroku site appeared to have slight delay. If changes did not appear, refresh the page while clearing caches will be able to solve the problem.
- Despite hidden column, the table's width is still too wide for small screen devices such as iPhone 5 (4" 16:9 screen), overflow scrolling has been enabled for left to right scrolling in these devices.

### Deployment
Most of the development has been developed on GitHub and deployed on Heroku as final product.
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
- Replace the original pymysql.connect to so that it will connect to ClearDB directly:
```
url = urlparse(os.environ['CLEARDB_DATABASE_URL') name = url.path[1:]
user = url.username
password= url.password
host = url.hostname
port= url.port
connection = pymysql.connect(
host=host,
    user=user,
    password=password,
    port=port,
    database=name
)
```
