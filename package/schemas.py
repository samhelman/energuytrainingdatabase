from package import ma

class QuestionSchema(ma.Schema):
  class Meta:
    fields = (
      "exam",
      "category",
      "question",
      "question_image",
      "question_type",
      "answers",
      "source",
    )

questions_schema = QuestionSchema(many=True)