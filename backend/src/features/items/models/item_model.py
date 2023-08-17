from pydantic import BaseModel

class Item(BaseModel):
    cpf_user: str
    item_id: str
    item_nome: str
    item_price: str
    quantidade: str
    marca: str
    categoria: str
    descricao: str
    imagem: str
    op_envio: str
    palavrachave: str | None = None