from fastapi import APIRouter, status
from ..schemas.response import HttpResponseModel, HTTPResponses
from ..features.categories.service.category_service import categoryService
from pydantic import BaseModel
from typing import Union


router = APIRouter()


def validatefield(value) -> bool:
    '''
    Validates the model fields
    returns a list of missing fields
    '''
    if value is None:
        return True
    return False

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
            "description": "Categoria encontrada",
        },
        status.HTTP_404_NOT_FOUND: {
            "description": "Categoria náo existe",
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
    missingfieldslist = []
    for f, v in category.model_fields.items():
        if validatefield(v):
            missingfieldslist.append(f.__str__())
    if len(missingfieldslist) > 0:
        return HttpResponseModel(
            message="Missing fields",
            status_code=400,
            data={"fields": missingfieldslist}
        )

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
def put_category(category_id, category: Category) -> HttpResponseModel:

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
