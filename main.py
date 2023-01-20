# Импортируем модуль
import telebot
# Импортируем из наших файлов необходимые данные
from currency import value, TOKEN
from extensions import MyConverterException, Converter

# Создаем объект bot
bot = telebot.TeleBot(TOKEN)


# Обработчик, реагирует на указанные команды и выводит необходимую нам информация (с повторением нашей команды)
@bot.message_handler(commands=['start', 'help'])
def help_(message: telebot.types.Message):
    text = 'Чтобы начать работу введите комманду боту в следующем формате:\nимя валюты в какую переводим  ' \
    '\nимя валюты, из какой переводим  ' \
    '\nколичество переводимой валюты \nчерез пробел\n\nУвидеть список всех доступных валют: /values'
    bot.reply_to(message, text)


# Тоже обработчик, который при команде values, выдаст весь список валют,
# взятых из используемого API и преобразованных в словарь в файле currency.
@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for k, v in value.items():
        text = '\n'.join((text, f'{v} : {k}',))
    bot.reply_to(message, text)


# Обработчик, принимающий данные валют от пользователя (кроме этого проверит количество введенных параметров),
# и через метод get_price произведет обращение к API и выдаст результат
@bot.message_handler(content_types=['text'])
def convert(message: telebot.types.Message):
    val = message.text.split(' ')  # разделяем введенную строку на список
    try:
        if len(val) != 3:  # проверяем количество параметров
            raise MyConverterException("Количество параметров задано неверно.")

        quote, base, amount = val  # разделяем наш список по параметрам

        conv = Converter.get_price(quote, base, amount)  # передаем данные в метод
        conv = round(conv, 2)  # округляем полученный результат до двух знаков
        text = f"Цена {amount} {base} в {quote} = {conv}"  # подготавливаем ответ в удобном виде
        bot.reply_to(message, text)  # выводим результат
    except MyConverterException as e:
        bot.reply_to(message, f"Ошибка ввода: {e}")
    except Exception as e:
        bot.reply_to(message, f"Ошибка: {e}")


# Запускаем бота с возможностью продолжения работы, даже при наличии ошибок
bot.polling(none_stop=True)
