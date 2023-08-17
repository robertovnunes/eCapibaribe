from fastapi import APIRouter, status
from src.schemas.response import HttpResponseModel
from src.service.impl.user_service import userService

router = APIRouter()


@router.get(
    "/{user_id}",
    response_model=HttpResponseModel,
    status_code=status.HTTP_200_OK,
    description="Retrieve an user by its ID",
    tags=["users"],
    responses={
        status.HTTP_200_OK: {
            "model": HttpResponseModel,
            "description": "Successfully got user by id",
        },
        status.HTTP_404_NOT_FOUND: {
            "description": "user not found",
        }
    },
)
def get_user(user_id: str) -> HttpResponseModel:
    """
    Get user by ID.

    Parameters:
    - user_id: The ID of the user to retrieve.

    Returns:
    - The user with the specified ID.

    Raises:
    - HTTPException 404: If the user is not found.

    """
    user_get_response = userService.get_user(user_id)
    return user_get_response


@router.get(
    "/",
    response_model=HttpResponseModel,
    status_code=status.HTTP_200_OK,
    description="Retrieve all users",
    tags=["users"],
    responses={
        status.HTTP_200_OK: {
            "model": HttpResponseModel,
            "description": "Successfully got all the users",
        }
    },
)
def get_users() -> HttpResponseModel:
    """
    Get all users.

    Returns:
    - A list of all users.

    """

    user_list_response = userService.get_users()

    return user_list_response

# TODO: Add POST, PUT, DELETE endpoints