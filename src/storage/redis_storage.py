import logging

from redis.asyncio.client import Redis
# from redis import asyncio as Redis

logger = logging.getLogger(__name__)

def redis_storage(host, port, db) -> Redis:
    redis_pool = Redis(
        host=host,
        port=port,
        db=db
                  )
    return redis_pool