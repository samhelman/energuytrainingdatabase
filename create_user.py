import os

from package import db, bcrypt
from package.models import User

def hash_password(password):
  return bcrypt.generate_password_hash(password).decode('utf-8')

def create_user(username, password):
  pw_hash = hash_password(password)
  user = User(username=username, password=pw_hash)
  db.session.add(user)
  db.session.commit()

def delete_user(username):
  user = User.query.filter_by(username=username).first()
  try:
    db.session.delete(user)
    db.session.commit()
  except:
    print('That username does not exist')