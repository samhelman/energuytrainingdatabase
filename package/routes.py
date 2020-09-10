import secrets
import os
from flask import render_template, flash, redirect, url_for, request
from package import app, db, bcrypt
from package.forms import LoginForm, AddQuestionForm, ViewQuestionForm
from package.models import User, Question, Category
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

def save_picture(form_picture):
  random_hex = secrets.token_hex(8)
  _, f_ext = os.path.splitext(form_picture.filename)
  picture_fn = random_hex + f_ext
  picture_path = os.path.join(app.root_path, 'static/images', picture_fn)
  form_picture.save(picture_path)
  return picture_fn

@app.route('/add-question', methods=['GET', 'POST'])
@login_required
def add_question():
  form = AddQuestionForm()
  if form.validate_on_submit():
    exam = form.exam.data
    category = form.category.data
    question = form.question.data
    question_type = form.question_type.data
    question_image = form.question_image.data
    if question_image:
      question_image = save_picture(question_image)
    answer_1 = form.answer_1.data
    correct_1 = form.correct_1.data
    answer_2 = form.answer_2.data
    correct_2 = form.correct_2.data
    answer_3 = form.answer_3.data
    correct_3 = form.correct_3.data
    answer_4 = form.answer_4.data
    correct_4 = form.correct_4.data
    source = form.source.data
    question = Question(
      exam=exam,
      category=category, 
      question=question,
      question_type=question_type,
      question_image=question_image,
      answer_1=f'{answer_1} ({correct_1})',
      answer_2=f'{answer_2} ({correct_2})',
      answer_3=f'{answer_3} ({correct_3})',
      answer_4=f'{answer_4} ({correct_4})',
      source=source,
    )
    try:
      db.session.add(question)
      db.session.commit()
      flash('Question added successfully.', 'success')
    except:
      flash('Something went wrong...', 'failure')
    return redirect(url_for('add_question'))
  return render_template('add-question.html', title = 'Add Question', form=form, categories=Category.query.all())

@app.route('/questions', methods=['GET', 'POST'])
@login_required
def questions():
  questions = Question.query.all()
  return render_template('questions.html', title = 'Questions', questions=questions)

@app.route('/delete/<int:id>')
@login_required
def delete(id):
  try:
    question = Question.query.filter_by(id=id).first()
    db.session.delete(question)
    db.session.commit()
    flash('Question deleted successfully.', 'success')
  except:
    flash('There was a problem deleting that record.', 'failure')
  return redirect(url_for('questions'))

@app.route('/add-category/<string:category>')
@login_required
def add_category(category):
  try:
    category = Category(category=category)
    db.session.add(category)
    db.session.commit()
  except:
    flash('There was a problem adding that category.', 'failure')
  return redirect(url_for('add_question'))

@app.route('/get-image/<string:img>')
@login_required
def get_image(img):
  return redirect(url_for('static', filename='images/' + img))
  