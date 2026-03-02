from openai import AsyncOpenAI

from src.config import Config


class OpenAIClient:
    def __init__(self, config: Config):
        self.client = AsyncOpenAI(
            api_key=config.openai_api_key,
            base_url=config.openai_base_url
        )
        self.model = config.openai_model

    async def get_completion(self, messages: list[dict]) -> str:
        """
        Получает ответ от модели OpenAI.
        
        Args:
            messages: Список сообщений в формате [{"role": "user|assistant", "content": "text"}]
        
        Returns:
            Ответ модели в виде строки
        """
        response = await self.client.chat.completions.create(
            model=self.model,
            messages=messages,
        )
        return response.choices[0].message.content
