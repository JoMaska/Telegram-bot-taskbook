from environs import Env
from dataclasses import dataclass

@dataclass
class TgBot:
    token: str
    admin_id: int
    
@dataclass
class Database:
    url: str

@dataclass
class Storage:
    host: str
    port: int
    db: int

@dataclass
class Config:
    bot: TgBot
    db: Database
    redis: Storage
    
def load_config(path: str | None = None):
    env = Env()
    env.read_env(path)
    return Config(
        bot=TgBot(
            token=env("BOT_TOKEN"),
            admin_id=env("ADMIN_ID")
            ),
        db=Database(
            url=env("DB_URL")
        ),
        redis=Storage(
            host=env("REDIS_HOST"),
            port=env("REDIS_PORT"),
            db=env("REDIS_DB")
        )
    )