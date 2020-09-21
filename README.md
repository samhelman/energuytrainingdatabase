# energuytrainingdatabase

The purpose of this project was for me to learn how to build a flask app with a database and api to access that database.

This will mark my first attempts at using sqlite databases for development and postgresql databases for production, with AWS S3 for image file persistance, and my first time building an api of any kind. This project was built using Flask, SQLAlchemy and Flask-RESTful.

A user login is required to access the GUI to add/remove database entries. Only one user account exists, with no provision in place to add a new one or restore the password.

No user login is necessary to retrieve data via the API. Data retrieved from the API is in JSON format. Data can be retrieved in the command line like so:

	curl https://energuytrainingdb.herokuapp.com/get-questions > questions.json

Each question contains the following fields: "exam", "category", "question", "question_image", "question_type", "answer_1", "answer_2", "answer_3", "answer_4", and "source". Each of the four answer fields contains a string which represents the answer followed by either "(TRUE)" or "(FALSE)" to indicate whether or not the answer is correct or incorrect (some questions may have more than one correct answer).
