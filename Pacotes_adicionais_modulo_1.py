import os
import viagens_modulo_1 as viagem
from time import sleep

def addPacote ():    
  pacoteAdd = int(input('Qual Serviço deseja adicionar?\n[1]-Aluguel de Carros\n[2]-Seguro Viagem\n[3]-Passeios não inclusos no pacote\n[4]-Sair\n'))
  #OPIÇÃO 1
  if (pacoteAdd == 1): 
    print ('Com mais de 400 agências, uma das maiores frota de carros do Brasil.\n Faça sua reserva!')
    opcaocarro =  int(input('Para mais informações acesse o site: https://www.revi.com/alugueis?\nEsta informacao foi util ?\n[1]-Sim\n[2]-Não\n')) 
    if (opcaocarro == 1 or opcaocarro == 2):
      print('Obrigado por sua opinião\n')
      sleep(1)
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
    print ('No Brasil, os planos de Seguro Viagem são regulamentados e supervisionados pela SUSEP - Superitendencia de Seguros Privados\n O seguro de viagem é disponibilizado sob a forma de apólices ou bilhetes e pode ser contratado no momento da reserva de um pacote de viagem para cobrir exatamente a duração dessa viagem\n')
    opcaoSeguro = int(input('Para mais informações acesse o site: https://revi.com/seguros\nEsta informacao foi util ?\n[1]-Sim\n[2]-Não\n')) 
    if (opcaoSeguro == 1 or opcaoSeguro == 2):
      print('Obrigado por sua opinião\n')
      sleep(1)
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
    #direcionar para o site ficticio
    print ('Com diversos serviços adcionais, para incrementar o seu pacote, veja nossa lista e escolha o serviço para tonar sua viagem ainda mais inesquecíves')
    opcaoPacotesA = int(input('Para mais informações acesse o site: https://revi.com/passeios-adicionais\nEsta informacao foi util ?\n[1]-Sim\n[2]-Não\n')) 
    if (opcaoPacotesA == 1 or opcaoPacotesA == 2):
      print('Obrigado por sua opinião\n')
      sleep(1)
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
    if viagem.finalizar() == False:
      return False
  #tratativa de erros de pacoteAdd
  else:
    print('Insira uma opção válida!')
    sleep(1)
    os.system("cls")
    if addPacote() == False:
      return False
