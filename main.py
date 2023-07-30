"""estrutura backend da aplicação
Websoket: serve como ia de comunicação entre o backend e o frontend
jquery: serve para fazer requisições js

"""

from flask import render_template, app, Flask

app = Flask(__name__)

@app.route('/')

def home():
    """função que renderiza a página inicial"""
    return render_template('home.html')

app.run()
