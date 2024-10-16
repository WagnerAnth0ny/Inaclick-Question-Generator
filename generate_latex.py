import json

def generate_latex(data):
    latex_output = r"\documentclass{article}" + "\n" + r"\usepackage{amsmath}" + "\n" + r"\begin{document}" + "\n\n"
    
    for i in range(len(data)):
        item = data[i]

        latex_output += f"\paragraph{{{"Questão " + str(i + 1) + ":"}}}\n"
        text = item['text']
        latex_output += f"{{{text}}}\n\n"

        latex_output += f"\\vspace{{\\baselineskip}}"

        latex_output += "Opções:\n\n"

        latex_output += f"\\vspace{{\\baselineskip}}"

        for option in item['options']:
            value = option['value']
            latex_output += f"\\textbf{{{option['label']}}}: {value} \n\n"

        latex_output += f"\\vspace{{\\baselineskip}}"

        correct_answer = item['correct_answer']
        latex_output += f"\\textbf{{Resposta Correta}}: {correct_answer}\n\n"
        if 'tip' in item:
            latex_output += f"\\vspace{{\\baselineskip}}"

            tip = item['tip']
            latex_output += f"\\textbf{{Dica}}: {tip}\n\n"
    
    latex_output += r"\end{document}"
    return latex_output

with open("questions.json", "r", encoding="utf-8") as f:
    data = json.load(f)

latex_output = generate_latex(data)

with open("questions.tex", "w", encoding="utf-8") as f:
    f.write(latex_output)

print(latex_output)