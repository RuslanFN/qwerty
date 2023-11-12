import telebot
from telebot import types
bot=telebot.TeleBot("6578892721:AAH2J1HsqO6LKD6xBYaHT9MBHbJY3i-jAAw")
joinedFile = open("id.txt", "r")
joinedUsers = set()
for line in joinedFile:
    joinedUsers.add(line.strip())
joinedFile.close()
 
@bot.message_handler(commands=["start"])
def start(message):
    if not str(message.chat.id) in joinedUsers:
        joinedFile = open("id.txt", "a")
        joinedFile.write(str(message.chat.id) + "\n")
        joinedUsers.add(message.chat.id)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Актировка")
    btn2 = types.KeyboardButton("Рассылка")
    btn3 = types.KeyboardButton("ЦОП")
    if str(message.chat.id)!="998618198":
        btn4 = types.KeyboardButton("Отзывы")
        markup.add(btn4)
    markup.add(btn1)
    markup.add(btn3)
    if str(message.chat.id)=="998618198":
        markup.add(btn2)
    mess=f"Привет,{message.from_user.first_name}"
    bot.send_message(message.chat.id,mess,reply_markup = markup,parse_mode="html")


@bot.message_handler(commands=["special"])
def propagetion(message):
    for user in joinedUsers:
        if user=="998618198":
                continue
        bot.send_message(user,message.text[message.text.find(" ")])     

@bot.message_handler(content_types=['text'])
def victim(message):
    if message.text=="Рассылка" and str(message.chat.id)=="998618198":    
        for user in joinedUsers:
            photo=open("95.png","rb")
            photo1=open("74.jpg","rb")
            if user=="998618198":
                continue
            bot.send_photo(user,photo)
            bot.send_photo(user,photo1)
    elif message.text=="Актировка":
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("Информация по актировкам", url='https://admhmansy.ru/')
        markup.add(button1)
        bot.send_message(message.chat.id," Нажми на кнопку и узнай про актировку".format(message.from_user),reply_markup=markup)  
    elif message.text=="ЦОП":
        markup = types.InlineKeyboardMarkup()
        button2 = types.InlineKeyboardButton("Электронный журнал", url='https://cop.admhmao.ru/elk')
        markup.add(button2)
        bot.send_message(message.chat.id," Нажми на кнопку и переходит в электронный журнал".format(message.from_user),reply_markup=markup)      
    elif message.text=="Отзывы":
        if str(message.chat.id)!="998618198":
            markup = types.InlineKeyboardMarkup()
            button5 = types.InlineKeyboardButton("Написать отзыв", url='https://t.me/airwar31')
            markup.add(button5)
            bot.send_message(message.chat.id," Оставить отзыв о нашем проекте ".format(message.from_user),reply_markup=markup)                
    else:
        bot.send_message(message.chat.id,"Извините, я вас не понимаю. Воспользуйтесь,пожалуйста,кнопками")
        
    
bot.polling(non_stop=True)      