from schemas.response import HTTPResponses, HttpResponseModel
from service.meta.item_service_meta import ItemServiceMeta
from db.__init__ import database as db

class ItemService(ItemServiceMeta):

    @staticmethod
    def get_item(item_id: str) -> HttpResponseModel:
        """Get item by id method implementation"""
        item = db.get_item_by_id('itens', item_id)
        if not item:
            return HttpResponseModel(
                message=HTTPResponses.ITEM_NOT_FOUND().message,
                status_code=HTTPResponses.ITEM_NOT_FOUND().status_code,
            )
        return HttpResponseModel(
                message=HTTPResponses.ITEM_FOUND().message,
                status_code=HTTPResponses.ITEM_FOUND().status_code,
                data=item,
            )
    
    @staticmethod
    def get_itens():
        """Get itens method implementation"""
        itens = db.get_all_itens('itens')
        if not itens:
            return HttpResponseModel(
                message=HTTPResponses.ITEM_NOT_FOUND().message,
                status_code=HTTPResponses.ITEM_NOT_FOUND().status_code,
            )
        
        return HttpResponseModel(
                message=HTTPResponses.ITEM_FOUND().message,
                status_code=HTTPResponses.ITEM_FOUND().status_code,
                data=itens,
            )
    
    # TODO: implement other methods (create, update, delete)