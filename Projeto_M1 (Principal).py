import os
from time import sleep
import viagens_modulo_1 as viagens
from Informacoes_modulo_1 import informacao
from Duvidas_modulo_1 import duvidas
from Pacotes_adicionais_modulo_1 import addPacote

loop = True
while loop == True:
    sleep(1/2)
    os.system('cls')
    opcao = int(input('Olá! seja bem vindo(a) a Revi, onde seus sonhos são os nossos sonhos!\n\nSelecione o tipo de atendimento desejado:\n[1] Dúvidas frequentes\n[2] Consultar as próximas viagens disponíveis\n[3] Informações\n[4] Pacotes adicionais\n[5] Sair\n'))
    sleep(1/2)
    if opcao == 1:
        os.system('cls')
        duvidas()  # Laura
        if viagens.finalizar() == False: 
            print('Atendimento cancelado.')
            sleep(1)
            loop = False
    elif opcao == 2:
        os.system('cls')
        if viagens.consulta() == False: # Lucas
            print('Atendimento cancelado.')
            sleep(1)
            loop = False
    elif opcao == 3:
        os.system('cls')
        informacao()  # Amanda
        if viagens.finalizar() == False: 
            print('Atendimento cancelado.')
            sleep(1)
            loop = False
    elif opcao == 4:
        os.system('cls')
        if addPacote() == False:  #Elizangela
            print('Atendimento cancelado.')
            sleep(1)
            loop = False
    elif opcao == 5:
        print('Muito obrigado por entrar em contato!')
        loop = False
    else:
        print('Opção indisponível, por favor, selecione uma das opções acima.')