import requests
username = input('Введите имя: ')
password = input('Введите пароль: ')

while True:
    text = input()
    response = requests.post('http://127.0.0.1:5000/send',
                             json={'username': username, 'password': password, 'text': text}
                           )
    if response.status_code == 200:
        print('Send')