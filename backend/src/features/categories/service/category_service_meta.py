
from abc import ABC, abstractmethod

from ....schemas.category import CategoryGet
from ....schemas.response import HttpResponseModel


class CategoryServiceMeta(ABC):

    @abstractmethod
    def get_category(self, category_id: str) -> HttpResponseModel:
        """Get category by id method definition"""

    @abstractmethod
    def get_categories(self) -> list:
        """Get all categories method definition"""

