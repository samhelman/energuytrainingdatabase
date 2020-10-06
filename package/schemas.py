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

class TenQuestionsSchema(ma.Schema):
    class Meta:
      fields = (
        "question",
        "answer_1",
        "answer_2",
        "answer_3",
        "answer_4",
        "correct_answer",
        "source",
      )

ten_questions_schema = TenQuestionsSchema(many=True)