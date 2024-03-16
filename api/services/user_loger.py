import bcrypt
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from api.models import User, LoginUser


class UserLoger:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def login(self, request: LoginUser):
        try:
            user = self.db_session.query(User).filter(User.username == request.username).first()
            password = self.db_session.query(User).filter(User.password == request.password).first()
        except IntegrityError as integrity_error:
            raise integrity_error
        if user is None or password is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid username or password",
            )
        return {"username": user.username, "role": user.role}

