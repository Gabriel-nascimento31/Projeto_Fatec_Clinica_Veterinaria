class Pagamento:
    def __init__(self, nome:str, prontuario:int, forma:str, valor_medicamentos:float, valor_procedimentos:float, valor_total:float, data_hora_pagamento):
        self.nome = nome
        self.prontuario = prontuario
        self.forma = forma
        self.valor_medicamentos = valor_medicamentos
        self.valor_procedimentos = valor_procedimentos
        self.valor_total = valor_total
        