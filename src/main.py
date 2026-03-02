import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode

from src.config import load_config
from src.handlers import routers
from src.handlers.base import init_openai
from src.openai_client import OpenAIClient

async def run_bot() -> None:
    config = load_config()
    bot = Bot(config.bot_token)
    dp = Dispatcher()

    # Инициализируем OpenAI клиент
    openai_client = OpenAIClient(config)
    init_openai(openai_client)

    # Подключаем все роутеры из handlers/__init__.py
    for router in routers:
        dp.include_router(router)

    # Запуск поллинга
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(run_bot())
