from datetime import datetime
class Prontuario:
    def __init__(self, numero, nome_animal, nome_tutor, veterinario, data_hora_abertura, medicamentos_utilizados, procedimentos_realizados):
        self.numero = numero
        self.nome_animal = nome_animal
        self.nome_tutor = nome_tutor
        self.veterinario = veterinario
        self.data_hora_abertura = datetime.now()
        self.medicamentos_utilizados = medicamentos_utilizados
        self.procedimentos_realizados = procedimentos_realizados