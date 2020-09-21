from package import db
from flask_login import UserMixin

class Category(db.Model):
  __tablename__ = 'Categories'

  id = db.Column(db.Integer, primary_key=True)
  category = db.Column(db.String(1000), unique=True, nullable=False)

  def __repr__(self):
    return f"Category('{self.category}')"

class User(db.Model, UserMixin):
  __tablename__ = 'Users'

  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(1000), unique=True, nullable=False)
  password = db.Column(db.String(1000), nullable=False)

  def __repr__(self):
    return f"User('{self.username}')"

class Question(db.Model):
  __tablename__ = 'Questions'

  id = db.Column(db.Integer, primary_key=True)
  exam = db.Column(db.String(1000), nullable=False)
  category = db.Column(db.String(1000), nullable=False)
  question = db.Column(db.String(1000), nullable=False)
  question_type = db.Column(db.String(1000), nullable=False)
  question_image = db.Column(db.String(1000), nullable=True)
  answer_1 = db.Column(db.String(2000), nullable=False)
  answer_2 = db.Column(db.String(2000), nullable=False)
  answer_3 = db.Column(db.String(2000), nullable=False)
  answer_4 = db.Column(db.String(2000), nullable=False)
  answers = db.Column(db.String(12000), nullable=False)
  source = db.Column(db.String(1000), nullable=False)

  def __repr__(self):
    return f"Question('{self.question}')"