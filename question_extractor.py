from models import *
from openai import OpenAI


def question_extractor(question_text: str, client: OpenAI):
    completion = client.beta.chat.completions.parse(
        model="gpt-4o-2024-08-06",
        messages=[
            {"role": "system", "content": "Extract the question information, saving every bit of information available in the question"},
            {"role": "user", "content": "Question: " + question_text},
        ],
        response_format=MultipleChoiceQuestion,
    )

    event = completion.choices[0].message.parsed

    return event
