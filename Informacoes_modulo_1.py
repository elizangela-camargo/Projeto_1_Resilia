# OPÇÃO DE ESCOLHA PARA COD DE VIAGEM. 
def informacao():
    print('-'*30)
    print('Informações adicionais')
    print('-'*30)
    print()
    print('[1] - Check-in \n[2] - Bagagem \n[3] - Reembolso e Cancelamento \n[4] - SAIR\n')


    resposta=int(input('ESCOLHA A SUA OPÇÃO: '))

    if resposta == 1:
        print("""Você pode realizar o web check-in 48 horas antes do seu voo. Para isso, basta seguir estes passos:
        1-Acesse o site da companhia aérea.
        2-Escolha a opção “check-in” ou “check-in online”.
        3-A companhia aérea solicitará seu sobrenome e o código de web check-in* que enviamos anteriormente para o seu e-mail.""")
    elif resposta==2:
        print("""A bagagem e despachada no momento do check-in e levada para o porão da aeronave. A bagagem despachada possui algumas regras:
        -Peso: 23kg
        -Altura: 50cm
        -Largura:80cm
        -Profundidade: 28cm
        Lembrando que as companhias Áerea tem o direito de recusar qualquer bagagem ou carga que coloque risco a segurança do voo. Se atente as regras
        para não ocorrer nenhum contratempo.""")
    elif resposta ==3:
        print(""" Fazer um cancelamento pode ter custo adicional
        -Você pode solicitar o cancelamento gratuito de seu voo se o fizer dentro de 24h após receber o comprovante de pagamento
        -Caso sua reserva seja cancelada, o reembolso será feito da mesma forma que de pagamento que foi usado para comprar
        -Se você não pode viajar por causa de uma doença grave, morte ou outra razão de força maior, deverá enviar seus documentos particulares a companhia áerea.""")
    else:
        print('SAIR')
        return False
        