from aiogram import Bot, Dispatcher
import os
from dotenv import load_dotenv

load_dotenv()

bot = Bot(os.getenv('TOKEN'))
BUSINESS_ID = os.getenv('BUSINESS_ID')
TON_API = os.getenv('TON_API')
key = os.getenv('KEY')
dp = Dispatcher()