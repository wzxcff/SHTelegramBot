import telebot
import os
from dotenv import load_dotenv
from handlers import *

load_dotenv()

bot = telebot.TeleBot(os.getenv('TOKEN'))

functions_map = {
    "hello": hello_handler
}


@bot.message_handler(content_types=['text'])
def message_handler(message):
    try:
        bot.send_message(message.chat.id, functions_map[str(message.text).lower()](message))
    except KeyError:
        bot.send_message(message.chat.id, "No function mapped to this word(s).")
    except Exception as e:
        print(f"Error occurred:\n{e}\n------------------")


bot.polling(none_stop=True)
