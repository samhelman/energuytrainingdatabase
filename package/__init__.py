from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_restful import Api

app = Flask(__name__)

app.config['SECRET_KEY'] = '59ad26e5cb630aab0c78a64b86d145483d2e387c47538ab46d3f64a88e06b62c'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://lpclwmwqhyggeh:ba1120790c77bd62cff3deaab8fa4b404a5e71be678146e53d6c5e1d2861072e@ec2-54-158-222-248.compute-1.amazonaws.com:5432/ddoap02q09ivuk'
app.config['TEMPLATE_AUTO_RELOAD'] = True
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

db = SQLAlchemy(app)
ma = Marshmallow(app)
api = Api(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from package import routes
from package.models import User
from package.schemas import QuestionSchema, questions_schema
from package.resources import QuestionListResource, QuestionListSheetsResource

@login_manager.user_loader
def load_user(user_id):
  return User.query.get(int(user_id))

api.add_resource(QuestionListResource, '/get-questions')
api.add_resource(QuestionListSheetsResource, '/get-sheets-questions')
