from fila import Fila
from lista_encadeada import Lista
from atendimento import atendimento_normal, atendimento_emergencia, Atendimento
from estoque import estoque
from prontuario import Prontuario
from pagamento import Pagamento
from datetime import datetime
from arvore import paciente
from random import choice 

prontuarios_abertos = Lista()
pagamentos_realizados = Lista()

def chegada_animal():
    animal = input('Digite o nome do animal a ser consultado: ')
    tutor = input('Digite o nome do tutor: ')
    queixa = input('Qual a queixa relatada pelo tutor: ')
    data_chegada = datetime.now()
    
    pet = Atendimento(animal, tutor , data_chegada, queixa)
    emergencia = input('O animal necessita de um atendimento de urgência?').strip().lower()
    if emergencia == 'sim':
        atendimento_emergencia.enfileirar(pet)
        print('Animal encaminhado para a emergência!')
    elif emergencia == 'não':
        atendimento_normal.enfileirar(pet)
        print('Animal encaminhado para a fila de atendimento normal!')
    else:
        print('Opção inválida! Digite sim ou não!')

numero_pr = 0
def abrir_prontuario():
    global numero_pr
    atendimento_atual = None
    if atendimento_emergencia.tamanho > 0:
        atendimento_atual = atendimento_emergencia.desenfileirar()
        print('Atendendo animal da fila de emergência!')
    elif atendimento_normal.tamanho > 0:
        atendimento_atual = atendimento_normal.desenfileirar()
        print('Atendendo animal da fila de atendimento normal!')
    else:
        print('Não há animais aguardando para serem atendidos nesse momento!')
        return

    animal_atendido = atendimento_atual.dado
    
    numero_pr += 1
    animal = input('Digite o nome do animal: ')
    tutor = input('Digite o nome do tutor: ')
    veterinario = input('Digite o nome do veterinário responsável pelo prontuário: ')
    data_abertura = datetime.now()
    medicamentos_utilizados = input('Digite os medicamentos e vacinas utilizados na consulta do animal: ')
    procedimentos_realizados = input('Digite os procedimentos realizados no animal: ')

    novo_pr = Prontuario(numero_pr, animal, tutor, veterinario, data_abertura, medicamentos_utilizados, procedimentos_realizados)
    print(f'Prontuário {numero_pr} aberto para o animal {animal}')
    prontuarios_abertos.adicionar(novo_pr) 

def realizar_diagnostico():
    print('Realizando diagnóstico do animal! ')
    paciente.realizar_diagnostico_recursivo()
    print(paciente)

def fechar_prontuario():
    numero = int(input('Digite o número do prontuario para encerrá-lo:'))
    prontuarios_abertos.deletar(numero)
    print('Prontuário encerrado! ')

def realizar_pagamento():
    
    prontuario = input('Digite o número do prontuário:')
    nome = input('Digite o nome do tutor: ')
    valor_medicamentos = float(input('Digite o valor dos medicamentos e vacinas utilizados no tratamento do animal: '))
    valor_procedimentos = float(input('Digite o valor dos procedimentos que foram realizados no animal: '))
    valor_total = valor_medicamentos + valor_procedimentos
    print(f'O valor total ficou R${valor_total:.2f}')

    forma = input('Digite a forma de pagamento (PIX, Dinheiro ou Cartão)').lower
    data_hora_pagamento = datetime.now()
    pagamento = Pagamento(prontuario, nome, valor_medicamentos, valor_procedimentos, valor_total, forma, data_hora_pagamento)
    
    if forma == 'PIX' or 'Dinheiro' or 'Cartão':
        pagamentos_realizados.adicionar(pagamento)
        print('Pagamento concluído com sucesso! ')
    else:
        print('Entrada Inválida! Digite uma das opções das formas de pagamento! ')

def adicionar_itens_estoque():
    item = input('Digite o nome do item que deseja adicionar ao estoque: ')
    codigo = input('Digite o código do item: ')
    fornecedor = input('Digite o nome do fornecedor: ')
    preco_compra = float(input('Digite o preço da compra do item: '))
    preco_venda = float(input('Digite o preço da venda do item: '))
    data_compra = datetime.now()
    data_validade = input('Digite a data de validade do item: ')
    quantidade = int(input('Digite a quantidade que deseja adicionar ao estoque: '))
    
    estoque.enfileirar(item)
    print(f'{item} adicionado ao estoque! ')

def remover_itens_estoque():
    item = input('Digite o nome do item que deseja dar baixa no estoque: ')
    estoque.desenfileirar()
    print(f'{item} dado baixa no estoque! ')