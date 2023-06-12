import telebot
from telebot import types

bot = telebot.TeleBot("") 

@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, 'Мене звуть Кіра Йошикаге 🙎🏻‍♂️\n\nМені 33 роки.' +
                        'Мій будинок знаходиться в північно-східній частині Моріо, в районі маєтку 🏡\n\n' + 
                        'Працюю в офісі мережі магазинів Kame Yu і додому повертаюся, ' +
                        'найпізніше, о восьмій вечора. Не курю, випиваю зрідка. Лягаю спати об 11 вечора 🫧')
@bot.message_handler(commands=['contact'])
def handle_contact(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton(text='GitHub🍎', url="https://github.com/ChessRubixTower56 "))
    bot.send_message(message.chat.id, 'My social media :', reply_markup=markup)
    markup.add(types.InlineKeyboardButton(text='Telegramm🍐', url="https://t.me/bablic74 "))
    bot.send_message(message.chat.id, 'My social media :', reply_markup=markup)
bot.polling()
