from telegram.ext import CommandHandler


class Command:
    def __init__(self, cmd, msg, msgargs, filter):
        self.cmd = cmd
        self.filter = filter
        self.msg = msg
        self.msgargs = msgargs

    def f(self, update, context):
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text=self.msg.format(*self.msgargs),
                                 parse_mode='MarkDown')

    def get_handler(self):
        return CommandHandler(self.cmd, self.f, self.filter)