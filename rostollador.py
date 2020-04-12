import logging
import os
from datetime import datetime
from telegram import ParseMode
from telegram.ext import Filters, Updater
from youtube_api import YouTubeDataAPI

from kvaasclient import Kvaas


class Rostollador:
    def __init__(self,
                 admin_user,
                 telegram_token,
                 handlers):
        self.admin_user = admin_user
        self.telegram_token = telegram_token
        self.admin_filter = Filters.chat(username=self.admin_user)
        self.updater = Updater(token=telegram_token, use_context=True)
        self.dispatcher = self.updater.dispatcher
        self.messages_sent = 0
        self.handlers = handlers

        self.nyofla_channel = os.getenv('NYOFLA_YT_CHANNEL')
        self.channel_rostollador_i_jo = os.getenv('ROSTOLLADOR_I_JO_CHANNEL')
        self.channel_rostolladors_hab = os.getenv('ROSTOLLADORS_CHANNEL')
        self.youtube_api_key = os.getenv('YOUTUBE_API_KEY')

        self.yt = YouTubeDataAPI(self.youtube_api_key)
        self.last_checked = datetime.fromtimestamp(0)

    def latest_nyofla_youtube(self, unused):
        global messages_sent
        # global last_checked

        kvaas_client = Kvaas()
        last_checked = datetime(1970, 1, 1, 0, 0, 0)  # init in the past
        fmt = '%c'

        try:
            stored_date = kvaas_client.getValue('lc')
        except:
            stored_date = last_checked
            logging.warning("Couldn''t retrieve stored date")

        try:
            last_checked = last_checked.strptime(stored_date, fmt)
        except Exception:
            logging.warning(Exception)

        ylist = self.yt.search(channel_id=self.nyofla_channel, search_type="video", max_results=1, order_by="date")
        if len(ylist) > 0:
            ylatest = ylist[0]
            if ylatest['video_publish_date'] > last_checked:
                kvaas_client.setValue('lc', ylatest['video_publish_date'].strftime(fmt))
                self.updater.bot.send_message(chat_id=self.channel_rostolladors_hab,
                                         text='Nou video de {}\n https://www.youtube.com/watch?v={}'.format(
                                             ylatest['channel_title'], ylatest['video_id']),
                                         parse_mode=ParseMode.HTML)

    def start(self):
        for handler in self.handlers:
            self.dispatcher.add_handler(handler.get_handler())
        self.dispatcher.job_queue.run_repeating(self.latest_nyofla_youtube, 2700, 0, 'NyoflaYT')
        self.updater.start_polling()