from datetime import datetime
from fila import Fila

class Atendimento:
    def __init__(self, nome_animal=str, nome_tutor=str, data_hora_chegada=datetime.now, queixa_relatada=str):
        self.nome_animal = nome_animal
        self.nome_tutor = nome_tutor
        self.data_hora_chegada = data_hora_chegada
        self.queixa_relatada = queixa_relatada


atendimento_normal = Fila()
atendimento_emergencia = Fila()

atendimento1 = Atendimento('laila', 'Gabriel do Nascimento', 'pata machucada') 
atendimento2 = Atendimento('mel', 'Rafael Costa', 'falta de apetite')
atendimento3 = Atendimento('caramelo', 'Carlos Carvalho', 'picada de abelha')
atendimento4 = Atendimento('guilherme', 'Mariana Lima', 'machucado')
atendimento5 = Atendimento('totó', 'Roberto Souza', 'problema de audição')
atendimento6 = Atendimento('kica', 'Juliana Dias', 'atropelamento')
atendimento7 = Atendimento('tica', 'Bruno Santos', 'falta de ar')



atendimento_normal.enfileirar(atendimento1)
atendimento_normal.enfileirar(atendimento2)
atendimento_normal.enfileirar(atendimento3)
atendimento_normal.enfileirar(atendimento4)
atendimento_normal.enfileirar(atendimento5)
atendimento_emergencia.enfileirar(atendimento6)
atendimento_emergencia.enfileirar(atendimento7)