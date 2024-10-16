from pydantic import BaseModel


class QuestionOption(BaseModel):
    label: str
    value: str

class MultipleChoiceQuestion(BaseModel):
    text: str
    options: list[QuestionOption]
    correct_answer: str
    tip: str

class CompletTest(BaseModel):
    questions: list[MultipleChoiceQuestion]
    