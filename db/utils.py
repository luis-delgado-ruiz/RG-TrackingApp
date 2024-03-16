from typing import Optional

from pydantic_settings import BaseSettings, SettingsConfigDict
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from api.models import User, Order


class DbConfig(BaseSettings):
    model_config = SettingsConfigDict(env_nested_delimiter="__", extra="ignore", populate_by_name=True)
    host: str
    username: str
    password: str
    db_name: str
    db_type: str
    dialect: str
    driver: Optional[str] = None

    def _get_alt_conn_str(self) -> str:
        conn_str = f"{self.db_type}+{self.dialect}://{self.username}:{self.password}@{self.host}/{self.db_name}"
        return conn_str

    def _get_conn_str_env(self) -> str:
        conn_str = f"{self.db_type}://{self.username}:{self.password}@{self.host}/{self.db_name}"
        return conn_str

    def get_session_maker(self) -> sessionmaker[Session]:
        conn_str = self._get_conn_str()
        engine = create_engine(url=conn_str, echo=True)
        session_maker = sessionmaker(engine)
        return session_maker


class DatabaseManager:
    def _get_conn_str(self) -> str:
        return "postgresql://u6629vaobotsq3:p925a17619a08269901521924716c43fb1fb92c81860f0988e4a365160f4fca71@cc3engiv0mo271.cluster-czrs8kj4isg7.us-east-1.rds.amazonaws.com:5432/df66be9g7ski4r"

    def get_session_maker(self) -> sessionmaker[Session]:
        conn_str = self._get_conn_str()
        engine = create_engine(url=conn_str, echo=True)
        session_maker = sessionmaker(bind=engine)
        return session_maker

    def create_tables(self):
        conn_str = self._get_conn_str()
        engine = create_engine(url=conn_str, echo=True)
        User.metadata.create_all(engine)
        Order.metadata.create_all(engine)

    def get_user_by_username(self, db: Session, username: str):
        return db.query(User).filter(User.username == username).first()
