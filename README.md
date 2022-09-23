# Personal Spending Tracker

This was my first solo project during my 5th week at CodeClan. 


## Brief

Build an app that allows a user to track their spending:
- The app should allow the user to create and edit `Transaction`s.
- The app should allow the user to create and edit `Merchant`s, e.g. Tesco, Amazon, ScotRail.
- The app should allow the user to create and edit `Tag`s for their spending, e.g. groceries, entertainment, transport.
- The user should be able to assign `Tag`s and `Merchant`s to a `Transaction`, as well as an amount spent on each `Transaction`.
- The app should display all the `Transaction`s that a user has made in a single view, with each `Transaction`'s amount, `Merchant` and `Tag`, as well as the total amount of all transactions.


## Getting Started

To get started, clone this repository to a location of your choice.

### Dependencies

* Python3
* Flask
* PostgreSQL


### Installing


* Flask: 
```bash 
pip install Flask
```


### Executing Program

* Create Database with pSQL:
```bash
createdb spending_tracker
```
* Link Database and SQL file from project directory:
```bash 
psql -d spending_tracker -f db/spending_tracker.sql 
```
* Run Flask:
```bash
flask run 
```

Navigate to http://127.0.0.1:5000

