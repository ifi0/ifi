from telethon.sync import TelegramClient
from telethon.sessions import StringSession
import os
APP_ID = os.environ.get("APP_ID", "18421930")
APP_HASH = os.environ.get("APP_HASH", "9cf3a6feb6dfcc7c02c69eb2c286830e")
SESSION = os.environ.get("SESSION")
ha313so = TelegramClient(StringSession(SESSION), APP_ID, APP_HASH)
ha313so.start()
