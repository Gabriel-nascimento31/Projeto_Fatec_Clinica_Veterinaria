import clinica

while True:
    print('Clinica Veterinária ')
    print('1 - Inserir animal para atendimento')
    print('2 - Abrir prontuário')
    print('3 - Realizar o diagnóstico do animal')
    print('4 - Fechar o prontuário')
    print('5 - Realizar o pagamento')
    print('6 - Adicionar itens ao estoque')
    print('7 - Remover itens do estoque')
    print('8 - Encerrar o sistema')

    usuario = int(input('Digite a opção que deseja realizar: '))

    if usuario == 1:
        clinica.chegada_animal()
    
    elif usuario == 2:
        clinica.abrir_prontuario()
    
    elif usuario == 3:
        clinica.realizar_diagnostico()
    
    elif usuario == 4:
        clinica.fechar_prontuario()
    
    elif usuario == 5:
        clinica.realizar_pagamento()
    
    elif usuario == 6:
        clinica.adicionar_itens_estoque()
    
    elif usuario == 7:
        clinica.remover_itens_estoque()
    
    elif usuario == 8:
        print('Sistema encerrado! ')
        break
    
    else:
        print('Opção inválida! ')