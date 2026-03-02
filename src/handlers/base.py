import random

from aiogram import types, Router
from aiogram.filters import CommandStart
from aiogram.types import ContentType

from src.openai_client import OpenAIClient
from src.const import PROMPT


router = Router()
openai_client: OpenAIClient | None = None


def init_openai(client: OpenAIClient) -> None:
    global openai_client
    openai_client = client


@router.message(CommandStart())
async def command_start_handler(message: types.Message) -> None:
    await message.answer(f"Привет, {message.from_user.full_name}!")


@router.message(lambda msg: msg.content_type == ContentType.TEXT)
async def chat_handler(message: types.Message) -> None:
    if openai_client is None:
        await message.answer("Сервис временно недоступен :(")
        return
    if random.random() > 0.85 or 'сафрон' in message.text.lower():        
        try:
            messages = [
                {"role": "system", "content": PROMPT},
                {"role": "user", "content": f"@{message.from_user.username}: '{message.text}'." or ""}
            ]
            
            response = await openai_client.get_completion(messages)
            await message.reply(response)
        except Exception as e:
            await message.answer(f"Произошла ошибка при обработке запроса :(")
