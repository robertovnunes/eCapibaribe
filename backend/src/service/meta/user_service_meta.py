from abc import ABC, abstractmethod

from src.schemas.user import UserGet

class UserServiceMeta(ABC):

    @abstractmethod
    def get_user(self, user_id: str) -> UserGet:
        """Get user by id method definition"""
        pass