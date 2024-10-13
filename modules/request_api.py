import requests
#импортируем функцию которая читает json
from .read_json import read_json
#импортируем json
import json
#создаем переменную в которой будут данные из json'а 
data_api = read_json(name_file= 'config_api.json')
#делаем переменную в которой API. API = способ подключения к серверу за данными
API_KEY = data_api['api_key']
#имя города которому для которого мы будем делатьпрогноз погоды
CITY_NAME = data_api['city_name']
#ссылка на сайт с которого мы будем брать информацию с помощью нашего API
URL = f"https://api.openweathermap.org/data/2.5/weather?q={CITY_NAME}&appid={API_KEY}"
#получаем данные по URL
response = requests.get(URL)
#проверяем получили ли мы данные
if response.status_code == 200:
    #дешифруем код с байт кода в словарь и записуем в переменную
    data_dict = json.loads(response.content)
    #выводим на экран и превращаем полученные дынные в str и делаем отступ в 4 пробела
    print(json.dumps(data_dict, indent= 4))