from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')   

@socketio.on('message') #if server listens to message event
def handleMessage(message):
    print("Message: " + str(message))  
    send({'user': message['user'], 'message': message['message']}, broadcast = True) #Send message to all clients 



if __name__ == '__main__':
	socketio.run(app)


























