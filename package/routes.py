import secrets
import os, boto3
from flask import render_template, flash, redirect, url_for, request
from package import app, db, bcrypt
from package.forms import LoginForm, CreateUserForm, AddQuestionForm, EditQuestionForm, ViewQuestionForm
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
      login_user(user)
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

def upload(form_picture):
  file = form_picture
  random_hex = secrets.token_hex(16)
  _, f_ext = os.path.splitext(file.filename)
  file.filename = random_hex + f_ext
  S3_BUCKET = os.environ.get('S3_BUCKET')
  s3_resource = boto3.resource('s3')
  bucket = s3_resource.Bucket(S3_BUCKET)
  bucket.Object(file.filename).put(Body=file)

  url = f'https://{S3_BUCKET}.s3.amazonaws.com/{file.filename}'

  return url

@app.route('/add-question', methods=['GET', 'POST'])
@login_required
def add_question():
  form = AddQuestionForm()
  correct_1 = form.correct_1.data
  correct_2 = form.correct_2.data
  correct_3 = form.correct_3.data
  correct_4 = form.correct_4.data
  checkboxes = [correct_1, correct_2, correct_3, correct_4]
  if form.validate_on_submit() and True in checkboxes:
    exam = form.exam.data
    category = form.category.data
    question = form.question.data
    question_type = form.question_type.data
    question_image = request.files['question_image']
    if question_image:
      question_image = upload(question_image)
    else:
      question_image = 'No Image'
    answer_1 = form.answer_1.data + f' ({correct_1})'
    answer_2 = form.answer_2.data + f' ({correct_2})'
    answer_3 = form.answer_3.data + f' ({correct_3})'
    answer_4 = form.answer_4.data + f' ({correct_4})'
    source = form.source.data
    question = Question(
      exam=exam,
      category=category, 
      question=question,
      question_type=question_type,
      question_image=question_image,
      answer_1=answer_1,
      answer_2=answer_2,
      answer_3=answer_3,
      answer_4=answer_4,
      answers=f"{answer_1} ({correct_1})\n{answer_2} ({correct_2})\n{answer_3} ({correct_3})\n{answer_4} ({correct_4})",
      source=source,
    )
    try:
      db.session.add(question)
      db.session.commit()
      flash('Question added successfully.', 'success')
    except:
      flash('Something went wrong...', 'failure')
    id = question.id
    return redirect(url_for('add', id=id))
  categories = Category.query.all()
  categories = [catergory.category for catergory in categories]
  categories = sorted(categories)
  return render_template('add-question.html', title = 'Add Question', form=form, categories=categories)

@app.route('/add/<int:id>', methods=['GET', 'POST'])
@login_required
def add(id):
  question = Question.query.filter_by(id=id).first()
  questions = Question.query.all()
  if question in questions:
    return render_template('add-another.html', title = 'Add Question', question=question)
  else:
    return render_template('add-another.html', title = 'Add Question')

@app.route('/questions', methods=['GET', 'POST'])
@login_required
def questions():
  questions = Question.query.all()
  return render_template('questions.html', title = 'Questions', questions=questions)

@app.route('/delete/<int:id>/origin-<string:page>')
@login_required
def delete(id, page):
  try:
    question = Question.query.filter_by(id=id).first()
    db.session.delete(question)
    db.session.commit()
    flash('Question deleted successfully.', 'success')
    return redirect(url_for(page, id=0))
  except:
    flash('There was a problem deleting that record.', 'failure')

@app.route('/delete-question/<int:id>/origin-<string:page>')
@login_required
def delete_question(id, page):
  id = id
  page = page
  return render_template('delete-question.html', id=id, page=page)

@app.route('/edit/<int:id>/origin-<string:page>', methods=["POST", "GET"])
@login_required
def edit_question(id, page):
  entry = Question.query.filter_by(id=id).first()
  form = EditQuestionForm()
  if form.validate_on_submit():
    entry.question = form.question.data
    entry.question_type = form.question_type.data
    entry.category = form.category.data
    entry.answer_1 = form.answer_1.data
    entry.answer_2 = form.answer_2.data
    entry.answer_3 = form.answer_3.data
    entry.answer_4 = form.answer_4.data
    entry.source = form.source.data
    if form.question_image.data:
      entry.question_image = upload(form.question_image.data)
    elif form.delete_image.data == True:
      entry.question_image = 'No Image'
    try:
      db.session.add(entry)
      db.session.commit()
      flash('Question edited successfully.', 'success')
      return redirect(url_for('questions'))
    except:
      flash('Something went wrong...', 'failure')
      return redirect(url_for('edit_question', id=entry.id))  
  return render_template('edit-question.html', title = 'Edit Question', form=form, question=entry, id=id, page=page)

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

def hash_password(password):
  return bcrypt.generate_password_hash(password).decode('utf-8')

def create_user(username, password):
  if current_user.username == 'admin':
    pw_hash = hash_password(password)
    user = User(username=username, password=pw_hash)
    try:
      db.session.add(user)
      db.session.commit()
      flash(f'Account created for {username}', 'success')
    except:
      flash('Something went wrong...', 'failure')
  else: flash('Only the admin user can create new accounts', 'info')

@app.route('/create-account', methods=['GET', 'POST'])
@login_required
def create_account():
  form = CreateUserForm()
  if form.validate_on_submit():
    users = User.query.all()
    usernames = []
    for user in users:
      usernames.append(user.username)
    if form.username.data in usernames:
      flash(f'The username \'{form.username.data}\' already exists!', 'failure')
    else:
      create_user(form.username.data, form.password.data)
      return redirect(url_for('admin'))
  return render_template('create-account.html', title = 'Create Account', form=form)

@app.route('/delete-user/<string:username>')
@login_required
def delete_user(username):
  if username == 'admin':
    flash('Cannot delete admin account', 'failure')
  else:
    user = User.query.filter_by(username=username).first()
    try:
      db.session.delete(user)
      db.session.commit()
      flash(f'The account \'{username}\' has been deleted.', 'success')
    except:
      flash('That username does not exist', 'failure')
  return redirect(url_for('admin'))

@app.route('/admin')
@login_required
def admin():
  users = User.query.all()
  return render_template('admin.html', title = 'Admin', users=users)