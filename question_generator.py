from models import *
from question_extractor import question_extractor
from openai import OpenAI
from typing import List
import json


def save_questions_to_json(questions: List[MultipleChoiceQuestion], file_path: str):
    questions_data = [question.model_dump() for question in questions]
    
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(questions_data, f, ensure_ascii=False, indent=4)


def generate_questions_from_instance(question_instance, client: OpenAI):
    prompt_text = (
        f"Dado o seguinte exemplo de questão: {question_instance.text} "
        f"Agora, baseado no exemplo crie outras dez questões"
        f"Cada questão de possuir cinco alternativas "
        f"Todas as questões devem estar em português "
        f"Não escreva o nome da banca "
        f"Mantenha o formato da fração fornecido na questão base"
    )

    completion = client.beta.chat.completions.parse(
        model="gpt-4o-2024-08-06",
        messages=[
            {"role": "system", "content": "Você é um professor especialista em gerar questões para provas de vestibulares"},
            {"role": "user", "content": prompt_text}
        ],
        response_format=CompletTest,
        max_tokens=5000
    )

    return completion.choices[0].message.parsed


def generate_ten_questions(question: str, client: OpenAI):
    question_instance = question_extractor(question_text=question, client=client)
    completion = generate_questions_from_instance(question_instance=question_instance, client=client)

    new_questions = completion.questions

    return new_questions
