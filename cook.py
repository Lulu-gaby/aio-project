import asyncio
from aiogram import Bot, Dispatcher,F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
import random
import requests

from config import TOKEN, ART_API_KEY

bot = Bot (token=TOKEN)
dp = Dispatcher()

def get_


async def main():
    await dp.start_polling(bot)

if __name__=='__main__':
    asyncio.run(main())