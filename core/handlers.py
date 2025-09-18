from db import *
import datetime


def hello_handler(message):
    return f"Hello, my friend {message.from_user.first_name} {message.from_user.last_name}!"


def start_handler(message):
    user = get_user_by_user_id(message.from_user.id)
    if not user:
        create_user(message.from_user.id, message.from_user.username, message.from_user.first_name, message.from_user.last_name)
        return "Привіт! Бачу що ти новенький, але тут все інтуітивно зрозуміло! -> /help"
    return f"Привіт, {message.from_user.first_name}! Ми вже знайомі :)"


def schedule_today_handler(message):
    today = datetime.date.today().weekday()
    return get_schedule_by_day(str(today))


def admin_keyboard_handler(message):
    if is_user_admin(message.from_user.id):
        return "Адмін панель надано"
    return "Ви не є адміністратором"


def get_admin_handler(message):
    return add_admin(message.from_user.id)


def to_main_menu_handler(message):
    return "Повертаю Вас на головне меню!"


def edit_schedule_handler(message):
    return f"{message.from_user.first_name}, оберіть день для редагування!"


def to_admin_panel_handler(message):
    return "Повертаю Вас до адмін панелі!"
