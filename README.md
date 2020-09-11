# energuytrainingdatabase

The purpose of this project was for me to learn how to build a flask app with a database and api to access that database.

This will mark my first attempts at using sqlite databases for development and postgresql databases for production and building an api of any kind. This project was built using Flask, SQLAlchemy and Flask-RESTful.

A user login is required to access the GUI to add/remove database entries. Only one user account exists, with no provision in place to add a new one or restore the password.

No user login is necessary to retrieve data via the API. Data retrieved from the API is in JSON format. Data can be retrieved in the command line like so:

	curl https://energuytrainingdb.heroku.app/get-questions > questions.json

