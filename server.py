from datetime import datetime
from flask import Flask, request
import time

app = Flask(__name__)
messages = []
password_storage = {}

@app.route('/')
def messenger():
    return {
        'status': True,
        'datetime': datetime.now(),
        'messages_count' : len(messages),
        'user_count': len(password_storage)
    }


@app.route('/send', methods=['POST'])
def send():
    username = request.json['username']
    password = request.json['password']
    text = request.json['text']

    # first attempt for password is always valid
    if username not in password_storage:
        password_storage[username] = password

    # validate data
    if not isinstance(username, str) or len(username) == 0:
        return {'ok': False}
    if not isinstance(text, str) or len(text) == 0:
        return {'ok': False}
    if password_storage[username] != password:
        return {'ok': False}

    messages.append({'username': username, 'time': time.time(), 'text': text})
    return {'ok': True}


@app.route('/messages')
def messages_method():
    after = float(request.args['after'])
    filtered_messages = [message for message in messages if message['time'] > after]
    return {'messages': filtered_messages}


if __name__ == '__main__':
    app.run()

