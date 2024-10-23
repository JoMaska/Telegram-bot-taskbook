from environs import Env
from dataclasses import dataclass

@dataclass
class TgBot:
    token: str
    admins_id: str
    
@dataclass
class Database:
    url: str

@dataclass
class Config:
    bot: TgBot
    db: Database
    
def load_config(path: str | None = None):
    env = Env()
    env.read_env(path)
    return Config(
        bot=TgBot(
            token=env("BOT_TOKEN"),
            admins_id=env("ADMINS_ID")
            ),
        db=Database(
            url=env("DB_URL")
        )
    )