import asyncio
from bot.config import bot, dp
from databases.core import init_db
from bot import callback_hand
from bot.handlers import boxes_handlers, handlers_business, handlers_private, lucky_bomb_handlers, handlers_tower
from bot.send_gifts import sender

async def main():
    await init_db()
    await dp.start_polling(bot)
if __name__ == "__main__":
    asyncio.run(main())