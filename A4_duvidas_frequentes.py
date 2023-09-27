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

def duvidas1():
    X ="Dúvidas Frequentes"
    sep(X)
    
###################
    P1 = " 1 - Qual a idade mínima permitida para crianças assistirem aos desfiles de samba?\n"
    P2 = "2 - Existem, no Sambódromo, áreas para Pessoas com Deficiência? Em caso afirmativo, como conseguir esses ingressos?\n"
    P3 = "3 - Existe a disponibilidade de ingressos de meia-entrada?\n"
    P4 = "4 - Como é feita a escolha dos julgadores do Grupo Especial?\n"
    P5 = "5 - Como são as Frisas e qual a sua capacidade?\n"
    P6 = "6 - Qual a primeira escola de samba?\n"
    P7 = "7 - A criança paga? Em caso afirmativo, tem alguma diferença no valor?\n"
    P8 = "8 - O que é permitido levar em bolsa térmica? Em que quantidade?\n"
    P9 = "9 - Qual o horário de abertura dos portões do Sambódromo nos dias de desfiles oficiais?\n"
    P10 = "10 - Onde consigo tirar outras dúvidas e informações?\n"

    print(P1,P2,P3,P4,P5,P6,P7,P8,P9,P10)
###################

##############
    X = input(f"\n{NAmarelo}Qual o indice da duvida que deseja ser esclarecida?{Corfim}")
    def Resposta():
        return print(f"{NVerde}Resposta:{Corfim}")
    
#############
    
    if X == "1":
        print(f"\n{P1}")
        Resposta()
        print("Com o intuito de preservar a integridade do sistema auditivo das crianças, o Juizado da Infância e da Adolescência da Comarca da Capital do Estado do Rio de Janeiro estabeleceu o limite mínimo de idade de 05 anos (completos) para o ingresso no Sambódromo, desde os desfiles carnavalescos de 2015. As autoridades podem, inclusive, exigir a apresentação da Certidão de Nascimento da criança")
    elif X == "2":
        print(f"\n{P2}")
        Resposta()
        print("Sim, existem duas áreas exclusivas para deficientes físicos, a saber:\n  PRIMEIRA: Junto à Praça da Apoteose, após as frisas do Setor 13. Ali são disponibilizados 300 lugares para Portadores de Necessidades Especiais (PNEs) com direito a um acompanhante. Estes ingressos são gratuitos e distribuídos pela Associação de PNEs , Riotur e Prefeitura do Rio de Janeiro. \n  SEGUNDA: Junto ao Setor 10 do Sambódromo, espaço com capacidade para 12 lugares. Estes ingressos são vendidos normalmente ao preço de R$ 600,00 (SEISCENTOS REAIS), com direito a levar um acompanhante. Ainda existe uma terceira área especificamente nas arquibancadas dos setores 02, 04, 06 e 08 localizada no primeiro degrau, numa área devidamente demarcada pela RIOTUR, com espaço de até 08 cadeirantes por setor")
    elif X == "3":
        print(f"\n{P3}")
        Resposta()
        print("Sim, a LIESA e a RIOTUR disponibilizam a oportunidade a estudantes, idosos, menores até 21 anos, jovens pertencentes a famílias de baixa renda, professores da rede pública municipal do Rio de Janeiro e a Portadores de Necessidades Especiais (PNEs) a adquirirem ingressos de meia-entrada em todas as Arquibancadas Especiais, Populares e Cadeiras Individuais. Aos portadores de PNEs é recomendável as Arquibancadas Especiais dos setores 02, 04, 06 e 08. As leis (Federais) nº 10.741/2003 e 12.933/13, (Estadual) nº 3364/2000, (Municipais) nº 3.424/2002 e 5.844/15 e Decreto Federal nº 8.537/15 amparam esse direito. A exceção ocorre nas Arquibancadas Especiais Numeradas do Setor 9, comercializadas pela ABAV/RJ. Estes ingressos são destinados às Agências de Viagens e para atendimento ao turismo receptivo.\nATENÇÃO!\n  A compra de meia-entrada é direito pessoal e intransferível. O ingresso deverá, ao ser feita a solicitação de compra (por internet, telefone e/ou presencial), ter origem numa codificação exclusiva. Não será admitido/permitido que o comprador, quando da reserva de ingressos que não for efetuada pela opção exclusiva de meia-entrada, possa, quando do pagamento da reserva efetuada de forma normal,querer exercer a opção de que um dos ingressos seja de meia-entrada. O ingresso de meia-entrada será emitido individualmente e personalizado (com nome e CPF). Nos dias de desfiles, os funcionários das roletas especialmente designados, nos setores 08 / lado par e 09 / lado ímpar, farão a conferência da identificação do ingresso com a documentação do portador, quando de seu acesso à Passarela. Para os estudantes que optarem pelo benefício de adquirir o ingresso de meia-entrada, deverão observar o que dispõe o art. 3º do Decreto nº 8.537 de 5 de Outubro de 2015.")
    elif X == "4":
        print(f"\n{P4}")
        Resposta()
        print("O critério e a responsabilidade pela escolha dos julgadores são de competência única e exclusiva do Presidente da LIESA, conforme o Regulamento dos Desfiles, aprovado em plenário pelos Representantes das Escolas de Samba.")
    elif X == "5":
        print(f"\n{P5}")
        Resposta()
        print("São boxes descobertos e cercados, com entrada privativa, com capacidade para seis.\n\nFrisas de 06 lugares: Localizadas nos setores: 02-03-04-05-06-07-08-09-10-11.\n\nSão divididas em quatro fileiras:\n\nFila A (junto à pista de desfile);\nFila B (40 cm acima, logo atrás da fila A);\nFila C (40 cm acima, logo atrás da fila B);\nFila D (40 cm acima, logo atrás da fila C);\n\nFrisas de 06 lugares:\n\nFrisas localizadas no setor 12:\nDivididas em duas fileiras\nFila A (junto à pista de desfile);\nFila B (logo atrás da fila A);\n\nFrisas localizadas no setor 13:\nFila A (junto à pista de desfile);\nFila B ( logo atrás da fila A);\nFilas C, D, E e F localizadas rigorosamente atrás da fileira antecedente;\n\nPREÇO: De acordo com a localização do setor.\nCOMERCIALIZAÇÃO: Pagamento à vista.\nAQUISIÇÃO: Por unidade de seis por dia de desfile.\n\nPessoa física: uma Frisa por dia de desfile.\nPessoa Jurídica: duas Frisas por dia de desfile.")
    elif X == "6":
        print(f"\n{P6}")
        Resposta()
        print("A primeira escola de samba é a gloriosa GRES Estácio de Sá. Fundada sob o nome de Deixa Falar em 12 de agosto de 1928 e ela é considerada pioneira porque foi a primeira a reunir a série de elementos que formam uma escola de samba atualmente.")
    elif X == "7":
        print(f"\n{P7}")
        Resposta()
        print("Sim, crianças pagam ingressos a partir dos 05 (cinco) anos de idade. A criança tem direito a meia-entrada, desde que acompanhada pelos pais ou responsáveis, nos setores de Arquibancadas Especiais, Populares e Cadeiras Individuais. Nas Frisas, Camarotes e Boxes Especiais deverão portar ingressos normais, não existindo possibilidade de meia-entrada.")
    elif X == "8":
        print(f"\n{P8}")
        Resposta()
        print("O espectador poderá levar até 12 (doze) vasilhames plásticos de 500 ml com bebida (água, suco, refrigerante ou cerveja) e até 10 (dez) itens de alimentação (fruta, salgado ou sanduíche). CONTINUA PROIBIDA A ENTRADA DE ISOPORES, GARRAFAS DE VIDRO, LATAS DE ALUMÍNIO, SACOLAS, ARMAS DE FOGO, OBJETOS CORTANTES, SACOS PLÁSTICOS, FOGOS DE ARTIFÍCIO E SINALIZADORES")
    elif X == "9":
        print(f"\n{P9}")
        Resposta()
        print("Os portões serão abertos às 21h")
    elif X == "10":
        print(f"\n{P10}")
        Resposta()
        print("Central LIESA de Atendimento\nRua da Alfândega, 25 - lojas B e C – Centro\nTel.: (21) 3190-2100\nHorário de Atendimento telefônico: Das 09:00 às 17:00 horas\nDe Segunda a Sexta-feira\nE-mail: centraldeatendimento@liesa.org.br")
     
        #Opção - Divergentes
    else:
        print( f"{NVermelho}Digito Errado, digite novamente{Corfim}")
        duvidas1()

duvidas1()