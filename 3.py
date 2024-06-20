import requests

url = 'https://wttr.in'

# Обновленный словарь параметров запроса (удален параметр 'lang')
weather_parameters = {
    '0': '',
    'T': '',
    'M': '',
}

# Словарь с заголовками запроса
request_headers = {
    'Accept-Language': 'ru'
}

# Выполнение HTTP-запроса с передачей параметров и заголовков
response = requests.get(url, params=weather_parameters, headers=request_headers)

# Печать текста HTTP-ответа
print(response.text)