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

produto1 = Produto('antibiótico', '1234', 'petlog', 2.50, 3.00, '09/10/2026', '20/12/2028', 500)
produto2 = Produto('vacina antirrabica', '1020', 'vacinas pet', 45.00, 89.90, '26/10/2026', '26/10/2031', 40)
produto3 = Produto('rifocina', '3040', 'petcamp', 12.50, 28.00, '20/10/2026', '20/10/2028', 120)
produto4 = Produto('vacina pra raiva', '5060', 'vacinas pet', 15.00, 32.50, '15/10/2026', '15/10/2031', 200)
