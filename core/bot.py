import telebot
import os
from dotenv import load_dotenv

load_dotenv()

bot = telebot.TeleBot(os.getenv('TOKEN'))


@bot.message_handler(content_types=['text'])
def message_handler(message):
    bot.send_message(message.chat.id, message.text)


bot.polling(none_stop=True)
