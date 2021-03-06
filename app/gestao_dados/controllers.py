from flask import Flask, request, render_template,Blueprint
mod_gestao_dados = Blueprint('gestao_dados', __name__)

@mod_gestao_dados.route('/')
def index():
    return render_template('index.html')

@mod_gestao_dados.route('/formulario', methods=['POST', 'GET'])
def formulario():

    ''' Verificando se o dado foi enviado via POST '''

    if request.method == 'POST':

        mensagem = 'Dados Enviado via Post'
        dados = request.form.to_dict()
        nome = request.form['nome']

        if nome == 'luke':
            mensagem = mensagem + 'Star War é Legal!!'
    else:

        mensagem = 'Dados Enviado via Get'
        dados = request.args.to_dict()
        nome = request.args['nome']

        if nome == 'luke':
            mensagem = mensagem + 'Star War é Legal!!'

    return render_template('resultado.html',mensagem = mensagem, dados = dados)
