from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from src.core.config import settings

"""
    DATABASE SETUP : 
        - USING THE ASYNC ENGINE
"""


engine = create_async_engine(
    url=settings.DATABASE_URL,
    pool_size=10,  # Keeping this as 10 connections since not a lot trafic we will be using
    max_overflow=20,
    pool_timeout=30,
    pool_recycle=1800,
    pool_pre_ping=True,
)


SessionLocal = async_sessionmaker(
    bind=engine, expire_on_commit=True, autoflush=False, autocommit=False
)
