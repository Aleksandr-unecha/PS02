import requests

# Отправляем GET-запрос к API GitHub с параметром поиска репозиториев по ключевому слову "html"
url = 'https://api.github.com/search/repositories'
params = {'q': 'html'}
response = requests.get(url, params=params)

# Выводим статус-код ответа
print('Статус-код ответа:', response.status_code)

# Выводим содержимое ответа в формате JSON
json_response = response.json()
print('Содержимое ответа в формате JSON:', json_response)