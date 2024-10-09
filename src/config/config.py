from environs import Env
from dataclasses import dataclass

@dataclass
class TgBot:
    token: str
    
@dataclass
class Config:
    bot: TgBot
    
def load_config(path: str | None = None):
    env = Env()
    env.read_env(path)
    return Config(
        bot=TgBot(
            token=env("BOT_TOKEN")
            )
    )