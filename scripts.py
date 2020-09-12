import os

from package import db, bcrypt
from package.models import User, Category

def hash_password(password):
  return bcrypt.generate_password_hash(password).decode('utf-8')

def create_user(username, password):
  pw_hash = hash_password(password)
  user = User(username=username, password=pw_hash)
  try:
    db.session.add(user)
    db.session.commit()
  except:
    print('An error occurred, please try again with a different username')

def delete_user(username):
  user = User.query.filter_by(username=username).first()
  try:
    db.session.delete(user)
    db.session.commit()
  except:
    print('That username does not exist')

def add_category(category):
  category = Category(category=category)
  try:
    db.session.add(category)
    db.session.commit()
  except:
    print('An error occurred, please try again with a different username')

def delete_category(category):
  category = Category.query.filter_by(category=category).first()
  try:
    db.session.delete(category)
    db.session.commit()
  except:
    print('That category does not exist')