from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
import os
from dotenv import load_dotenv

load_dotenv()

default_bot_properties = DefaultBotProperties(parse_mode="HTML")
bot = Bot(os.getenv('TOKEN'), default=default_bot_properties)

BUSINESS_ID = os.getenv('BUSINESS_ID')
TON_API = os.getenv('TON_API')
key = os.getenv('KEY')
dp = Dispatcher()
channel = os.getenv('CHANNEL_USERNAME')