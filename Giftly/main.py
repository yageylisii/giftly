import asyncio
from config import bot, dp
from handlers import handlers_private, handlers_business
import callback_hand
from databases.core import init_db

async def main():
    await init_db()
    await dp.start_polling(bot)
if __name__ == "__main__":
    asyncio.run(main())