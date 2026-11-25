import asyncio
import logging

from aiogram import Bot, Dispatcher

from config import BOT_TOKEN

from handlers import start, catalog, cart, orders


async def main():
    logging.basicConfig(level=logging.INFO)

    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    dp.include_router(start.router)
    dp.include_router(catalog.router)
    dp.include_router(cart.router)
    dp.include_router(orders.router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())