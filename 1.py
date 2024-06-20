import requests

# URL сервиса погоды
url = 'http://wttr.in'

# Параметры запроса
weather_parameters = {
    '0': '',
    'T': ''
}

# Выполнение HTTP-запроса с передачей параметров
response = requests.get(url, params=weather_parameters)

# Печать текста HTTP-ответа
print(response.text)