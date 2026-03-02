from dataclasses import dataclass
from os import getenv
from dotenv import load_dotenv

load_dotenv()


@dataclass
class Config:
    bot_token: str
    openai_api_key: str
    openai_model: str = "gpt-4o-mini"
    openai_base_url: str = "https://api.openai.com/v1"

def load_config() -> Config:
    token = getenv("BOT_TOKEN")
    if not token:
        raise ValueError("BOT_TOKEN не установлен!")
    
    openai_key = getenv("OPENAI_API_KEY")
    if not openai_key:
        raise ValueError("OPENAI_API_KEY не установлен!")
    
    model = getenv("OPENAI_MODEL", "gpt-4o-mini")
    base_url = getenv("OPENAI_BASE_URL", "https://api.openai.com/v1")
    
    return Config(
        bot_token=token,
        openai_api_key=openai_key,
        openai_model=model,
        openai_base_url=base_url
    )

