'''
    Modulo de testes usando o Flask no Github
'''

from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    '''
        Essa função é a função basica a ser chamada quando o caminho raiz for invocado
    '''
    return 'Hello, World!'
