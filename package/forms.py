from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, BooleanField
from flask_wtf.file import FileField
from wtforms.validators import DataRequired, Length, InputRequired

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
  exam_type = SelectField(
    choices=[
      ('', '---'),
      ('EA', 'EA'),
      ('MAIN', 'Main'),
    ],
    validators=[
      DataRequired(),
    ]
  )
  question_type = SelectField(
    choices=[
      ('', '---'),
      ('Furnace', 'Furnace'),
      ('Window', 'Window'),
    ],
    validators=[
      DataRequired(),
    ],
    default=None,
  )
  question_image = FileField('Image (Optional)',
    validators=[
      Length(min=2, max=50),
    ]
  )
  question = StringField('Question', 
    validators=[
      DataRequired(),
      Length(min=2, max=200),
    ]
  )
  correct_answer = StringField('Correct Answer', 
    validators=[
      DataRequired(),
      Length(min=2, max=50),
    ]
  )
  wrong_answer_1 = StringField('Wrong Answers', 
    validators=[
      DataRequired(),
      Length(min=2, max=50),
    ]
  )
  wrong_answer_2 = StringField('', 
    validators=[
      DataRequired(),
      Length(min=2, max=50),
    ]
  )
  wrong_answer_3 = StringField('', 
    validators=[
      DataRequired(),
      Length(min=2, max=50),
    ]
  )
  source = StringField('Source', 
    validators=[
      DataRequired(),
      Length(min=2, max=50),
    ]
  )
  submit = SubmitField('Add')