import telebot
from telebot import types
import emoji


numpanel = telebot.types.InlineKeyboardMarkup()
numpanel.row(telebot.types.InlineKeyboardButton('*️⃣', callback_data='**'),
             telebot.types.InlineKeyboardButton('🔄', callback_data='clear'),
             telebot.types.InlineKeyboardButton('⏪', callback_data='erase'),
             telebot.types.InlineKeyboardButton('➗', callback_data='/'))
numpanel.row(telebot.types.InlineKeyboardButton('7️⃣', callback_data='7'),
             telebot.types.InlineKeyboardButton('8️⃣', callback_data='8'),
             telebot.types.InlineKeyboardButton('9️⃣', callback_data='9'),
             telebot.types.InlineKeyboardButton('✖️', callback_data='*'))
numpanel.row(telebot.types.InlineKeyboardButton('4️⃣', callback_data='4'),
             telebot.types.InlineKeyboardButton('5️⃣', callback_data='5'),
             telebot.types.InlineKeyboardButton('6️⃣', callback_data='6'),
             telebot.types.InlineKeyboardButton('➖', callback_data='-'))
numpanel.row(telebot.types.InlineKeyboardButton('1️⃣', callback_data='1'),
             telebot.types.InlineKeyboardButton('2️⃣', callback_data='2'),
             telebot.types.InlineKeyboardButton('3️⃣', callback_data='3'),
             telebot.types.InlineKeyboardButton('➕', callback_data='+'))
numpanel.row(telebot.types.InlineKeyboardButton('🔠', callback_data='j'),
             telebot.types.InlineKeyboardButton('0️⃣', callback_data='0'),
             telebot.types.InlineKeyboardButton('◾', callback_data='.'),
             telebot.types.InlineKeyboardButton('🟰', callback_data='='))


help_message = """Welcome to the PyCulator.
                  A simple calculator, counting rational and complex numbers. 
                  Push '🔠' to make a complex number, ️ '*️⃣' to exponentiate a number
                  and 🔄 to clean the board. The rest look simple enough 😉
               """
