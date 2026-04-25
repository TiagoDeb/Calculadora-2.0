from flask import Flask, render_template, request

app = Flask(__name__)

# Variável para guardar os números digitados
conteudo_visor = ""

@app.route('/', methods=['GET', 'POST'])
def index():
    global conteudo_visor

    if request.method == 'POST':
        botao_apertado = request.form.get('botao')

        # 1. Se apertar o igual, calcula
        if botao_apertado == "=":
            try:
                conteudo_visor = str(eval(conteudo_visor))
            except:
                conteudo_visor = "Erro"

        # 2. Se apertar o C, limpa tudo
        elif botao_apertado == "C":
            conteudo_visor = ""

        # 3. Se for número ou sinal, vai grudando no visor
        else:
            conteudo_visor += botao_apertado

    return render_template('1.html', valor=conteudo_visor)