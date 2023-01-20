# Импортируем модули
import json
import requests
# Токен для бота
TOKEN = '5701407828:AAH9v3GJwFHyi1clOZZIUq9Kb1T73aKETuk'
# Создаем пустой словарь для списка валют
value = {}
payload = {}
# Ключ для нашего API
headers = {
    "apikey": "9Vm3YeoNH9F24R004Qch9Gdh73zyPsgg"
}
url = "https://api.apilayer.com/exchangerates_data/symbols"
# Отправляем HTTP-запрос
response = requests.get(url, headers=headers, data=payload)
# Десериализация JSON в объект Python (парсинг)
text = json.loads(response.text)
# Добавляем данные в наш словарь
value.update(text['symbols'])
# Меняем местами ключи и значения для более наглядного вывода данных в боте
value = dict(zip(value.values(), value.keys()))
