import requests

url = 'https://wttr.in'  # не изменяйте значение URL

# Обновленный словарь параметров запроса
weather_parameters = {
    '0': '',
    'T': '',
    'M': '',
    'lang': 'ru'
}

# Выполнение HTTP-запроса с передачей параметров
response = requests.get(url, params=weather_parameters)

# Печать текста HTTP-ответа
print(response.text)