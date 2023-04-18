import json
import os  
 
def register(login, paswrd):
    data = {'login': login, 'password': paswrd}
    if os.path.exists('reg.json'):
        with open('reg.json', 'r') as f:
            data = json.load(f)
            if login in data:
                print(f'Пользователь с логином {login} уже существует')
                return
    else:
        data = {}
    data[login] = paswrd
    with open('reg.json', 'w') as f:
        json.dump(data, f)
    print(f'Пользователь {login} успешно зарегистрирован')
register('user5', 'password0')  
import json
import os

def login_user(login: str, paswrd: str):
    if os.path.exists('reg.json'):
        with open('reg.json', 'r') as f:
            data = json.load(f)
            if login in data and data[login] == paswrd:
                print(f'Пользователь {login} успешно вошел в систему')
                return
    print(f'Неверный логин или пароль')
login_user('user5', 'password1')

