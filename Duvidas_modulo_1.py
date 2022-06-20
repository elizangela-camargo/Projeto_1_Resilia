from time import sleep
def duvidas():
        print('\n[1] Hospedagem? \n[2] Viagem? \n[3] Sair\n')
        opcao = int(input('Digite qual tipo da sua duvida :  '))
        if opcao == 1:
            print('\n[1] Qual meu hotel e quarto ?\n[2] Qual valor da diária?\n[3]Como cancelar minha hospedagem ?\n[4]Voltar ao Menu inicial\n')
            opcao = int(input('Digite a opção que representa sua dúvida :  '))
            if opcao == 1 :
                site = 'https://suaviagemresilia.com/reserva/'
                print(f'\nFaça seu login em {site}, em seu perfil encontrara o hotel e quarto escolhidos\n' )
            elif opcao == 2:
                site = 'https://suaviagemresilia.com/reserva/diária'
                print(f'\nFaça seu login em {site}, em seu perfil encontrara o valor da diária\n' )
            elif opcao == 3:
                site = 'https://suaviagemresilia.com/reserva/cancelamento'
                print(f'\nFaça seu login em {site}, em seu perfil encontrara a opçao de cancelamento\n' )
            else:
                return False
            sleep(1/2)
        elif opcao == 2:
            print('\n[1] Qual horário do meu voo ?\n[2] Como reservar uma passagem aerea?\n[3]Posso transportar animais ?\n[4]Voltar ao Menu inicial\n')
            opcao = int(input('Digite a opção que representa sua dúvida :  '))
            if opcao == 1 :
                site = 'https://suaviagemresilia.com/horário/'
                print(f'\nFaça seu login em {site}, em seu perfil encontrara o horário de seu voo\n' )
            elif opcao == 2:
                site = 'https://suaviagemresilia.com/passagem/'
                print(f'\nAtravés de nosso site: {site}, encontrara varias opções e seus respectivos valores\n' )
            elif opcao == 3:
                site = 'https://suaviagemresilia.com/reserva/cancelamento'
                print(f'O transporte de animais domésticos, tais como cachorros e gatos, deve autorizá-lo a companhia aérea. Consulte as condições da companhia no ato da reserva\n' )
            else:
                return False