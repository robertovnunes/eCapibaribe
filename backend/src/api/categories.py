from fastapi import APIRouter, status
from ..schemas.response import HttpResponseModel, HTTPResponses
from ..service.impl.category_service import categoryService
from pydantic import BaseModel
from typing import Union


router = APIRouter()


class Category(BaseModel):
    id: Union[str, None] = None
    name: str
    description: str
    image: str
    keywords: list
    items: list


@router.get(
    "/",
    response_model=HttpResponseModel,
    status_code=status.HTTP_200_OK,
    description="Retrieve all categories",
    tags=["categories"],
    responses={
        status.HTTP_200_OK: {
            "model": HttpResponseModel,
            "description": "Successfully got all the categories",
        }
    },
)
def get_categories() -> HttpResponseModel:
    """
    Get all categories.

    Returns:
    - A list of all categories.

    """

    category_list_response = categoryService.get_categories()

    return category_list_response


@router.get(
    "/{category_id}",
    response_model=HttpResponseModel,
    status_code=status.HTTP_200_OK,
    description="Retrieve an category by its ID",
    tags=["categories"],
    responses={
        status.HTTP_200_OK: {
            "model": HttpResponseModel,
            "description": "Successfully got category by id",
        },
        status.HTTP_404_NOT_FOUND: {
            "description": "category not found",
        }
    },
)
def get_category(category_id: str) -> HttpResponseModel:
    """
    Get category by ID.

    Parameters:
    - category_id: The ID of the category to retrieve.

    Returns:
    - The category with the specified ID.

    Raises:
    - HTTPException 404: If the category is not found.

    """
    category_get_response = categoryService.get_category(category_id)
    return category_get_response


# TODO: Add POST, PUT, DELETE endpoints


@router.post(
    "/",
    response_model=HttpResponseModel,
    status_code=status.HTTP_200_OK,
    description="Posting category",
    tags=["categories"],
    responses={
        status.HTTP_200_OK: {
            "model": HttpResponseModel,
            "description": "Successfully inserted category",
        }
    },
)
def post_category(category: Category) -> HttpResponseModel:
    """
    Post category.

    Returns:
    - A list of all categories.

    """
    categories = categoryService.get_categories()
    categories = categories.data
    for c in categories:
        if category.name == c["name"]:
            return HttpResponseModel(
                message=HTTPResponses.CATEGORY_ALREADY_EXISTS().message,
                status_code=HTTPResponses.CATEGORY_ALREADY_EXISTS().status_code,
            )
    category.id = str((int(categories[-1]["id"]) + 1))

    print(category)
    category_post_response = categoryService.post_category(category)

    return category_post_response


@router.put(
    "/{category_id}",
    response_model=HttpResponseModel,
    status_code=status.HTTP_200_OK,
    description="Upddate some category",
    tags=["categories"],
    responses={
        status.HTTP_200_OK: {
            "model": HttpResponseModel,
            "description": "Successfully updated category",
        }
    },
)
def put_category(category_id, category) -> HttpResponseModel:
    """
    Put category.

    Returns:
    - A list of all categories.

    """

    category_list_response = categoryService.put_category(category_id, category)

    return category_list_response


@router.delete(
    "/{category_id}",
    response_model=HttpResponseModel,
    status_code=status.HTTP_200_OK,
    description="Delete some category",
    tags=["categories"],
    responses={
        status.HTTP_200_OK: {
            "model": HttpResponseModel,
            "description": "Successfully deleted category",
        }
    },
)
def delete_category(category_id: str) -> HttpResponseModel:
    """
    Delete category.

    Returns:
    - A list of all categories.

    """

    category_list_response = categoryService.delete_category(category_id)

    return category_list_response
