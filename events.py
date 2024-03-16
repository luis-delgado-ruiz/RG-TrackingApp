from contextlib import asynccontextmanager
from typing import TypedDict, AsyncIterator

from sqlalchemy.orm import Session, sessionmaker
from fastapi import FastAPI

from db import DatabaseManager


class State(TypedDict):
    session_maker: sessionmaker[Session]


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[State]:
    db_manager = DatabaseManager()
    db_manager.create_tables()
    db_session = db_manager.get_session_maker()

    state_dict = {
        "session_maker": db_session,
    }

    yield State(**state_dict)
