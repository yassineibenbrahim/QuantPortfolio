from __future__ import annotations

import os

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DEFAULT_DB_USER = "quantportfolio"
DEFAULT_DB_PASSWORD = "quantportfolio"
DEFAULT_DB_HOST = "db"
DEFAULT_DB_PORT = "5432"
DEFAULT_DB_NAME = "quantportfolio"

DEFAULT_DATABASE_URL = (
    f"postgresql+psycopg2://{DEFAULT_DB_USER}:{DEFAULT_DB_PASSWORD}"
    f"@{DEFAULT_DB_HOST}:{DEFAULT_DB_PORT}/{DEFAULT_DB_NAME}"
)

DATABASE_URL = os.getenv("DATABASE_URL", DEFAULT_DATABASE_URL)

engine = create_engine(DATABASE_URL, future=True)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False, future=True)
Base = declarative_base()
