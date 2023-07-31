"""estrutura backend da aplicação
Websoket: serve como ia de comunicação entre o backend e o frontend
jquery: serve para fazer requisições js

site : cdnjs.com

pip install python-socketio flask-socketio simple-websocket

"""
from flask import render_template, Flask
from flask_socketio import SocketIO, send

app = Flask(__name__, template_folder='templates')



socketio = SocketIO(app, cors_allowed_origins="*")

# Funcionalidade de enviar mensagens
@socketio.on('message')
def gerenciar_mensagem(mensagem):
    """Função que gerencia as mensagens enviadas pelo usuário"""
    send(mensagem, broadcast=True)

@app.route('/')
def home():
    """Função que renderiza a página inicial"""
    return render_template('home.html')

if __name__ == '__main__':
    socketio.run(app, host='localhost', debug=True)
