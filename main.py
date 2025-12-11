from aiogram import Bot, Dispatcher
import asyncio
from handlers import start, create, get, delete, update
from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application
from aiohttp import web


bot=Bot('8550645746:AAE4Xeftx2NIOmQJqkebNYtLTMhmEGyjfMI')
dp=Dispatcher()


dp.include_router(start.router)
dp.include_router(create.router)
dp.include_router(get.router)
dp.include_router(delete.router)
dp.include_router(update.router)

async def main():
    print("Bot started")
    await dp.start_polling(bot)

asyncio.run(main())