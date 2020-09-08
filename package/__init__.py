from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)

app.config['SECRET_KEY'] = '59ad26e5cb630aab0c78a64b86d145483d2e387c47538ab46d3f64a88e06b62c'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from package import routes
from package.models import User

@login_manager.user_loader
def load_user(user_id):
  return User.query.get(int(user_id))