from aiogram import Bot, Dispatcher
import asyncio
from handlers import start, create, get, delete, update
import dotenv, os



dotenv.load_dotenv()
Token = os.getenv('Token')


bot=Bot(Token)
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