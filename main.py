from question_generator import generate_ten_questions, save_questions_to_json
from openai import OpenAI


client = OpenAI()

questions = []

questions.append('''
(VSD-2019) Sabendo que, em um
triângulo retângulo, x é um ângulo
agudo e que cos x = 4
5 . Os valores de
sen x e tg x são, respectivamente, iguais a:
A) 1/5 e 1/4
B) 1/4 e 1/5
C) 2/5 e 3/4
D) 3/5 e 1/4
E) 3/5 e 3/4
''')

questions.append('''
(VSD-2019) Em um triângulo ABC,
retângulo em Â, tem-se AC = 15 cm e
3
sen B̂ = 7 . Determine a hipotenusa BC
do triângulo.
A) 35 cm
B) 32 cm
C) 30 cm
D) 27 cm
E) 25 cm
''')

questions.append('''
(UFAM) Se um cateto e a hipotenusa
de um triângulo retângulo medem 2a
e 4a, respectivamente, então a
tangente do ângulo oposto ao menor
lado é:
A) 2√3
B) √3/3
C) √3/6
D) √20/20
E) 3√3
''')

questions.append('''
(CFTMG-2017) Em um triângulo
retângulo, a tan-gente de um de seus
ângulos agudos é 2. Sabendo-se que a
hipotenusa desse triângulo é 5, o valor
do seno desse mesmo ângulo é
A) 4/5
B) √5/4
C) √5/5
D) 2√5/5
''')

questions.append('''
Para fazer a tubulação de água em um
terreno retangular de dimensões 32 m
e 24 m, um pedreiro optou por passar
um cano unindo dois vértices opostos do terreno.
Qual o valor do seno do ângulo formado entre o
cano e o lado de menor medida do terreno?
A) 0,4
B) 0,5
C) 0,6
D) 0,7
E) 0,8
''')

questions.append('''
(Vunesp-SP) Duas rodovias retilíneas,
A e B, cruzam-se formando um ângulo
de 45o. Um posto de gasolina se
encontra na rodovia A, a 4 km do cruzamento. Pelo
posto, passa uma rodovia retilínea C,
perpendicular a B. A distância do posto de gasolina
à rodovia B, indo através de C, em quilômetros, é:
A) √2/8
B) √2/4
C) √3/2
D) √2
E) 2√2
''')

new_questions = []

for question in questions:
    ten_new_questions = generate_ten_questions(question=question, client=client)

    new_questions += ten_new_questions

save_questions_to_json(new_questions, 'questions.json')
