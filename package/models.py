from package import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(20), unique=True, nullable=False)
  password = db.Column(db.String(60), nullable=False)

  def __repr__(self):
    return f"User('{self.username}')"

class Question(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  exam_type = db.Column(db.String(10), nullable=False)
  question_type = db.Column(db.String(10), nullable=False)
  question = db.Column(db.String(100), nullable=False)
  question_image = db.Column(db.String(100), nullable=True)
  correct_answer = db.Column(db.String(100), nullable=False)
  source = db.Column(db.String(100), nullable=False)
  wrong_answer_1 = db.Column(db.String(100), nullable=False)
  wrong_answer_2 = db.Column(db.String(100), nullable=False)
  wrong_answer_3 = db.Column(db.String(100), nullable=False)

  def __repr__(self):
    return f"User('{self.exam_type}', '{self.question_type}', '{self.question}')"