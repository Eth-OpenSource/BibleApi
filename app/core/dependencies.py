from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession
import redis.asyncio as redis

from app.core.database import AsyncSessionLocal
from app.core.config import settings

async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSessionLocal() as session:
        yield session

async def get_redis() -> AsyncGenerator[redis.Redis, None]:
    client = redis.from_url(settings.REDIS_URL, decode_responses=True)
    try:
        yield client
    finally:
        await client.aclose()
