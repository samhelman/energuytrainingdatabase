from package import db
from flask_login import UserMixin

class Category(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  category = db.Column(db.String(20), unique=True, nullable=False)

  def __repr__(self):
    return f"Category('{self.category}')"

class User(db.Model, UserMixin):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(20), unique=True, nullable=False)
  password = db.Column(db.String(60), nullable=False)

  def __repr__(self):
    return f"User('{self.username}')"

class Question(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  exam = db.Column(db.String(10), nullable=False)
  category = db.Column(db.String(10), nullable=False)
  question = db.Column(db.String(100), nullable=False)
  question_type = db.Column(db.String(100), nullable=False)
  question_image = db.Column(db.String(100), nullable=True) 
  answers = db.Column(db.String(255), nullable=False)
  source = db.Column(db.String(100), nullable=False)

  def __repr__(self):
    return f"Question('{self.question_type}', '{self.question}')"