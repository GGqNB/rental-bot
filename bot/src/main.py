import asyncio
import logging
from aiogram.types import Message
from aiogram import Bot, Dispatcher
from aiogram.enums.parse_mode import ParseMode
from aiogram import types, F, Router
from aiogram.fsm.storage.memory import MemoryStorage

import config

from handlers import router

bot = Bot(token=config.BOT_TOKEN, parse_mode=ParseMode.HTML)
async def main():
    dp = Dispatcher(storage=MemoryStorage())
    dp.include_router(router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())
    



if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
    