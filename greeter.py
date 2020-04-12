from telegram.ext import MessageHandler
from random import randint, choice
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)

class Greeter:
    def __init__(self, greetings, filter, p):
        self.greetings = greetings
        self.filter = filter
        self.p = p

    def _prob(self):
        r = randint(0, 100)
        if r <= self.p:
            return True
        else:
            return False

    def f(self, update, context):
        if self._prob():
            context.bot.send_message(
                chat_id=update.effective_chat.id,
                text=choice(self.greetings).format(update.effective_user.first_name),
                parse_mode='MarkDown')

    def get_handler(self):
        return MessageHandler(self.filter , self.f)
