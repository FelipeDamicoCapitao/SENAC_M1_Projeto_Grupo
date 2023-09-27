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

# ###########################################################################################################

from B1_separacao import sep
from B1_separacao import sep2
from B1_separacao import sep3

######################################################################################################################################################

def frisa():
    dias = ("Domingo", "Segunda-feira", "Sábado das campeãns")

    def diasprint():
        print(f"{NAmarelo}\nDias de Desfile:{Corfim}")
        for i, valor in enumerate(dias):
            print (i+1,"-",valor)
    
    def dia():
        while True:
            diasprint()
            D1 = (input(f"{NVerde}\nSelecione o dia da desfile desejado:{Corfim}"))
            try:
                D1 = int(D1)
                if D1<=0 or D1>=4:
                    print( f"{NVermelho}Digito do dia de desfile errado, digite novamente{Corfim}")

                else:
                    return D1
                
            except:
                print( f"{NVermelho}Digito do dia de desfile errado, digite novamente{Corfim}")
                
                
    D1 = dia()

######################################################################################################################################################

    Setores_disp= ["Setor 2","Setor 3","Setor 4","Setor 5","Setor 6","Setor 7","Setor 8","Setor 9","Setor 10","Setor 11","Setor 12","Setor 13"]

    def setoresprint():
        print(f"{NAmarelo}\nSetores Disponiveis:{Corfim}")
        for i, valor in enumerate(Setores_disp):
            print (i+2,"-",valor)

    def setor():
        while True:
            setoresprint()
            S1 = (input(f"{NVerde}\nSelecione o setor preferido:{Corfim}"))

            try:
                S1 = int(S1)
                if S1<2 or S1>13:
                    print( f"{NVermelho}Digito do setor errado, digite novamente{Corfim}")
                else:
                    return S1
            except:
                print( f"{NVermelho}Digito do setor errado, digite novamente{Corfim}")
    
    S1 = setor()

######################################################################################################################################################

    sep3()

    print(f"{NAmarelo}\nO Setor Escolhido foi o {Setores_disp[S1-2]} no(a) {dias[D1-1]}{Corfim}")
    print("Valores:")

    if D1 >=1 and D1 <= 2:
        if (S1 >=2 and S1 <=7) or (S1 >=10 and S1<=11):
            print("Fila A - R$ 7500,00")
            print("Fila B,C e D - R$ 5000,00")

        elif S1 == 8 or S1 == 9:
            print("Fila A - R$ 8000,00")
            print("Fila B,C e D - R$6100,00")
    
        elif S1 == 12:
            print("Fila A - R$2750,00")
            print("Fila B - R$1875,00")
    
        elif S1 == 13:
            print("Fila A - R$2750,00")
            print("Fila B - R$1875,00")
            print("Fila C, D, E e F - R$1375,00")
    

    elif D1==3:
        if (S1 >=2 and S1 <=7) or (S1 >=10 and S1<=11):
            print("Fila A - R$ 5200,00" )
            print("Fila B,C e D - R$3500,00")

        elif S1 == 8 or S1 == 9:
            print("Fila A - R$5300,00")
            print("Fila B,C e D - R$3500,00")
    
        elif S1 == 12:
            print("Fila A - R$2000,00")
            print("Fila B - R$1375,00")
    
        elif S1 == 13:
            print("Fila A - R$2000,00")
            print("Fila B - R$1375,00")
            print("Fila C, D, E e F - R$1000,00")

    print(f"{NAmarelo}\nTodas as frisas contém 6 lugares{Corfim}")
    print(f"O site para compras é:\n{NCiano}https://www.totalacesso.com/events/carnavalrio2024{Corfim}\n")

frisa()
