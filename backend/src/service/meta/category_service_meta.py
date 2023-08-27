
from abc import ABC, abstractmethod

from ...schemas.category import CategoryGet

class CategoryServiceMeta(ABC):

    @abstractmethod
    def get_category(self, category_id: str) -> CategoryGet:
        """Get category by id method definition"""
