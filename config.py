from telethon.sync import TelegramClient
from telethon.sessions import StringSession
import os
APP_ID = os.environ.get("APP_ID", "29285293")
APP_HASH = os.environ.get("APP_HASH", "74b1df0fa75271117354959a68cc2fc6")
SESSION = os.environ.get("SESSION")
ha313so = TelegramClient(StringSession(SESSION), APP_ID, APP_HASH)
ha313so.start()
