from telebot import types


def reply_markup_builder(labels: iter, row_size: int = 2, resize: bool = True) -> types.ReplyKeyboardMarkup:
    buttons = []
    temp_markup = types.ReplyKeyboardMarkup(row_width=row_size, resize_keyboard=resize)
    for label in labels:
        buttons.append(types.KeyboardButton(label))
    temp_markup.add(*buttons)
    return temp_markup


main_keyboard_labels = ["Розклад", "Розклад на тиждень", "Відмітка", "Дедлайни", "Scoreboard", "Адмін"]
main_keyboard_built = reply_markup_builder(main_keyboard_labels, 2)

admin_keyboard_labels = ["Редагувати розклад", "Подивитись відмітки", "Керування дедлайнами", "На головну"]
admin_keyboard_built = reply_markup_builder(admin_keyboard_labels, 2)

edit_schedule_labels = ["Понеділок", "Вівторок", "Четвер", "Середа", "Пʼятниця", "Субота", "До адмін панелі"]
edit_schedule_built = reply_markup_builder(edit_schedule_labels, 2)