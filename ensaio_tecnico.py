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

from separacao import sep
from separacao import sep2
from separacao import sep3

# ###########################################################################################################


def ensaio():
    X = "Ensaios Técnicos"
    sep(X)

#dia 1
    X = "07 de janeiro - Domingo"

    sep2(X)

    print (f"{NBranco}Porto da Pedra{Corfim} {NCinza}(B) - 20h30{Corfim}")
    print (f"{NBranco}Mocidade{Corfim} {NCinza}(C) - 22h{Corfim}")

#dia 2
    X = "14 de janeiro - Domingo"

    sep2(X)

    print (f"{NBranco}Portela{Corfim} {NCinza}(B) - 20h30{Corfim}")
    print (f"{NBranco}Unidos da Tijuca{Corfim} {NCinza}(C) - 22h{Corfim}")
    
#dia 3
    X = "21 de janeiro - Domingo"

    sep2(X)

    print (f"{NBranco}Paraíso do Tuiuti{Corfim} {NCinza}(C) - 20h30{Corfim}")
    print (f"{NBranco}Salgueiro{Corfim} {NCinza}(B) - 22h{Corfim}")

#dia 4
    X = "28 de janeiro - Domingo"
    sep2(X)

    print (f"{NBranco}Grande Rio{Corfim} {NCinza}(C) - 20h30{Corfim}")
    print (f"{NBranco}Mangueira{Corfim} {NCinza}(B) - 22h{Corfim}")

#dia 5
    X = "03 de fevereiro - Sábado"

    sep2(X)

    print (f"{NBranco}Beija-Flor{Corfim} {NCinza}(B) - 20h30{Corfim}")
    print (f"{NBranco}Vila Isabel{Corfim} {NCinza}(C) - 22h{Corfim}")

#dia 6
    X = "04 de feverero - Domingo"

    sep2(X)

    print (f"{NBranco}Viradouro{Corfim} {NCinza}(C) - 20h30{Corfim}")
    print (f"{NBranco}Imperatriz{Corfim} {NCinza}(B) - 22h{Corfim}")

#Observações
    X ="Concentração:\n [C] - Correios\n [B] - Balança"
    X = f"{NCinza}{X}{Corfim}"
    sep2(X)

ensaio()