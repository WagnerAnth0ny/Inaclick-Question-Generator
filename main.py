from models import *
from question_extractor import question_extractor
from openai import OpenAI

client = OpenAI()

question = '''
 Analisando as vendas de uma empresa, o gerente concluiu que o montante diário arrecadado, em milhar de real, poderia ser calculado pela expressão V(x) = x2/4 - 10x + 105,  em que os valores de x representam os dias do mês, variando de 1 a 30.
Um dos fatores para avaliar o desempenho mensal da empresa é verificar qual é o menor montante diário V0 arrecadado ao longo do mês e classificar o desempenho conforme as categorias apresentadas a seguir, em que as quantidades estão expressas em milhar de real.

• Ótimo: V0 ≥ 24 • Bom: 20 ≤ V0 < 24 • Normal: 10 ≤ V0 < 20 • Ruim: 4 ≤ V0 < 10 • Péssimo: V0 < 4

No caso analisado, qual seria a classificação do desempenho da empresa?
Alternativas
A
Ótimo.
B
Bom.
C
Normal.
D
Ruim.
E
Péssimo.
'''

def generate_questions_from_instance(question_instance):
    prompt_text = (
        f"Here is a sample math question: {question_instance.prompt} "
        f"Options: {', '.join([f'{opt.label}) {opt.value}' for opt in question_instance.options])}. "
        f"Now, based on this example, please generate three new math questions "
        f"Each question should include multiple choice answer options."
    )

    completion = client.beta.chat.completions.parse(
        model="gpt-4o-2024-08-06",
        messages=[
            {"role": "system", "content": "You are an expert at generating educational exam questions."},
            {"role": "user", "content": prompt_text}
        ],
        response_format=CompleteTest
    )

    return completion

question_instance = question_extractor(question_text=question, client=client)

new_questions = generate_questions_from_instance(question_instance=question_instance)

for q in new_questions:
    print(q)
    print("#" * 10)
