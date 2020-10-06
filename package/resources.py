from flask_restful import Resource
from package.models import Question
from package.schemas import questions_schema, ten_questions_schema
import random

class QuestionListResource(Resource):
  def get(self):
    questions = Question.query.all()
    return questions_schema.dump(questions)

class TenQuestionsResource(Resource):
  def get(self):
    questions = Question.query.filter_by(question_type="Multiple Choice").filter_by(question_image="No Image").all()
    sample = random.sample(questions, 10)
    return ten_questions_schema.dump(sample)