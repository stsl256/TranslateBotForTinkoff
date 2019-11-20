# -*- coding: utf-8 -*-
import telebot
import requests

TOKEN = "710024822:AAEVOiQHizxhCd3O59p2zcbYQsgZwdznfbQ"
MAIN_URL = "https://api.telegram.org/bot710024822:AAEVOiQHizxhCd3O59p2zcbYQsgZwdznfbQ"

URL = "https://translate.yandex.net/api/v1.5/tr.json/translate" 
KEY = "trnsl.1.1.20191120T141955Z.2f35ae3842eb1edc.760f22c9223d9498edaff79ea188dd984579a55d" 
bot = telebot.TeleBot(TOKEN)
#r = requests.get("https://api.telegram.org/bot710024822:AAEVOiQHizxhCd3O59p2zcbYQsgZwdznfbQ/getUpdates")
#print(r.json())
def translate_me(mytext):

    params = {
        "key": KEY,     
        "text": mytext,
        "lang": 'ru-en' 
    }
    response = requests.get(URL ,params=params)
    return response.json()

@bot.message_handler(content_types=["text"])
def echo_digits(message): 
	print(message.text)
	bot.reply_to(message,(''.join(translate_me(message.text)["text"])))


if __name__ == '__main__':
	bot.polling(none_stop=True)
	