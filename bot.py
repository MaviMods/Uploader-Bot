# Hey Give Me Star 🥲



import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import os
from plugins.config import Config

from pyrogram import Client as Ntbots
from pyrogram import filters
logging.getLogger("pyrogram").setLevel(logging.WARNING)


if __name__ == "__main__" :

    if not os.path.isdir(Config.DOWNLOAD_LOCATION):
        os.makedirs(Config.DOWNLOAD_LOCATION)
    plugins = dict(root="plugins")
    Ntbots = Ntbots(
        "UploadLinkToFileBot",
        bot_token=Config.MAVI_TOKEN,
        api_id=Config.MAVI_ID,
        api_hash=Config.MAVI_HASH,
        plugins=plugins)

    print("🎊 I AM ALIVE @MAVIMODS 🎊")
    Ntbots.run()

