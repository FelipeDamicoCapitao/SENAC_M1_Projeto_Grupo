# ###########################################################################################################
NCinza = "\033[1;30;1m"
NVermelho = "\033[1;31;1m"
NVerde = "\033[1;32;1m"
NAmarelo = "\033[1;33;1m"
NMagenta = "\033[1;34;1m"
NRosa = "\033[1;35;1m"
NCiano = "\033[1;36;1m"
NBranco = "\033[1;37;1m"
Corfim = "\033[m"

# ###########################################################################################################
from B1_separacao import sep
from B1_separacao import sep2
from B1_separacao import sep3

# ###########################################################################################################


def desfiles1():
    X = "Ordem de Desfile"
    sep(X)

#Domingo
    X = " Domingo - 11/02/2024"
    sep2(X)

    print (f"{NBranco}1- Unidos do Porto da Pedra{Corfim} {NCinza}[C]{Corfim}")
    print (f"{NBranco}2- Beija-Flor de Nilópolis{Corfim} {NCinza}[B]{Corfim}")
    print (f"{NBranco}3- Acadêmicos do Salgueiro{Corfim} {NCinza}[C]{Corfim}")
    print (f"{NBranco}4- Acadêmicos do Grande Rio{Corfim} {NCinza}[B]{Corfim}")
    print (f"{NBranco}5- Unidos da Tijuca{Corfim} {NCinza}[C]{Corfim}")
    print (f"{NBranco}6- Imperatriz Leopoldinense{Corfim} {NCinza}[B]{Corfim}")

#Segunda
    X =" Segunda - 12/02/2024"
    sep2(X)

    print (f"{NBranco}1- Mocidade Independente{Corfim} {NCinza}[C]{Corfim}")
    print (f"{NBranco}2- Portela{Corfim} {NCinza}[B]{Corfim}")
    print (f"{NBranco}3- Unidos de Vila Isabel{Corfim} {NCinza}[C]{Corfim}")
    print (f"{NBranco}4- Estação Primeira de Mangueira{Corfim} {NCinza}[B]{Corfim}")
    print (f"{NBranco}5- Paraíso do Tuiuti{Corfim} {NCinza}[C]{Corfim}")
    print (f"{NBranco}6- Unidos do Viradouro{Corfim} {NCinza}[B]{Corfim}")

#Observações
    X =f"{NCinza}Concentração:\n [C] - Correios\n [B] - Balança{Corfim}"

    sep2(X)

