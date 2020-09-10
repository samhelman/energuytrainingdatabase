from flask_restful import Resource
from package.models import Question
from package.schemas import questions_schema, questions_sheets_schema

class QuestionListResource(Resource):
  def get(self):
    questions = Question.query.all()
    return questions_schema.dump(questions)

class QuestionListSheetsResource(Resource):
  def get(self):
    questions = Question.query.all()
    return questions_sheets_schema.dump(questions)