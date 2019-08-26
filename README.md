# Family Money Tracker

[Click here for website](to be deployed)

_Developed By Yu Cheng_

## Index
1. Introduction
2. UI/UX
3. Technologies Used
4. Features
5. Testing
6. Deployment
7. Credit

## Introduction
This project is developed as a money tracker for a family for better management of family budget.  

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
4. MySQL
5. PhpMyAdmin
6. Javascript
7. Chart.JS
8. FontAwesome

### Features
- Main page : Overview of all the income/expenses/balance via Chart.JS
- Add Transaction : Enable users to add in their transaction easily
- History : View all the transaction history, along with the ability to edit/delete them

Chart.JS will auto-update based on the value changed during each create/modify/delete of transaction

### Testing
As this is a website based on data input by users to the database, Jasmine testing is not used hence all the testing has been done manually.  
The following are the test result:
- Keying in negative value (eg: -2000) in either debit/credit will directly substract the amount from their respective field. However taking into consideration in scenario where we received any cashback/reimbusement/discount (eg: spent $1000 and received $100 cashback for same purchase in later time), it is not considered as additional income so it should be substracted under the credit amount itself. 
- For the chart.js, information are passed from app.py to index.html through flask. As those figures are necessary for the chart, the script for chart.js are included in the index.html itself for the chart visualization purposes.

### Deployment
Most of the development has been developed on GitHub and deployed on Heroku as final product.
