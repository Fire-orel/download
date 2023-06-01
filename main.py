import wget
from telebot import TeleBot
import os.path
import datetime


api_token="6232828877:AAEk1NvcISCrLcVdWWxtllSNGw_UdFdmHrQ"
bot=TeleBot(api_token)

@bot.message_handler(commands=["help","start"])
def send_welcome(message):
    bot.send_message(message.chat.id,"Здравствуйте я бот для скачивания презентаций по ссылке")
@bot.message_handler(commands=["history"])
def send_history(message):
    if message.chat.id == 380512347:
        f=open("history.txt","r",encoding="utf8")
        data=f.read()
        bot.send_message(message.chat.id,data)
        f.close()
@bot.message_handler(content_types="text")
def send_prezintacia(message):
    if message.text.split('https://', maxsplit = 1)[0] == '' or message.text.split('http://', maxsplit = 1)[0] == '':
        try:
            bot.send_message(message.chat.id,"Файл скачиваеться ожидайте...")
            url = message.text
            wget.download(url, f'{message.from_user.id}.pptx')
            f=open(f'{message.from_user.id}.pptx',"rb")
            bot.send_document(message.chat.id,f)
            f.close()
            os.remove(f'{message.from_user.id}.pptx')
            with open('history.txt', 'a') as h:
                h.write(f'{datetime.datetime.now()}, {message.chat.username} \n')
            h.close()
        except:
            bot.send_message(message.chat.id,"Непредвиденная ошибка попробуйте ещё раз")
    else:
        bot.send_message(message.chat.id,"Формат ссылки не правильный")



bot.polling(none_stop=True)



