import telebot
#from telebot import types
bot = telebot.TeleBot('1881912422:AAEfBCKJnLB2U6UtR9oyHe84zAu9NqLSObw') # //регистрация токена



@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "/start":
        # Если написали «/start»
        bot.send_message(message.from_user.id, "Тестовое приветствие")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")




bot.polling(none_stop=True, interval=0)