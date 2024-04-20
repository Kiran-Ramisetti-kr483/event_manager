from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_async_db
from settings.config import Settings

def get_settings() -> Settings:
    return Settings()

async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async for session in get_async_db():
        yield session
