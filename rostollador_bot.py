import logging
import yaml
import os
from telegram.ext import Filters
from commands.command import Command
from commands.roller import Roller
from rostollador import Rostollador
from handlers import greeter

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)

def main():
    admin = os.getenv('ADMIN_USER')
    telegram_token = os.getenv('TELEGRAM_TOKEN')
    with open('version', 'r') as v:
        version = v.read().rstrip()
    with open('handlers/greeters.yml') as f:
        gs = f.read()
    handlers = []
    for g in yaml.full_load_all(gs):
        handlers.append(g)
    handlers.append(
        Command(
            'versio',
            'La meva versió és {}',
            [version],
            Filters.chat(username=admin)
        )
    )
    handlers.append(
        Roller(
            'roll',
            '',
            '',
            None
        )
    )


    r = Rostollador(admin, telegram_token, handlers)
    r.start()


main()










