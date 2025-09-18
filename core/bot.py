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
    "розклад": schedule_today_handler,
    "адмін": admin_keyboard_handler,
    "стати адміном": get_admin_handler,
    "на головну": to_main_menu_handler,
    "редагувати": what_to_edit_handler,
    "до адмін панелі": to_admin_panel_handler,
    "редагувати дисципліну": edit_lesson_handler,
    "редагувати розклад": edit_schedule_handler,
}


@bot.message_handler(content_types=['text'])
def message_handler(message):
    if is_spamming(message.from_user.id):
        bot.send_message(message.chat.id, "You're sending too much requests!")
        return
    try:
        call = functions_map[str(message.text).lower()](message)
        bot.send_message(message.chat.id, call[0], parse_mode="HTML", reply_markup=call[1])
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
