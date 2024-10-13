from pydantic import BaseModel


class QuestionOption(BaseModel):
    label: str
    value: str

class MultipleChoiceQuestion(BaseModel):
    text: str
    options: list[QuestionOption]
    correct_answer: str

class CompleteTest(BaseModel):
    questions: list[MultipleChoiceQuestion]
    