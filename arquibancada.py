######################################################################################################################################################
# Cores
# \033[style; text; back m
NCinza = "\033[1;30;1m"
NVermelho = "\033[1;31;1m"
NVerde = "\033[1;32;1m"
NAmarelo = "\033[1;33;1m"
NMagenta = "\033[1;34;1m"
NRosa = "\033[1;35;1m"
NCiano = "\033[1;36;1m"
NBranco = "\033[1;37;1m"
Corfim = "\033[m"

######################################################################################################################################################

def arquibancada():
    setor_2_11 = ('Setor 2', 'Setor 3', 'Setor 4', 'Setor 5', 'Setor 10', 'Setor 11')
    setor_6_8 = ('Setor 6', 'Setor 7', 'Setor 8')
    setores = list(setor_2_11[0:4]) + list(setor_6_8) + list(setor_2_11[4:6])

    def exibir_opcoes(opcoes):
        print (f"\n{NAmarelo}Opções disponiveis:{Corfim}")
        for i, opcao in enumerate(opcoes, 1):
            print(f"{i}. {opcao}")

    # Exiba as opções numeradas ao usuário
    exibir_opcoes(setores)

    # Função que retorna a opção do usuário
    def escolher_setores(opcoes):
        while True:
            try:
                opcao = int(input(f"\n{NVerde}Digite a opção desejada: {Corfim}"))
                if opcao < 1 or opcao > len(opcoes):
                    print(f"{NVermelho}Opção fora do intervalo. Digite uma opção válida.{Corfim}")
                else:
                    return opcao  # Retorna a opção como um número válido
            except ValueError:
                print(f"{NVermelho}Opção inválida. Digite um número válido.{Corfim}")

    opcao_escolhida_setor = escolher_setores(setores)
    print(f"\nVocê escolheu a opção: {setores[opcao_escolhida_setor - 1]}") # Menos 1, pois os elementos dentro da tupla começam em 0

    ingressos = ('Meia entrada', 'Inteira')

    # Exiba as opções numeradas ao usuário
    exibir_opcoes(ingressos)

    # Função que retorna a opção do usuário
    def escolher_ingressos(ingressos):
        while True:
            try:
                opcao = int(input(f"\n{NVerde}Digite a opção desejada: {Corfim}"))
                if opcao < 1 or opcao > len(ingressos):
                    print(f"{NVermelho}Opção fora do intervalo. Digite uma opção válida.{Corfim}")
                else:
                    return opcao  # Retorna a opção como um número válido
            except ValueError:
                print(f"{NVermelho}Opção inválida. Digite um número válido.{Corfim}")

    opcao_escolhida_ingresso = escolher_ingressos(ingressos)
    print(f"\nVocê escolheu a opção: {ingressos[opcao_escolhida_ingresso - 1]}") # Menos 1, pois os elementos dentro da tupla começam em 0

    dias = ('Domingo', 'Segunda', 'Sábado')

    # Exiba as opções numeradas ao usuário
    exibir_opcoes(dias)

    # Função que retorna a opção do usuário
    def escolher_dia(dias):
        while True:
            try:
                opcao = int(input(f"\n{NVerde}Digite a opção desejada: {Corfim}"))
                if opcao < 1 or opcao > len(dias):
                    print(f"{NVermelho}Opção fora do intervalo. Digite uma opção válida.{Corfim}")
                else:
                    return opcao  # Retorna a opção como um número válido
            except ValueError:
                print(f"{NVermelho}Opção inválida. Digite um número válido.{Corfim}")

    opcao_escolhida_dia = escolher_dia(dias)

    setor_escolhido = setores[opcao_escolhida_setor - 1] # Menos 1, pois os elementos dentro da tupla começam em 0
    ingresso_escolhido = ingressos[opcao_escolhida_ingresso - 1] # Menos 1, pois os elementos dentro da tupla começam em 0
    dia_escolhido = dias[opcao_escolhida_dia - 1]
    # A partir do setor escolhido, determine a faixa de preços
    if setor_escolhido in setor_2_11 and (dia_escolhido == 'Domingo' or dia_escolhido == 'Segunda'):
        preco_meia, preco_inteira = (125.00, 250.00)
    elif setor_escolhido in setor_6_8 and (dia_escolhido == 'Domingo' or dia_escolhido == 'Segunda'):
        preco_meia, preco_inteira = (150.00, 300.00)
    elif setor_escolhido in setor_2_11 and (dia_escolhido == 'Sabado'):
        preco_meia, preco_inteira = (85.00, 170.00) 
    else:
        preco_meia, preco_inteira = (100.00, 200.00) 

    preco_final = preco_meia if ingresso_escolhido == 'Meia entrada' else preco_inteira

    print(f"\nVocê escolheu o setor: {setor_escolhido}")
    print(f"Você escolheu o ingresso: {ingresso_escolhido}")
    print(f"Você escolheu o dia: {dia_escolhido}")
    print(f"{NCiano}O preço total é: R${preco_final:.2f}\n{Corfim}")
    
arquibancada()
