import asyncio

from config import TOKEN
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram import Bot, Dispatcher

bot = Bot(token = TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer("Salom!")

async def main():
    await dp.start_polling(bot)
    
    

if __name__ == '__main__':
    asyncio.run(main())
    print("Started")
