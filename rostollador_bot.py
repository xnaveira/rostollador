import logging
import os
from telegram.ext import Filters
from command import Command
from greeter import Greeter
from rostollador import Rostollador

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)

def main():
    admin = os.getenv('ADMIN_USER')
    telegram_token = os.getenv('TELEGRAM_TOKEN')

    handlers = []
    handlers.append(
        Greeter(
            ['Hola {}', 'Què tal {}?', 'Com vas {}?', 'Què dius {}?', 'Com ho portes {}?'],
            Filters.regex('.*[H|h]ola.*'),
            60
        )
    )
    handlers.append(
        Greeter(
            ['Bon dia {}', 'Bon dia tinguis {}'],
            Filters.regex('.*[B|b]on\s+dia.*'),
            60
        )
    )
    handlers.append(
        Greeter(
            ['Què?', 'Com dius {}?', 'Are you talking to ME?', 'T''he sentit {}'],
            Filters.regex('.*[B|b][O|o][T|t].*'),
            50
        )
    )
    handlers.append(
        Command(
            'versio',
            'La meva versió és {}',
            ['3.0.0'],
            Filters.chat(username=admin)
        )
    )

    r = Rostollador(admin, telegram_token, handlers)
    r.start()


main()










