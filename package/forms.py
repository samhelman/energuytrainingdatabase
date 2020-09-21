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
  exam = SelectField('Exam Type',
    choices=[
      ('', '---'),
      ('EA', 'EA'),
      ('MAIN', 'MAIN'),
    ],
    validators=[
      DataRequired(),
    ],
    default=None,
  )
  category = SelectField('Category',
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
    ]
  )
  question_type = SelectField(
    choices=[
      ('', '---'),
      ('Multiple Choice', 'Multiple Choice'),
      ('Boolean', 'Boolean'),
      ('Multiple Select', 'Multiple Select'),
    ],
    validators=[
      DataRequired(),
    ],
    default=None,
  )
  answer_1 = StringField('Answers', 
    validators=[
      DataRequired(),
    ]
  )
  correct_1 = BooleanField('')
  answer_2 = StringField('', 
    validators=[
      DataRequired(),
    ]
  )
  correct_2 = BooleanField('')
  answer_3 = StringField('', 
    validators=[
      DataRequired(),
    ]
  )
  correct_3 = BooleanField('')
  answer_4 = StringField('', 
    validators=[
      DataRequired(),
    ]
  )
  correct_4 = BooleanField('')
  source = StringField('Source', 
    validators=[
      DataRequired(),
    ]
  )
  submit = SubmitField('Add')

class EditQuestionForm(FlaskForm):
  exam = StringField('Exam Type',
    validators=[
      DataRequired(),
    ],
  )
  category = StringField('Category',
    validators=[
      DataRequired(),
    ],
  )
  question_image = FileField('Image (Optional)',
    validators=[
      FileAllowed(['jpg', 'png'])
    ]
  )
  question = StringField('Question', 
    validators=[
      DataRequired(),
    ]
  )
  question_type = StringField('Question Type',
    validators=[
      DataRequired(),
    ],
  )
  answer_1 = StringField('Answers', 
    validators=[
      DataRequired(),
    ]
  )
  answer_2 = StringField('', 
    validators=[
      DataRequired(),
    ]
  )
  answer_3 = StringField('', 
    validators=[
      DataRequired(),
    ]
  )
  answer_4 = StringField('', 
    validators=[
      DataRequired(),
    ]
  )
  source = StringField('Source', 
    validators=[
      DataRequired(),
    ]
  )
  delete_image = BooleanField('')
  submit = SubmitField('Submit Changes')

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