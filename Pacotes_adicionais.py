import os
import viagens_modulo_1 as viagem
from time import sleep

def addPacote ():    
    pacoteAdd = int(input('Qual Serviço deseja adicionar?\n[1]-Aluguel de Carros\n[2]-Seguro Viagem\n[3]-Passeios não inclusos no pacote\n[4]-Sair\n'))
    #OPIÇÃO 1
    if (pacoteAdd == 1): 
        os.system("cls")
        opcaocarro =  int(input('Acesse o site: https://www.localiza.com/?\nEsta informacao foi util ?\n[1]-Sim\n[2]-Não\n')) 
        if (opcaocarro == 1 or opcaocarro == 2):
            print('Obrigado por sua opinião\n')
            sleep(1)
            os.system("cls")
            if viagem.finalizar() == False:
              return False
        else:
            print('Insira uma opção válida!')
            sleep(1)
            os.system("cls")
            if addPacote() == False:
              return False
              
    #OPIÇÃO 2
    elif (pacoteAdd == 2):
        os.system("cls")
        opcaoSeguro = int(input('Acesse o site: https://assistentedeviagem.com.br/\nEsta informacao foi util ?\n[1]-Sim\n[2]-Não\n')) 
        if (opcaoSeguro == 1 or opcaoSeguro == 2):
            print('Obrigado por sua opinião\n')
            sleep(1)
            os.system("cls")
            if viagem.finalizar() == False:
              return False
        else:
            print('Insira uma opção válida!')
            sleep(1)
            os.system("cls")
            if addPacote() == False:
              return False
    #OPIÇÃO 3
    elif (pacoteAdd == 3):
        os.system("cls")
        #direcionar para o site ficticio
        opcaoPacotesA = int(input('Acesse o site: https://assistentedeviagem.com.br/\nEsta informacao foi util ?\n[1]-Sim\n[2]-Não\n')) 
        if (opcaoPacotesA == 1 or opcaoPacotesA == 2):
            print('Obrigado por sua opinião\n')
            sleep(1)
            os.system("cls")
            if viagem.finalizar() == False:
              return False
        else:
            print('Insira uma opção válida!')
            sleep(1)
            os.system("cls")
            if addPacote() == False:
              return False
    #OPIÇÃO 4
    elif (pacoteAdd == 4):
            print('Obrigado pelo contato\n')
            sleep(1)
            os.system("cls")
            if viagem.finalizar() == False:
              return False
    #tratativa de erros de pacoteAdd
    else:
         print('Insira uma opção válida!')
         sleep(1)
         os.system("cls")
         if addPacote() == False:
            return False