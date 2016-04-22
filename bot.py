import telepot

bot_key = ''
bot = telepot.Bot(bot_key)
response = bot.getUpdates()
your_id = 0


def sendMessage(z):
    try:
        bot.sendMessage(your_id, z)
    except:
        print('Error sending message', z)