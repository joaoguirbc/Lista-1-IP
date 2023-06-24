funcionalidade1 = str(input())
energia1 = int(input())

funcionalidade2 = str(input())
energia2 = int(input())

funcionalidade3 = str(input())
energia3 = int(input())

funcionalidade4 = str(input())
energia4 = int(input())

funcionalidade5 = str(input())
energia5 = int(input())

soma_energia = int(energia1 + energia2 + energia3 + energia4 + energia5)

if funcionalidade1 == "novo lançador de teias":
    print("Com calma, aranha")

if funcionalidade1 == "novo lançador de teias":
    if funcionalidade2 == "lentes de visão avançada":
        print("Lembre de desativar as lentes depois, e cuidado ao usar as teias no escuro")

if funcionalidade1 == "novo lançador de teias":
    if funcionalidade2 == "lentes de visão avançada":
        if funcionalidade3 == "traje à prova de balas":
            print("UOU, só tente sair dessa vivo, vou otimizar a energia aqui")

if (
    funcionalidade1 == "ativação de inteligência artificial" or 
    funcionalidade2 == "ativação de inteligência artificial" or 
    funcionalidade3 == "ativação de inteligência artificial" or 
    funcionalidade4 == "ativação de inteligência artificial" or 
    funcionalidade5 == "ativação de inteligência artificial"
):
    print("Espero que não esteja ativando isso para usar nas provas")

if soma_energia >= 80:
    print("Vou descarregar em questão de minutos, pare AGORA")

if ((funcionalidade1 == "ativação de inteligência artificial" or 
    funcionalidade2 == "ativação de inteligência artificial" or 
    funcionalidade3 == "ativação de inteligência artificial" or 
    funcionalidade4 == "ativação de inteligência artificial" or 
    funcionalidade5 == "ativação de inteligência artificial") and
    (funcionalidade1 == "novo lançador de teias" or 
    funcionalidade2 == "novo lançador de teias" or 
    funcionalidade3 == "novo lançador de teias" or 
    funcionalidade4 == "novo lançador de teias" or 
    funcionalidade5 == "novo lançador de teias") and
    (funcionalidade1 == "membranas planadoras" or 
    funcionalidade2 == "membranas planadoras" or 
    funcionalidade3 == "membranas planadoras" or 
    funcionalidade4 == "membranas planadoras" or 
    funcionalidade5 == "membranas planadoras")
):
    print("Tudo certo, mas cuidado ao ficar conversando com IA enquanto voa")

print(f"Aranha, nessa sequência você usou {soma_energia} de energia!")