import logging
from datetime import datetime
from random import randint, choice

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, InlineQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, InlineQueryResultArticle, ParseMode, InputTextMessageContent
import os

from youtube_api import YouTubeDataAPI

admin = os.getenv('ADMIN_USER')
admin_filter = Filters.chat(username=admin)
youtube_api_key = os.getenv('YOUTUBE_API_KEY')
yt = YouTubeDataAPI(youtube_api_key)
nyofla_channel=os.getenv('NYOFLA_YT_CHANNEL')
last_checked = datetime.fromtimestamp(0)
channel_rostollador_i_jo = os.getenv('ROSTOLLADOR_I_JO_CHANNEL')
channel_rostolladors_hab = os.getenv('ROSTOLLADORS_CHANNEL')

updater = Updater(token=os.getenv('TELEGRAM_TOKEN'), use_context=True)
dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)

messages_sent = 0

def version(update, context):
    version = '2.2.0'
    global messages_sent
    messages_sent = messages_sent + 1
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text='La meva versió és {}'.format(version),
                             parse_mode='MarkDown')

version_handler = CommandHandler('versio', version, filters=admin_filter)
dispatcher.add_handler(version_handler)

def total_messages(update, context):
    global messages_sent
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text='He enviat {} missatges.'.format(messages_sent),
                             parse_mode='MarkDown')

total_messages_handler = CommandHandler('missatges', total_messages, filters=admin_filter)
dispatcher.add_handler(total_messages_handler)

def say(update, context):
    global messages_sent
    messages_sent = messages_sent + 1
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text='{}'.format(' '.join(context.args)),
                             parse_mode='MarkDown')

say_handler = CommandHandler('digues', say, filters=admin_filter)
dispatcher.add_handler(say_handler)

def latest_nyofla_youtube(unused):
    global messages_sent
    global last_checked
    messages_sent = messages_sent + 1
    ylist = yt.search(channel_id=nyofla_channel, search_type="video", max_results=1, order_by="date")
    if len(ylist) > 0:
        ylatest = ylist[0]
        if ylatest['video_publish_date'] > last_checked:
            last_checked = ylatest['video_publish_date']
            updater.bot.send_message(chat_id=channel_rostollador_i_jo,
                                     text='{} presenta: {}\n{}'.format(ylatest['channel_title'], ylatest['video_title'], ylatest['video_thumbnail']),
                                     parse_mode='Html')


# latest_nyofla_handler = CommandHandler('ultim', latest_nyofla_youtube, filters=admin_filter)
# dispatcher.add_handler(latest_nyofla_handler)




def hello(update, context):
    global messages_sent
    greetings = ['Hola {}', 'Què tal {}?', 'Com vas {}?', 'Què dius {}?', 'Com ho portes {}?']
    if percent(60):
        messages_sent = messages_sent + 1
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=choice(greetings).format(update.effective_user.first_name),
            parse_mode='MarkDown')


hello_handler = MessageHandler(Filters.regex('.*[H|h]ola.*'), hello)
dispatcher.add_handler(hello_handler)

def good_morning(update, context):
    global messages_sent
    greetings = ['Bon dia {}', 'Bon dia tinguis {}']
    if percent(40):
        messages_sent = messages_sent + 1
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=choice(greetings).format(update.effective_user.first_name),
            parse_mode='MarkDown')


good_morning_handler = MessageHandler(Filters.regex('.*[B|b]on\s+dia.*'), good_morning)
dispatcher.add_handler(good_morning_handler)

dispatcher.job_queue.run_repeating(latest_nyofla_youtube, 1800, 0, 'NyoflaYT')


#Randomly throws a 100 dice and returns if result less than number
def percent(number):
    r = randint(0, 100)
    if r <= number:
        return True
    else:
        return False

updater.start_polling()

