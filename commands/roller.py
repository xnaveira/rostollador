import re
from random import randint

from telegram import ParseMode

from commands.command import Command

class Roller(Command):
    def __init__(self, cmd, msg, msgargs, filter):
        super(Roller, self).__init__(cmd, msg, msgargs, filter)

    def _build_answer(self, context):
        roll = re.compile(r'^(\d+)d(\d+)$')
        n = roll.match(context.args[0])
        cardinal = int(n.group(1))
        dice = int(n.group(2))
        result = []
        for i in range(0, cardinal):
            result.append(randint(1, dice))
        return 'Has tret un {} <i>{}</i>'.format(sum(result), result)

    def f(self, update, context):
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text=self._build_answer(context),
                                 parse_mode=ParseMode.HTML)
