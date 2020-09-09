from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, BooleanField
from flask_wtf.file import FileField, FileAllowed
from wtforms.validators import DataRequired, Length, InputRequired
from markupsafe import Markup
from package import db
from package.models import Category

class LoginForm(FlaskForm):
  username = StringField('Username', 
    validators=[
      DataRequired(),
      Length(min=2, max=10),
    ]
  )
  password = PasswordField('Password', 
    validators=[
      DataRequired(),
    ]
  )
  remember = BooleanField('Remember Me?')
  submit = SubmitField('Log In')

class AddQuestionForm(FlaskForm):
  category = SelectField(
    choices=[
      ('', '---'),
    ],
    validators=[
      DataRequired(),
    ],
    default=None,
    validate_choice=False,
  )
  question_image = FileField('Image (Optional)',
    validators=[
      FileAllowed(['jpg', 'png'])
    ]
  )
  question = StringField('Question', 
    validators=[
      DataRequired(),
      Length(min=2, max=200),
    ]
  )
  question_type = SelectField(
    choices=[
      ('', '---'),
      ('Multiple Choice', 'Multiple Choice'),
      ('Boolean', 'Boolean'),
      ('Multiple Select', 'Multiple Select')
    ],
    validators=[
      DataRequired(),
    ],
    default=None,
  )
  answer_1 = StringField('Answers', 
    validators=[
      DataRequired(),
      Length(min=2, max=50),
    ]
  )
  correct_1 = BooleanField('')
  answer_2 = StringField('', 
    validators=[
      DataRequired(),
      Length(min=2, max=50),
    ]
  )
  correct_2 = BooleanField('')
  answer_3 = StringField('', 
    validators=[
      DataRequired(),
      Length(min=2, max=50),
    ]
  )
  correct_3 = BooleanField('')
  answer_4 = StringField('', 
    validators=[
      DataRequired(),
      Length(min=2, max=50),
    ]
  )
  correct_4 = BooleanField('')
  source = StringField('Source', 
    validators=[
      DataRequired(),
      Length(min=2, max=50),
    ]
  )
  submit = SubmitField('Add')

class ViewQuestionForm(FlaskForm):
  delete = SubmitField('Delete Question')

  def __init__(self, question):
    super().__init__()
    self.category = question.category
    self.question =  question.question
    self.question_type = question.question_type
    self.question_image = question.question_image
    self.answer_1 = question.answer_1
    self.answer_2 = question.answer_2
    self.answer_3 = question.answer_3
    self.answer_4 = question.answer_4
    self.source = question.source