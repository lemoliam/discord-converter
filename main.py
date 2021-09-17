import requests
import json

login_data = input('Enter login data: test@gmail.com password123\n')
array = login_data.split(' ')
mail = array[0]
password = array[1]


def login():
    payload = {
        'email': mail,
        'password': password,
        'undelete': 'false',
        'captcha_key': 'null'
    }
    r = requests.post('https://discordapp.com/api/v9/auth/login', json=payload)
    j = json.loads(r.content)
    print(j['token'] if 'token' in j else 'No token found')


login()
