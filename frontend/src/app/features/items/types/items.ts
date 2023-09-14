export interface Item {
    cpf_user: string,
    item_id: number,
    item_nome: string,
    item_price: number,
    quantidade: number,
    marca: string,
    categoria: string,
    descricao: string,
    imagem: string,
    op_envio: string,
    palavrachave: string | undefined
}

export const defaultItem: Item = {
    cpf_user: "123.456.789-10",
    item_id: 0,
    item_nome: "",
    item_price: 0,
    quantidade: 0,
    marca: "",
    categoria: "",
    descricao: "",
    imagem: "",
    op_envio: "",
    palavrachave: ""
}

export interface showItem {
    item_id: number,
    item_nome: string,
    item_price: number,
    quantidade: number,
    marca: string,
    categoria: string,
    imagem: string,
}