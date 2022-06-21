import os
from time import sleep
def duvidas():
        print('\nSobre o que é a dúvida: \n[1] Hospedagem? \n[2] Viagem? \n[3] Sair\n')
        opcao = int(input('Digite qual tipo da sua duvida :  '))
        if opcao == 1:
            os.system('cls')
            print('\nDúvidas frequentes sobre hospedagem: \n[1] Qual meu hotel e quarto ?\n[2] Qual valor da diária?\n[3] Como cancelar minha hospedagem ?\n[4] Voltar ao Menu inicial\n')
            opcao = int(input('Digite a opção que representa sua dúvida :  '))
            if opcao == 1 :
                site = 'https://revi.com/reserva/'
                print(f'\nFaça seu login em {site}, em seu perfil encontrará o hotel e quarto escolhidos\n' )
            elif opcao == 2:
                site = 'https://revi.com/reserva/diária'
                print(f'\nFaça seu login em {site}, em seu perfil encontrará o valor da diária\n' )
            elif opcao == 3:
                site = 'https://revi.com/reserva/cancelamento'
                print(f'\nFaça seu login em {site}, em seu perfil encontrará a opçao de cancelamento\n' )
            else:
                return False
            sleep(1/2)
        elif opcao == 2:
            os.system('cls')
            print('\nDúvidas frequentes sobre a viagem: \n[1] Qual horário do meu voo ?\n[2] Como reservar uma passagem aerea?\n[3] Posso transportar animais ?\n[4] Voltar ao Menu inicial\n')
            opcao = int(input('Digite a opção que representa sua dúvida :  '))
            if opcao == 1 :
                site = 'https://revi.com/horário/'
                print(f'\nFaça seu login em {site}, em seu perfil encontrará o horário de seu voo\n' )
            elif opcao == 2:
                site = 'https://revi.com/passagem/'
                print(f'\nAtravés de nosso site: {site}, encontrará varias opções e seus respectivos valores\n' )
            elif opcao == 3:
                site = 'https://revi.com/reserva/cancelamento'
                print(f'O transporte de animais domésticos, tais como cachorros e gatos, deve autorizá-lo a companhia aérea. Consulte as condições da companhia no ato da reserva\n' )
            else:
                return False