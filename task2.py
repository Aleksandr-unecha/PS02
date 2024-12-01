import requests

# Указываем базовый URL API
url = 'https://jsonplaceholder.typicode.com/posts'

# Указываем параметры запроса
params = {'userId': 1}

# Отправляем GET-запрос с указанными параметрами
response = requests.get(url, params=params)

# Проверяем, успешен ли запрос
if response.status_code == 200:
    # Парсим содержимое ответа в формате JSON
    posts = response.json()

    # Распечатываем полученные записи
    for post in posts:
        print(post)
else:
    print(f'Ошибка: статус-код {response.status_code}')