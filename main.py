import telebot


TOKEN = '6566637505:AAFDeUw9ssdse5vKBwzgpKQSyf48X8q8O3A'

bot = telebot.TeleBot(TOKEN)

keys ={
    'Рубли': 'RUB',
    'Доллары': 'USD',
    'Юани': 'CNY'
}


@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    text = 'Чтобы начать работу введите команду боту в следующем формате:\n<имя валюты> \
<в какую валюту перевести> \
<количество переводимой валюты>\nУвидеть список всех доступных валют: /values'
    bot.reply_to(message, text)

@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for key in keys.keys():
        text = '\n'.join((text, key, ))
    bot.reply_to(message, text)

bot.polling()