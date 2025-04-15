import telebot
bot = telebot.TeleBot('')
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Hello! I am a bot that can help you with various tasks. Type /help to see what I can do!')
@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, 'Here are the commands you can use:\n/start - Start the bot\n/help - Get help\n/echo - Echo back your message')
@bot.message_handler(commands=['echo'])
def echo(message):
    bot.send_message(message.chat.id, 'Please send me a message to echo back.')
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    bot.send_message(message.chat.id, 'You said: ' + message.text)
    bot.polling(none_stop=True)
