from src.schemas.response import HTTPResponses, HttpResponseModel
from src.service.meta.user_service_meta import UserServiceMeta
from src.db.__init__ import database as db


class userService(UserServiceMeta):

    @staticmethod
    def get_user(user_id: str) -> HttpResponseModel:
        """Get user by id method implementation"""
        user = db.get_user_by_id('users', user_id)
        if not user:
            return HttpResponseModel(
                message=HTTPResponses.USER_NOT_FOUND().message,
                status_code=HTTPResponses.USER_NOT_FOUND().status_code,
            )
        return HttpResponseModel(
            message=HTTPResponses.USER_FOUND().message,
            status_code=HTTPResponses.USER_FOUND().status_code,
            data=user,
        )

    @staticmethod
    def get_users():
        """Get user method implementation"""
        users = db.get_all_users('users')
        if not users:
            return HttpResponseModel(
                message=HTTPResponses.USER_NOT_FOUND().message,
                status_code=HTTPResponses.USER_NOT_FOUND().status_code,
            )

        return HttpResponseModel(
            message=HTTPResponses.USER_FOUND().message,
            status_code=HTTPResponses.USER_FOUND().status_code,
            data=users,
        )

    # TODO: implement other methods (create, update, delete)