from flask import render_template, flash, redirect, url_for, request
from package import app, db, bcrypt
from package.forms import LoginForm, AddQuestionForm
from package.models import User
from flask_login import login_user, logout_user, current_user, login_required

@app.route('/')
@app.route('/home')
def home():
  return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
  if current_user.is_authenticated:
    return redirect(url_for('home'))
  form = LoginForm()
  if form.validate_on_submit():
    user = User.query.filter_by(username=form.username.data).first()
    if user and bcrypt.check_password_hash(user.password, form.password.data):
      login_user(user, remember=form.remember.data)
      next_page = request.args.get('next')
      flash(f'{form.username.data} logged in successfully.', 'success')
      return redirect(next_page) if next_page else redirect(url_for('home'))
  else:
    flash('Login Unsuccessful. Please check username and password.', 'failure')
  return render_template('login.html', title = 'Login', form=form)

@app.route('/logout', methods=['GET', 'POST'])
def logout():
  logout_user()
  flash('Logged Out Successfully', 'success')
  return redirect(url_for('home'))

@app.route('/add-question', methods=['GET', 'POST'])
@login_required
def add_question():
  form = AddQuestionForm()
  return render_template('add-question.html', title = 'Add Question', form=form)

@app.route('/questions')
@login_required
def questions():
  return render_template('questions.html', title = 'Questions')