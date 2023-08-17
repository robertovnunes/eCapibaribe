from pydantic import BaseModel

class Item(BaseModel):
    item_id: int
    item_nome: str
    item_price: float
    quantidade: int
    marca: str
    categoria: str
    descricao: str
    imagem: str
    op_envio: str
    palavrachave: str | None = None
    #criar o cpf do usuario que registrou o item