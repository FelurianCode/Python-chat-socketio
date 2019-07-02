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
	cleanMessage = sanitizeMessage(message['message'])
	cleanUsername = sanitizeMessage(message['user'])
	print(cleanMessage)
	if message['message'] == '':
		send({'error': ['Empty message']}, broadcast = True)
	else:
		print("Message: " + str(message))
		send({'user': cleanUsername, 'message': cleanMessage}, broadcast = True) #Send message to all clients 




def sanitizeMessage(message):
	cleanMessage = message.replace('<', '&lt')
	cleanMessage = cleanMessage.replace('>', '&gt')
	cleanMessage = cleanMessage.replace('&', '&amp')
	return cleanMessage


if __name__ == '__main__':
	socketio.run(app)


























