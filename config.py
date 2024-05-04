from telethon.sync import TelegramClient
from telethon.sessions import StringSession
import os
APP_ID = os.environ.get("APP_ID", "29885460")
APP_HASH = os.environ.get("APP_HASH", "9fece1c7f0ebf1526ed9ade4cb455a03")
SESSION = os.environ.get("SESSION")
ha313so = TelegramClient(StringSession(SESSION), APP_ID, APP_HASH)
ha313so.start()
