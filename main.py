from models import *
from openai import OpenAI

client = OpenAI()

completion = client.beta.chat.completions.parse(
    model="gpt-4o-2024-08-06",
    messages=[
        {"role": "system", "content": "You are an expert at generating educational exam questions."},
        {"role": "user", "content": (
            "Here is a sample math question: "
            "Para fazer a tubulação de água em um terreno retangular de dimensões 32 m e 24 m, "
            "um pedreiro optou por passar um cano unindo dois vértices opostos do terreno. "
            "Qual o valor do seno do ângulo formado entre o cano e o lado de menor medida do terreno? "
            "A) 0,4 B) 0,5 C) 0,6 D) 0,7 E) 0,8. "
            "Now, please generate one three new math questions similar to this one, "
            "focusing on geometry and trigonometry, with answer choices in a multiple-choice format."
        )}
    ],
    response_format=CompleteTest
)

my_test = completion.choices[0].message.parsed

questions = my_test.questions

for question in questions:
    print(question)
    print("######################################")
