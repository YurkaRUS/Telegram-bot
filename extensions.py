# Импортируем модули
import json
import requests
# Импортируем словарь с валютами, ключ обращения в API
from currency import value, headers, payload


# Создаем класс исключений
class MyConverterException(Exception):
    pass


# Создаем класс для проведения конвертации
class Converter:
    @staticmethod
    def get_price(quote, base, amount):  # Статический метод, принимает аргументы введенные пользователем
        if quote == base:  # Проверяем, чтобы названия валют не совпадали
            raise MyConverterException(f"Вы ввели одинаковое наименование валюты {base}.")

        try:
            quote = value[quote]  # Проверяем наличие введенной валюты в словаре
        except KeyError:
            raise MyConverterException(f'Не удалось обработать валюту {quote}.')

        try:
            base = value[base]  # Проверяем наличие введенной валюты в словаре
        except KeyError:
            raise MyConverterException(f'Не удалось обработать валюту {base}.')

        try:
            amount = float(amount)  # Проверяем чтобы было введено число
        except ValueError:
            raise MyConverterException(f'Не удалось обработать количество {amount}.')
# Введенные данные передаем в наш API с помощью HTTP-запроса, переводим данные в объект Python
        url = f"https://api.apilayer.com/exchangerates_data/convert?to={quote}&from={base}&amount={amount}"
        response = requests.get(url, headers=headers, data=payload)
        total = json.loads(response.content)
# Возвращаем полученный результат по ключу
        return total['result']
