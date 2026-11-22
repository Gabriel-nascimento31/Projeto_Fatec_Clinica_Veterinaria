from datetime import datetime

class Atendimento:
    def __init__(self, nome_animal:str, nome_tutor:str, queixa_relatada:str):
        self.nome_animal = nome_animal
        self.nome_tutor = nome_tutor
        self.data_hora_chegada = datetime.now()
        self.queixa_relatada = queixa_relatada