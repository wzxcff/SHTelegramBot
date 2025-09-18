from db import *
import datetime
from keyboards import *

not_admin_text = "Ви не є адміністратором!"


def hello_handler(message):
    return f"Hello, my friend {message.from_user.first_name} {message.from_user.last_name}!"


def start_handler(message):
    user = get_user_by_user_id(message.from_user.id)
    if not user:
        create_user(message.from_user.id, message.from_user.username, message.from_user.first_name, message.from_user.last_name)
        return "Привіт! Бачу що ти новенький, але тут все інтуітивно зрозуміло! -> /help", main_keyboard_built
    return f"Привіт, {message.from_user.first_name}! Ми вже знайомі :)"


def schedule_today_handler(message):
    today = datetime.date.today().weekday()
    return get_schedule_by_day(str(today))


def admin_keyboard_handler(message):
    if is_user_admin(message.from_user.id):
        return "Адмін панель надано", admin_keyboard_built
    return not_admin_text, None


def get_admin_handler(message):
    return add_admin(message.from_user.id), None


def to_main_menu_handler(message):
    return "Повертаю Вас на головне меню!", main_keyboard_built


def what_to_edit_handler(message):
    return f"{message.from_user.first_name}, що саме хочете редагувати?", edit_schedule_detailed_built


def edit_lesson_handler(message):
    if is_user_admin(message.from_user.id):
        return f"Наразі функція недоступна", None
    return not_admin_text, None


def edit_schedule_handler(message):
    if is_user_admin(message.from_user.id):
        return f"Наразі функція недоступна", None
    return not_admin_text, None


def to_admin_panel_handler(message):
    if is_user_admin(message.from_user.id):
        return "Повертаю Вас до адмін панелі!", admin_keyboard_built
    return not_admin_text, None
