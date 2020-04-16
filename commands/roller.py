from commands.command import Command

class Roller(Command):
    def __init__(self, cmd, msg, msgargs, filter):
        super(Roller, self).__init__(cmd, msg, msgargs, filter)

