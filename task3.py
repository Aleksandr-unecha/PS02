import requests

# Указываем URL API
url = 'https://jsonplaceholder.typicode.com/posts'

# Создаем словарь с данными для отправки
data = {
    'title': 'foo',
    'body': 'bar',
    'userId': 1
}

# Отправляем POST-запрос с данными
response = requests.post(url, json=data)

# Распечатываем статус-код ответа
print('Статус-код ответа:', response.status_code)

# Распечатываем содержимое ответа
print('Содержимое ответа:', response.json())