import telebot
import os
from dotenv import load_dotenv
from handlers import *
from time import time

load_dotenv()

bot = telebot.TeleBot(os.getenv('TOKEN'))

last_message_time = {}
MESSAGE_RATE_SECONDS = 1

functions_map = {
    "hello": hello_handler,
    "/start": start_handler,
}


@bot.message_handler(content_types=['text'])
def message_handler(message):
    if is_spamming(message.from_user.id):
        bot.send_message(message.chat.id, "You're sending too much requests!")
        return
    try:
        bot.send_message(message.chat.id, functions_map[str(message.text).lower()](message), parse_mode="HTML")
    except KeyError:
        bot.send_message(message.chat.id, "No function mapped to this word(s).")
    except Exception as e:
        print(f"Error occurred:\n{e}\n------------------")


def is_spamming(user_id: int) -> bool:
    current_time = time()
    last_time = last_message_time.get(user_id, 0)

    if current_time - last_time < MESSAGE_RATE_SECONDS:
        return True

    last_message_time[user_id] = current_time
    return False


bot.polling(none_stop=True)
