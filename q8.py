dica = int(input())

nivel_cansaco = int(0)

if dica % 2 == 0:
    num_caracteres = int(((dica / 2) ** (1/2)) + 2)
else:
    num_caracteres = int((dica / 3) + 3)  

filme_1 = str(input())
filme_2 = str(input())
filme_3 = str(input())

#Checagem de universo
if filme_1 == "Coringa" or filme_1 == "Batman vs Superman" or filme_1 == "O Cavaleiro das Trevas":
    print("Algo de errado não está certo!")
elif len(filme_1) == num_caracteres:
    print("Miles: Achei o easter egg!!!")
    nivel_cansaco += 1
    nome_do_filme = str(input())
    duracao = int(input())
else:
    print("Miles: Tou frio, melhor ir procurar nas fases mais antigas")
    if len(filme_2) == num_caracteres:
        print("Miles: Achei o easter egg!!!")
        nivel_cansaco += 2
        nome_do_filme = str(input())
        duracao = int(input())
    else:
        print("Gwen: Cadê o velho??? Queria um autógrafo")
        if len(filme_3) == num_caracteres:
            print("Miles: Achei o easter egg!!!")
            nivel_cansaco += 3
            nome_do_filme = str(input())
            duracao = int(input())
        else:
            print("Peter: Parece que o próximo filme do aranha-verso vai demorar mais do que esperado pra sair...")

if filme_1 == "Vingadores: Ultimato" or filme_2 == "Vingadores: Ultimato" or filme_3 == "Vingadores: Ultimato":
    nivel_cansaco += 1

if filme_1 != "Coringa" and filme_1 != "Batman vs Superman" and filme_1 != "O Cavaleiro das Trevas":
    if len(filme_1) == num_caracteres or len(filme_2) == num_caracteres or len(filme_3) == num_caracteres:
        if nivel_cansaco >= 2 and duracao >= 135:
            print("Miles: A mimir")
        elif nivel_cansaco >= 2 and 120 <= duracao < 135:
            print("Gwen: Nada que uma xícara de café não resolva!")
        elif nivel_cansaco < 2 or duracao < 120:
            print(f"Peter: {nome_do_filme} é o melhor filme do homem aranha, 10/10")