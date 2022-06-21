import os
from time import sleep

def finalizar(): # Função responsável por parar o programa / finalizar atendimento
    resetar = int(input('Selecione:\n[1] Resetar o atendimento\n[2] Finalizar o atendimento\n'))
    if resetar == 1:
        return True
    elif resetar == 2:
        return False
    else:
        print('Insira uma opção válida!')
        sleep(1/2)
        if finalizar() == False:
            return False

def consulta(): # Função referente a opção [2] Consultar as próximas viagens disponíveis

    nacionalidade = int(input('Que tipo de viagem você deseja realizar?\n[1] Nacional\n[2] Internacional \n[3] Sair\n'))
    if nacionalidade == 3:
        return False
    sleep(1/2)
    tempo = int(input('Quando você deseja realizar a viagem?\n[1] Dentro de 6 meses\n[2] Dentro de 1 ano\n[3] Mais de 1 ano \n[4] Sair\n'))
    os.system('cls')
    if tempo == 4:
        return False
    sleep(1/2)

    # Bloco1 - Nesse bloco condicional ele checa se a opção de viagem escolhida é nacional ou internacional.
    if nacionalidade == 1: 

            #Bloco2.1 - Nesse bloco condicional ele checa se o tempo da viagem (NACIONAL) escolhido, é dentro de 6 meses, dentro 1 ano ou mais de um ano e oferece as opções disponíveis.            
        if tempo == 1:
            nacional_6 = int(input('Próximas viagens nacionais disponíveis dentro de 6 meses: \n\n[1] Porto de Galinhas - Pernambuco ---------- R$999\n[2] Foz do Iguaçu - Paraná ------------------ R$849\n'))
            #Bloco 3.1 - Nesse bloco, ele oferece informações sobre o pacote escolhido
            if nacional_6 == 1:
                print('o pacote Porto de Galinhas - Pernambuco vem incluso Hospedagem, Café da manhã e a passagem aérea, o preço é individual e referente a 3 diárias, podendo ser aumentada para 5 ou 7.\n')
                fim = finalizar()  # Bloco 4 - Nesse bloco, ele checa se o usuário quer finalizar o programa, caso a resposta seja positiva, ele encerra o atendimento.
                if fim == False: 
                    return False
            
            elif nacional_6 == 2:
                print('o pacote Foz do Iguaçu - Paraná vem incluso Hospedagem, Café da manhã e a passagem aérea, o preço é individual e referente a 3 diárias, podendo ser aumentada para 5 ou 7.\n')
                fim = finalizar()
                if fim == False:
                    return False
            else:
                print('Por favor, selecione um pacote válido!')

            # A partir daqui, o processo se repete a partir do Bloco 2.1, mudando apenas as informações.
        elif tempo == 2:
            nacional_12 = int(input('Próximas viagens nacionais disponíveis dentro de 1 ano: \n\n[1] Chapada dos Guimarães - Mato Grosso --- R$659\n[2] Beto Carrero World - Santa Catarina --- R$769\n[3] Recife - Pernambuco ------------------- R$399\n'))

            if nacional_12 == 1:
                print('O pacote Chapada dos guimarães - Mato Grosso vem incluso hospedagem, café da manhã, Aluguel de carro e a Passagem aérea, o preço é individual e referente a 3 diárias, podendo ser aumentada para 5 ou 7.\n')
                fim = finalizar()
                if fim == False:
                    return False

            elif nacional_12 == 2:
                print('O pacote Beto Carrero World - Santa Catarina vem incluso hospedagem, café da manhã, ingresso para 1 dia de parque e a Passagem aérea, o preço é individual e referente a 3 diárias, podendo ser aumentada para 5 ou 7.\n')
                fim = finalizar()
                if fim == False:
                    return False

            elif nacional_12 == 3:
                print('O pacote Recife - Pernambuco vem incluso hospedagem, café da manhã e a Passagem aérea, o preço é individual e referente a 3 diárias, podendo ser aumentada para 5 ou 7.\n')
                fim = finalizar()
                if fim == False:
                    return False
            else:
                print('Por favor, selecione um pacote válido!')

           
        elif tempo == 3:

            nacional_12mais = int(input('Próximas viagens nacionais disponíveis para mais de 1 ano: \n\n[1] Jericoacoara + Fortaleza - Ceará ------- R$799\n'))

            if nacional_12mais == 1:
                print('O pacote Jericoacoara + Fortaleza - Ceará vem incluso hospedagem, café da manhã,  e a Passagem aérea, o preço é individual e referente a 5 diárias, podendo ser aumentada para 7.\n')
                fim = finalizar()
                if fim == False:
                    return False

            
        else:
            print('Por favor, selecione uma data válida!')
            consulta()


    elif nacionalidade == 2:

        if tempo == 1:
            internacional_6 = int(input('Próximas viagens internacionais disponíveis dentro de 6 meses:\n\n[1] Madrid + Barcelona - Espanha ------ R$5939\n[2] Toronto - Canadá ------------------ R$5539 '))

            if internacional_6 == 1:
                print('O pacote Madri + Barcelona vem incluso hospedagem e a passagem aérea, o preço é individual e referente a 8 diárias.\n')
                fim = finalizar()
                if fim == False:
                    return False

            elif internacional_6 == 2:
                print('O pacote Toronto - Canadá vem incluso hospedagem e a passagem aérea, o preço é individual e referente a 5 diárias, podendo ser aumentada para 7 ou 9.\n')
                fim = finalizar()
                if fim == False:
                    return False
            else:
                print('Por favor, selecione um pacote válido!')

        elif tempo == 2:

            internacional_12 = int(input('Próximas viagens internacionais disponíveis dentro de 1 ano:\n\n[1] Japão - Tóquio ------------------ R$3849 \n[2] Orlando - Estados Unidos -------- R$2889 \n[3] Atenas + Santorini - Grécia ----- R$3599\n'))

            if internacional_12 == 1:
                print('O pacote Japão - Tóquio vem incluso hospedagem e passagem aérea, o preço é individual e referente a 7 diárias, podendo ser aumentada para 10.\n')
                fim = finalizar()
                if fim == False:
                    return False

            elif internacional_12 == 2:
                print('O pacote Orlando - Estados Unidos vem incluso hospedagem e passagem aérea, o preço é individual e referente a 7 diárias, podendo ser aumentada para 14.\n')
                fim = finalizar()
                if fim == False:
                    return False

            elif internacional_12 == 3:
                print('essa é a opção 3 inter 1a\n')
                fim = finalizar()
                if fim == False:
                    return False
            else:
                print('Por favor, selecione um pacote válido!')

        elif tempo == 3:

            internacional_12mais = int(input('Próximas viagens internacionais disponíveis para mais de 1 ano: \n\n[1] Las Vegas - Estados Unidos -------- R$2749\n'))

            if internacional_12mais == 1:
                print('O pacote Las Vegas - Estados Unidos vem incluso hospedagem e passagem aérea, o preço é individual e referente a 5 diárias, podendo ser aumentada para 7.\n')
                fim = finalizar()
                if fim == False:
                    return False
            else:
                print('Por favor, selecione um pacote válido!')

        else:
            print('Por favor, selecione uma data válida!')
            consulta()

    else:
        print('Opção de viagem não disponível, por favor, escolha outra!')
        sleep(1/2)
        consulta()
