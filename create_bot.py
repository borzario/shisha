from aiogram import Bot
from aiogram.dispatcher import Dispatcher
import os
from aiogram.contrib.fsm_storage.memory import MemoryStorage

import tok

storage = MemoryStorage()
bot = Bot(token = tok.TOKEN)
dp = Dispatcher(bot, storage=storage)