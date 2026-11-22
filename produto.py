class Produto:
    def __init__(self, nome:str, codigo:str, fornecedor:str, preco_compra:float, preco_venda:float, data_compra, data_validade, quantidade:int):
        self.nome = nome
        self.codigo = codigo
        self.fornecedor = fornecedor
        self.preco_compra = preco_compra
        self.preco_venda = preco_venda
        self.data_compra = data_compra
        self.data_validade = data_validade
        self.quantidade = quantidade