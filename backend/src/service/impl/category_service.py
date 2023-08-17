from src.schemas.response import HTTPResponses, HttpResponseModel
from src.service.meta.category_service_meta import CategoryServiceMeta
from src.db.__init__ import database as db


class categoryService(CategoryServiceMeta):

    @staticmethod
    def get_category(category_id: str) -> HttpResponseModel:
        """Get category by id method implementation"""
        category = db.get_category_by_id('categories', category_id)
        if not category:
            return HttpResponseModel(
                message=HTTPResponses.CATEGORY_NOT_FOUND().message,
                status_code=HTTPResponses.CATEGORY_NOT_FOUND().status_code,
            )
        return HttpResponseModel(
            message=HTTPResponses.CATEGORY_FOUND().message,
            status_code=HTTPResponses.CATEGORY_FOUND().status_code,
            data=category,
        )

    @staticmethod
    def get_categories():
        """Get category method implementation"""
        categories = db.get_all_categories('categories')
        if not categories:
            return HttpResponseModel(
                message=HTTPResponses.CATEGORY_NOT_FOUND().message,
                status_code=HTTPResponses.CATEGORY_NOT_FOUND().status_code,
            )

        return HttpResponseModel(
            message=HTTPResponses.CATEGORY_FOUND().message,
            status_code=HTTPResponses.CATEGORY_FOUND().status_code,
            data=categories,
        )

    @staticmethod
    def post_category(category):
        """Post category method implementation"""
        category = db.insert_category('categories', category)
        if not category:
            return HttpResponseModel(
                message=HTTPResponses.CATEGORY_NOT_CREATED().message,
                status_code=HTTPResponses.CATEGORY_NOT_CREATED().status_code,
            )

        return HttpResponseModel(
            message=HTTPResponses.CATEGORY_CREATED().message,
            status_code=HTTPResponses.CATEGORY_CREATED().status_code,
            data=category,
        )

    @staticmethod
    def put_category(category_id: str, category: dict):
        """Put category method implementation"""
        category = db.update_category('categories', category_id, category)
        if not category:
            return HttpResponseModel(
                message=HTTPResponses.CATEGORY_NOT_UPDATED().message,
                status_code=HTTPResponses.CATEGORY_NOT_UPDATED().status_code,
            )

        return HttpResponseModel(
            message=HTTPResponses.CATEGORY_UPDATED().message,
            status_code=HTTPResponses.CATEGORY_UPDATED().status_code,
            data=category,
        )

    @staticmethod
    def delete_category(category_id: str):
        """Delete category method implementation"""
        category = db.delete_category('categories', category_id)
        if not category:
            return HttpResponseModel(
                message=HTTPResponses.CATEGORY_NOT_DELETED().message,
                status_code=HTTPResponses.CATEGORY_NOT_DELETED().status_code,
            )

        return HttpResponseModel(
            message=HTTPResponses.CATEGORY_DELETED().message,
            status_code=HTTPResponses.CATEGORY_DELETED().status_code,
            data=category,
        )