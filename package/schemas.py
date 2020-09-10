from package import ma

class QuestionSchema(ma.Schema):
  class Meta:
    fields = (
      "exam",
      "category",
      "question",
      "question_image",
      "question_type",
      "answer_1",
      "answer_2",
      "answer_3",
      "answer_4",
      "source",
    )

questions_schema = QuestionSchema(many=True)