from telegram.ext import MessageHandler
from random import choice
from rostolladorhandler import RostolladorHandler
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)


class Greeter(RostolladorHandler):
    def __init__(self, greetings, f, p):
        super().__init__(p)
        self.greetings = greetings
        self.filter = f

    def _build_answer(self, update):
        return choice(self.greetings).format(update.effective_user.first_name)

    def f(self, update, context):
        if self._prob():
            context.bot.send_message(
                chat_id=update.effective_chat.id,
                text=self._build_answer(update),
                parse_mode='MarkDown')

    def get_handler(self):
        return MessageHandler(self.filter, self.f)
