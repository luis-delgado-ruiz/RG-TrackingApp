from starlette.requests import Request

from api.services import UserLoger


async def get_user_loger(request: Request) -> UserLoger:
    with request.state.session_maker() as db_session:
        return UserLoger(db_session=db_session)
