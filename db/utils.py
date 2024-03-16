from pydantic_settings import BaseSettings
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from api.models import User, Order


class DbConfig(BaseSettings):
    db_conn_str: str

    def _get_conn_str(self) -> str:
        return self.db_conn_str

    def get_session_maker(self) -> sessionmaker[Session]:
        conn_str = self._get_conn_str()
        engine = create_engine(url=conn_str, echo=True)
        session_maker = sessionmaker(engine)
        return session_maker

    def create_tables(self):
        conn_str = self._get_conn_str()
        engine = create_engine(url=conn_str, echo=True)
        User.metadata.create_all(engine)
        Order.metadata.create_all(engine)
