import logging
from uuid import uuid4

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, InlineQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, InlineQueryResultArticle, ParseMode, InputTextMessageContent
from telnetlib import Telnet
from threading import Thread
import os
import re

from telegram.utils.helpers import escape_markdown

admin = os.getenv('ADMIN_USER')
admin_filter = Filters.chat(username=admin)

updater = Updater(token=os.getenv('TELEGRAM_TOKEN'), use_context=True)
dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)

# thread_dict = {}
#
#
# class GameThread(Thread):
#
#     def __init__(self,telnet_session,context,update):
#         Thread.__init__(self)
#         self.telnet_session = telnet_session
#         self.context = context
#         self.update = update
#         self.li = [b'\?\s*$', b'\>\s*$', b'\.\s*$', b'RETURN\:\s*$', b'\:\s*$']
#         keyboard = [
#             [InlineKeyboardButton('Norte', callback_data='Norte')],
#             [InlineKeyboardButton('Sur', callback_data='Sur')],
#             [InlineKeyboardButton('Este', callback_data='Este')],
#             [InlineKeyboardButton('Oeste', callback_data='Oeste')],
#         ]
#         self.reply_markup = InlineKeyboardMarkup(keyboard)
#
#
#     def run(self):
#         while self.telnet_session.sock is not None:
#             s = self.telnet_session.expect(self.li)
#             logging.debug('The server says {}'.format(repr(s)))
#             if s[1] is not None:
#                 if s[0] == 3: #Ends with RETURN: then hit return
#                     self.telnet_session.write('\n'.encode('latin-1'))
#                 else:
#                     self.context.bot.send_message(
#                         chat_id=self.update.effective_chat.id,
#                         text='```\n' + s[2].decode('latin-1').rstrip() + '\n```',
#                         parse_mode='MarkDown')
#                     self.update.message.reply_text('aa', reply_markup=self.reply_markup)
#
#     def stop(self):
#         self.context.bot.send_message(
#             chat_id=self.update.effective_chat.id,
#             text='```\ncerrando conexión...\n```',
#             parse_mode='MarkDown')
#         self.telnet_session.close()
#
#     def get_telnet_session(self):
#         return self.telnet_session


# def stop(update, context):
#     thread_dict[update.effective_chat.id].stop()
#     del thread_dict[update.effective_chat.id]
#
#
# stop_handler = CommandHandler('cerrar', stop)
# dispatcher.add_handler(stop_handler)

messages_sent = 0

def missatges(update, context):
    global messages_sent
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text='```\nHe enviat {} missatges.\n```'.format(messages_sent),
                             parse_mode='MarkDown')


missatges_handler = CommandHandler('missatges', missatges, filters=admin_filter)
dispatcher.add_handler(missatges_handler)


def hola(update, context):
    query = update.inline_query.query
# expr = re.compile('.*[h|H]ola')
# if expr.search(query) is not None:
    results = [
        InlineQueryResultArticle(
            id=uuid4(),
            title="Caps",
            input_message_content=InputTextMessageContent(
                query.upper())),
        InlineQueryResultArticle(
            id=uuid4(),
            title="Bold",
            input_message_content=InputTextMessageContent(
                "*{}*".format(escape_markdown(query)),
                parse_mode=ParseMode.MARKDOWN)),
        InlineQueryResultArticle(
            id=uuid4(),
            title="Italic",
            input_message_content=InputTextMessageContent(
                "_{}_".format(escape_markdown(query)),
                parse_mode=ParseMode.MARKDOWN))]

    update.inline_query.answer(results)

hola_handler = InlineQueryHandler(hola)
dispatcher.add_handler(hola_handler)

updater.start_polling()