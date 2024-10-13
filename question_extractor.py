from models import *
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


def question_extractor(question_text: str):
    completion = client.beta.chat.completions.parse(
        model="gpt-4o-2024-08-06",
        messages=[
            {"role": "system", "content": "Extract the question information, saving every bit of information available in the question"},
            {"role": "user", "content": "Question: " + question},
        ],
        response_format=MultipleChoiceQuestion,
    )

    event = completion.choices[0].message.parsed

    return event
