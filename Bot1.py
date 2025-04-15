import telebot
import webbrowser
from telebot import types
bot = telebot.TeleBot('8144284032:AAH6SIkPcnm3v5ZkU28-3XEFOe_d52RKjcI')
@bot.message_handler(commands=['site', 'website'])
def site(message):
    webbrowser.open('https://www.youtube.com')
bot = telebot.TeleBot('')
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = (types.KeyboardButton('/help', ))
    btn2 = (types.KeyboardButton('/echo', ))
    markup.row(btn1, btn2)
    bot.send_message(message.chat.id,
                     f'Hello, {message.from_user.first_name}!\nI am a bot that can help you with various tasks.\nType /help to see what I can do.',
                     reply_markup=markup)
@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, 'Here are the commands you can use:\n/start - Start the bot\n/help - Get help\n/echo - Echo back your message')
@bot.message_handler(commands=['echo'])
def echo(message):
    bot.send_message(message.chat.id, 'Please send me a message to echo back.')
    bot.reply_to(message, 'I received your message!')
@bot.message_handler(content_types=['photo'])
def handle_image(message):
    markup = types.InlineKeyboardMarkup()
    btn1=(types.InlineKeyboardButton('Open website', url='https://www.google.com'))
    btn2=(types.InlineKeyboardButton('delete photo', callback_data='delete photo'))
    btn3=(types.InlineKeyboardButton('edit text',callback_data='edit text'))
    markup.row(btn1)
    markup.row( btn2, btn3)

    bot.reply_to(message, 'I received an image!', reply_markup=markup)
@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 'delete photo':
        bot.delete_message(callback.message.chat.id, callback.message.message_id-1)
    elif callback.data == 'edit text':
        bot.edit_message_text('edited text', callback.message.chat.id, callback.message.message_id)
@bot.message_handler()
def handle_message(message):
    bot.reply_to(message, 'There is no such command')

bot.polling(none_stop=True)