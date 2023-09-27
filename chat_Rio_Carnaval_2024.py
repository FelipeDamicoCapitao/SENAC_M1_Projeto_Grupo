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

# ######################################################################################################################################################
# Importa Função Cabeçalho de separação

from B1_separacao import sep
from B1_separacao import sep2
from B1_separacao import sep3


# ###########################################################################################################
#Função Menu Inicial      
def menu():
    X ="Menu Inicial"
    sep(X)
    print( f"{NAmarelo}Selecione a opção de atendimento:{Corfim}\n")
    print( "1 - Ingressos")
    print( "2 - Ordem de Desfile")
    print( "3 - Ensaios Técnicos")
    print( "4 - Dúvidas Frequentes")
    print( "5 - Sair\n")
    
    X0 = (input(f"{NVerde}Qual a opção desejada?{Corfim}"))
    
    #Opção 1
    if X0 == "1":
        ingresso() 
                 
    #Opção 2
    elif X0 == "2":
        desfile() #Função nao configurada
  
    #Opção 3    
    elif X0 == "3":
        ensaios() #Função nao configurada

    #Opção 4    
    elif X0 == "4": 
        duvidas() #Função nao configurada

    #Opção 5    
    elif X0 == "5": #Sair
        sair()

    #Opção - Divergentes
    else:
        print( f"{NVermelho}Digito Errado, digite novamente{Corfim}")
        menu()

# ###########################################################################################################
#Função opção 1 - Ingressos
def ingresso():

    X ="Ingressos"
    sep(X)

    print( f"{NAmarelo}Selecione a opção de atendimento:{Corfim}\n")
    print( "1 - Arquibancadas")
    print( "2 - Frisas")
    print( "3 - Retornar ao menu principal")
    print( "4 - Sair\n")
    X1 = (input(f"{NVerde}qual a opção desejada?{Corfim}"))

        #Opção 1
    if X1 == "1":
        arquibancada() 
                 
    #Opção 2
    elif X1 == "2":
        frisa() 
  
    #Opção 3    
    elif X1 == "3":
        menu()

    #Opção 4    
    elif X1 == "4": #Sair
        sair()

    #Opção - Divergentes
    else:
        print( f"{NVermelho}Digito Errado, digite novamente{Corfim}")
        ingresso()
# ###########################################################################################################
#Função opção 1.1 - Arquibancada
def arquibancada():
    X ="Ingressos de Arquibancada"
    sep(X)

    from A1_1_arquibancada import arquibancada1

    arquibancada1()
    
#DEfinição
    fimingresso()

# ###########################################################################################################
#Função opção 1.2 - Frisa
def frisa():
    X ="Ingressos de Frisa"
    sep(X)

    from A1_2_frisa import frisa1

    frisa1()

#DEfinição
    fimingresso()

# ###########################################################################################################
#Função opção 2 - Ordem de desfile
def desfile():

    from A2_ordem_de_desfile import desfiles1

    desfiles1()

    #DEfinição
    fim()

# ###########################################################################################################
#Função opção 3 - Ensaios Técnicos
def ensaios():

    from A3_ensaio_tecnico import ensaios1

    ensaios1()

#DEfinição
    fim()

# ###########################################################################################################
#Função opção 4 - Duvidas Frequentes
def duvidas():

    from A4_duvidas_frequentes import duvidas1

    duvidas1()

#DEfinição
    fimduvidas()


# ######################################################################################################################################################
# Função Pergunta em Caso de Erro e fim - Geral (Menu + Sair)
def fim():
    sep3()
    print( f"{NAmarelo}\nSelecione a opção de atendimento:{Corfim}\n")
    print( "1 - Retornar ao menu principal")
    print( "2 - Sair\n")
    X12 = (input(f"{NVerde}Qual a opção desejada?{Corfim}"))

    #Opção 3    
    if X12 == "1":
        menu()

    #Opção 4    
    elif X12 == "2": #Sair
        sair()

    #Opção - Divergentes
    else:
        print( f"{NVermelho}Digito Errado, digite novamente{Corfim}")
        fim()

# Função Pergunta final - ingresso + Geral
def fimingresso():
    sep3()
    print( f"{NAmarelo}\nSelecione a opção de atendimento:{Corfim}\n")
    print( "1 - Retornar ao menu de Ingressos")
    print( "2 - Retornar ao menu principal")
    print( "3 - Sair\n")
    X12 = (input(f"{NVerde}Qual a opção desejada?{Corfim}"))

    #Opção 1    
    if X12 == "1":
        ingresso()
    #Opção 2  
    elif X12 == "2": 
        menu()
    #Opção 4    
    elif X12 == "3": #Sair
        sair()

    #Opção - Divergentes
    else:
        print( f"{NVermelho}Digito Errado, digite novamente{Corfim}")
        fimingresso()

# Função Pergunta final - Duvidas = Geral
def fimduvidas():
    sep3()
    print( f"{NAmarelo}\nSelecione a opção de atendimento:{Corfim}\n")
    print( "1 - Retornar ao menu de dúvidas frequentes")
    print( "2 - Retornar ao menu principal")
    print( "3 - Sair\n")
    X12 = (input(f"{NVerde}Qual a opção desejada?{Corfim}"))

    #Opção 1    
    if X12 == "1":
        duvidas()
    #Opção 2  
    elif X12 == "2": 
        menu()
    #Opção 4    
    elif X12 == "3": #Sair
        sair()

    #Opção - Divergentes
    else:
        print( f"{NVermelho}Digito Errado, digite novamente{Corfim}")
        fimduvidas()

# ######################################################################################################################################################
# Função Sair - Agredecimento e fim de programa
def sair():
    X = f"Obrigado, nos vemos na Sapucai em 2024"
    L = 80

    Y = int(((L-len(X)))/2)
    Y2 = (" "*Y)
    print("")
    print(f"{NAmarelo}="*L)
    print(f"{Y2}{X}")
    print(f"="*L)
    print(f"{Corfim}")


# ######################################################################################################################################################
# executar programa
X = "Chat Rio Carnaval 2024"
sep(X)
X = "Sejam bem-vindos ao maior espetáculo da terra."
L = 80

Y = int(((L-len(X)))/2)
Y2 = (" "*Y)
print(f"{Y2}{NCiano}{X}{Corfim}")

menu()



    
    
    