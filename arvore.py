from random import choice

class No_arvore:
    def __init__(self, dado):
        self.dado = dado
        self.filhos = []
        self.estado = 'Não avaliado'
    
    def adicionar_filho(self, filho_no):
        self.filhos.append(filho_no)

    def realizar_diagnostico_recursivo(self):
        opcoes = ['saudável', 'alterado']
        self.estado = choice(opcoes)
        for filho in self.filhos:
            filho.realizar_diagnostico_recursivo()
    
    def __str__(self, nivel=0):
        resultado = " " * nivel + f"-{self.dado} [{self.estado}]\n"
        for filho in self.filhos:
            resultado += filho.__str__(nivel + 1)
        return resultado
    
    def percorrer_profundidade(self):
        print(self.dado)
        for filho in self.filhos:
            filho.percorrer_profundidade()


paciente = No_arvore("ANIMAL DE ESTIMAÇÃO (Paciente Veterinário)")


cardiorrespiratorio = No_arvore(" 1. Sistema Cardiorrespiratório")
cardiovascular = No_arvore("Sistema Cardiovascular")
for item in ["Coração (Átrios e Ventrículos)", "Válvulas Cardíacas", "Artérias e Veias", "Frequência e Ritmo Cardíaco"]:
    cardiovascular.adicionar_filho(No_arvore(item))

respiratorio = No_arvore("Sistema Respiratório")
for item in ["Cavidade Nasal e Seios Paranasais", "Faringe e Laringe", "Traqueia e Brônquios", "Pulmões e Alvéolos"]:
    respiratorio.adicionar_filho(No_arvore(item))

cardiorrespiratorio.adicionar_filho(cardiovascular)
cardiorrespiratorio.adicionar_filho(respiratorio)
paciente.adicionar_filho(cardiorrespiratorio)


digestorio = No_arvore(" 2. Sistema Digestório")
trato_superior = No_arvore("Trato Gastrointestinal Superior")
for item in ["Cavidade Oral (Dentes e Gengivas)", "Esôfago", "Estômago"]:
    trato_superior.adicionar_filho(No_arvore(item))

trato_inferior_anexos = No_arvore("Trato Inferior e Órgãos Anexos")
for item in ["Intestino Delgado", "Intestino Grosso e Reto", "Fígado e Vesícula Biliar", "Pâncreas"]:
    trato_inferior_anexos.adicionar_filho(No_arvore(item))

digestorio.adicionar_filho(trato_superior)
digestorio.adicionar_filho(trato_inferior_anexos)
paciente.adicionar_filho(digestorio)


urinario = No_arvore(" 3. Sistema Urinário")
for item in ["Rins", "Ureteres", "Bexiga Urinária", "Uretra"]:
    urinario.adicionar_filho(No_arvore(item))
paciente.adicionar_filho(urinario)


locomotor = No_arvore(" 4. Sistema Locomotor (Musculoesquelético)")
esqueletico = No_arvore("Sistema Esquelético")
for item in ["Crânio e Coluna Vertebral", "Membros Torácicos (Dianteiros)", "Membros Pélvicos (Traseiros)", "Articulações e Ligamentos"]:
    esqueletico.adicionar_filho(No_arvore(item))

muscular = No_arvore("Sistema Muscular")
for item in ["Musculatura Esquelética", "Tendões", "Tônus e Massa Muscular"]:
    muscular.adicionar_filho(No_arvore(item))

locomotor.adicionar_filho(esqueletico)
locomotor.adicionar_filho(muscular)
paciente.adicionar_filho(locomotor)


nervoso_sensorial = No_arvore(" 5. Sistema Nervoso e Sensorial")
nervoso = No_arvore("Sistema Nervoso")
for item in ["Encéfalo (Cérebro e Cerebelo)", "Medula Espinhal", "Nervos Periféricos e Reflexos"]:
    nervoso.adicionar_filho(No_arvore(item))

sensorial = No_arvore("Órgãos dos Sentidos")
for item in ["Olhos e Visão", "Orelhas e Audição / Equilíbrio"]:
    sensorial.adicionar_filho(No_arvore(item))

nervoso_sensorial.adicionar_filho(nervoso)
nervoso_sensorial.adicionar_filho(sensorial)
paciente.adicionar_filho(nervoso_sensorial)


endocrino_imune = No_arvore(" 6. Sistema Endócrino e Linfático")
endocrino = No_arvore("Sistema Endócrino")
for item in ["Tireoide e Paratireoides", "Glândulas Adrenais", "Pâncreas Endócrino"]:
    endocrino.adicionar_filho(No_arvore(item))

linfatico = No_arvore("Sistema Linfático e Imunológico")
for item in ["Linfonodos (Submandibulares, Poplíteos)", "Baço", "Medula Óssea"]:
    linfatico.adicionar_filho(No_arvore(item))

endocrino_imune.adicionar_filho(endocrino)
endocrino_imune.adicionar_filho(linfatico)
paciente.adicionar_filho(endocrino_imune)


tegumentar = No_arvore(" 7. Sistema Tegumentar (Pele e Anexos)")
for item in ["Epiderme e Derme", "Pelagem", "Glândulas Cutâneas e Subcutâneo", "Coxins Plantares e Unhas"]:
    tegumentar.adicionar_filho(No_arvore(item))
paciente.adicionar_filho(tegumentar)



