from typing import Optional
from pydantic import BaseModel


class HttpResponseModel(BaseModel):
    message: str
    status_code: int
    data: Optional[dict] | Optional[list] = None


class HTTPResponses:
    """
    This class contains the basic HTTP responses for the API
    """

    @staticmethod
    def ITEM_NOT_FOUND() -> HttpResponseModel:
        return HttpResponseModel(
            message="Item not found",
            status_code=404,
        )

    @staticmethod
    def ITEM_FOUND() -> HttpResponseModel:
        return HttpResponseModel(
            message="Item found",
            status_code=200,
        )

    @staticmethod
    def ITEM_CREATED() -> HttpResponseModel:
        return HttpResponseModel(
            message="Item created",
            status_code=201,
        )

    @staticmethod
    def CATEGORY_NOT_FOUND() -> HttpResponseModel:
        return HttpResponseModel(
            message="Category not found",
            status_code=404,
        )

    @staticmethod
    def CATEGORY_FOUND() -> HttpResponseModel:
        return HttpResponseModel(
            message="Category found",
            status_code=200,
        )

    @staticmethod
    def CATEGORIES_NOT_FOUND() -> HttpResponseModel:
        return HttpResponseModel(
            message="Category not found",
            status_code=404,
        )

    @staticmethod
    def CATEGORIES_FOUND() -> HttpResponseModel:
        return HttpResponseModel(
            message="Category found",
            status_code=200,
        )

    @staticmethod
    def CATEGORY_CREATED() -> HttpResponseModel:
        return HttpResponseModel(
            message="Category created",
            status_code=201,
        )

    @staticmethod
    def CATEGORY_NOT_CREATED() -> HttpResponseModel:
        return HttpResponseModel(
            message="Category not created",
            status_code=500,
        )

    @staticmethod
    def USER_NOT_FOUND() -> HttpResponseModel:
        return HttpResponseModel(
            message="User not found",
            status_code=404,
        )

    @staticmethod
    def USER_FOUND() -> HttpResponseModel:
        return HttpResponseModel(
            message="User found",
            status_code=200,
        )

    @staticmethod
    def USER_CREATED() -> HttpResponseModel:
        return HttpResponseModel(
            message="User created",
            status_code=201,
        )

    @staticmethod
    def SERVER_ERROR() -> HttpResponseModel:
        return HttpResponseModel(
            message="Server error",
            status_code=500,
        )

    @staticmethod
    def CATEGORY_NOT_UPDATED() -> HttpResponseModel:
        return HttpResponseModel(
            message="Category not updated",
            status_code=500,
        )

    @staticmethod
    def CATEGORY_UPDATED() -> HttpResponseModel:
        return HttpResponseModel(
            message="Category updated",
            status_code=200,
        )

    @staticmethod
    def CATEGORY_NOT_DELETED() -> HttpResponseModel:
        return HttpResponseModel(
            message="Category not deleted",
            status_code=500,
        )

    @staticmethod
    def CATEGORY_DELETED() -> HttpResponseModel:
        return HttpResponseModel(
            message="Category deleted",
            status_code=200,
        )

    @staticmethod
    def CATEGORY_ALREADY_EXISTS() -> HttpResponseModel:
        return HttpResponseModel(
            message="Category already exists",
            status_code=400,
        )

    @staticmethod
    def MISSING_FIELDS() -> HttpResponseModel:
        return HttpResponseModel(
            message="Missing fields",
            status_code=400,
        )
