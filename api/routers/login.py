from typing import Annotated
from fastapi import APIRouter, Depends
from api.models import LoginUser
from api.services import UserLoger
from api.routers.dependencies import get_user_loger

login_router = APIRouter(prefix="/user")


@login_router.post("/login")
def login(request: LoginUser, user_loger: Annotated[UserLoger, Depends(get_user_loger)]):
    response = user_loger.login(request=request)
    return response
