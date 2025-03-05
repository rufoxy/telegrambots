from app.database.models import async_main
from app.handlers import router
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
import os
import asyncio
import nest_asyncio
nest_asyncio.apply()


async def main():
    load_dotenv()
    await async_main()
    bot = Bot(os.environ.get('TOKENSHOPBOT'))
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
