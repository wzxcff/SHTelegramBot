from db import *


def hello_handler(message):
    return f"Hello, my friend {message.from_user.first_name} {message.from_user.last_name}!"


def start_handler(message):
    user = get_user_by_user_id(message.from_user.id)
    if not user:
        create_user(message.from_user.id, message.from_user.username, message.from_user.first_name, message.from_user.last_name)
        return "Created new user!"
    return "User already created!"
