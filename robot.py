import telebot

import keyboard as kb


API_TOKEN = ''
robot = telebot.TeleBot(API_TOKEN)
current_number = previous_number = ''


@robot.message_handler(commands=['start'])
def start(message):
    global current_number
    if current_number == '':
        robot.send_message(message.from_user.id, '0', reply_markup=kb.numpanel)
    else:
        robot.send_message(message.from_user.id, current_number, reply_markup=kb.numpanel)


@robot.message_handler(commands=['help'])
def help(message):
    robot.send_message(message.chat.id, kb.help_message)


@robot.callback_query_handler(func=lambda call: True)
def calculate(query):
    global current_number, previous_number
    data = query.data

    match data:
        case 'clear':
            current_number = ''
        case 'erase':
            if current_number != '':
                current_number = current_number[:len(current_number) - 1]
        case '=':
            current_number = str(eval(current_number))
        case _:
            current_number += data

    if current_number != previous_number:
        if current_number == '':
            robot.edit_message_text(chat_id=query.message.chat.id,
                                  message_id=query.message.id,
                                  text='0', reply_markup=kb.numpanel)
        else:
            robot.edit_message_text(chat_id=query.message.chat.id,
                                  message_id=query.message.id,
                                  text=current_number, reply_markup=kb.numpanel)
        previous_number = current_number


robot.polling()
