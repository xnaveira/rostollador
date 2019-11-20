import sys
import time
import telepot
from telepot.loop import MessageLoop
from pprint import pprint

def handle(msg):
    pprint(msg)
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)

    if content_type == 'text':
        if 'Hola'.lower() in msg['text'].lower():
            try:
                bot.sendMessage(chat_id, f"Hola {msg['chat']['first_name']}")
            except KeyError:
                bot.sendMessage(chat_id, f"Hola {msg['from']['first_name']}")
        elif 'Bon dia'.lower() in msg['text'].lower():
            try:
                bot.sendMessage(chat_id, f"Bon dia {msg['chat']['first_name']}")
            except KeyError:
                bot.sendMessage(chat_id, f"Bon dia {msg['from']['first_name']}")
        elif ('cabro'.lower() or 'marica'.lower() or 'tonto'.lower() or 'puta'.lower() or 'merda'.lower()) in msg['text'].lower() and 'rostollador'.lower() in msg['text'].lower():
            bot.sendMessage(chat_id, '🖕')
        #bot.sendMessage(chat_id, msg['text'])

TOKEN = sys.argv[1]  # get token from command-line

bot = telepot.Bot(TOKEN)
MessageLoop(bot, handle).run_as_thread()
print ('Listening ...')

# Keep the program running.
while 1:
    time.sleep(10)
