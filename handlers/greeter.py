from telegram.ext import MessageHandler, Filters
import yaml
from random import choice
from handlers.rostolladorhandler import RostolladorHandler
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)


class Greeter(RostolladorHandler, yaml.YAMLObject):
    yaml_tag = u'!greeter'

    def __init__(self, greetings, p, regex, regex_positive_tests, regex_negative_tests):
        super().__init__(p)
        self.greetings = greetings
        self.regex = regex
        self.regex_positive_tests = regex_positive_tests
        self.regex_negative_tests = regex_negative_tests

    def _build_answer(self, update):
        return choice(self.greetings).format(update.effective_user.first_name)

    def f(self, update, context):
        if self._prob():
            context.bot.send_message(
                chat_id=update.effective_chat.id,
                text=self._build_answer(update),
                parse_mode='MarkDown')

    def get_handler(self):
        return MessageHandler(Filters.regex(self.regex), self.f)
