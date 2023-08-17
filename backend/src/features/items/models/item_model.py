from pydantic import BaseModel

class Item(BaseModel):
    cpf_user: str
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
