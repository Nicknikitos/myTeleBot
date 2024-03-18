import telebot
import requests
import json

bot = telebot.TeleBot('6983489685:AAEnNlJwI9b9V_AxHiOwCNtuYksbI5u5CzI')
API = '0717dbb242127c68b9f0585cd5d63622'


@bot.message_handler(commands=['start', 'main'])
def start(message):
    bot.send_message(message.chat.id, f'Herzlich Willkomen!, {message.from_user.first_name}. Напиши название города, где узнать погоду.')


@bot.message_handler(content_types=['text'])
def get_weather(message):
    city = message.text.strip().lower()
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
    if res.status_code == 200:

        data = json.loads(res.text)
        temp = round(data['main']['temp'], 1)
        weather = data['weather'][0]['main']
        wind = data['wind']['speed']
        bot.reply_to(message, f"Сейчас погода: {temp} °C. Скорость ветра: {wind} м/с.")

        if weather == "Clear":
            image = "sun.jpeg"
        if weather == "Rain":
            image = "rain.jpeg"
        if weather == "Clouds":
            image = "oblacno.jpeg"
        if weather == "Snow":
            image = "snow.jpeg"

        file = open('./' + image, 'rb')
        bot.send_photo(message.chat.id, file)
    else:
        bot.reply_to(message, 'Город указан не верно')






bot.polling(none_stop=True)