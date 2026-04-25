from flask import Flask, render_template, request

app = Flask(__name__)


conteudo_visor = ""

@app.route('/', methods=['GET', 'POST'])
def index():
    global conteudo_visor
    
    if request.method == 'POST':
        botao_apertado = request.form.get('botao')
        
      
        if botao_apertado == "=":
            try:
                conteudo_visor = str(eval(conteudo_visor))
            except:
                conteudo_visor = "Erro"
        
       
        elif botao_apertado == "C":
            conteudo_visor = ""
            
       
        else:
            conteudo_visor += botao_apertado

    return render_template('1.html', valor=conteudo_visor)
if __name__ == '__main__':
    app.run(debug=True)
            
