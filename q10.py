nome_aranha = str(input())
dano_aranha = int(input())
defesa_aranha = int(input())
nome_aliado = str(input())
dano_aliado = int(input())
defesa_aliado = int(input())

nome_vilao = str(input())
dano_vilao = int(input())
defesa_vilao = int(input())
nome_capanga = str(input())
dano_capanga = int(input())
defesa_capanga = int(input())

fator_sorte_r1 = int(input())
fator_sorte_r2 = int(input())
fator_sorte_r3 = int(input())

pontos_aranha = 0
pontos_vilao = 0

#1º Confronto
print("1° confronto:")

if fator_sorte_r1 == 0:
    if dano_aranha >= defesa_vilao:
        pontos_aranha += 1
        print(f"O {nome_aranha} acertou vários golpes no {nome_vilao}")
    else:
       print(f"O {nome_vilao} está dificultando a vida do {nome_aranha}")
       pontos_vilao += 1 
elif fator_sorte_r1 == 1:
    dano_aranha_r1 = dano_aranha + dano_aliado
    if dano_aranha_r1 >= defesa_vilao:
        pontos_aranha += 1
        print(f"O {nome_aranha} acertou vários golpes no {nome_vilao}")
    else:
        pontos_vilao += 1
        print(f"O {nome_vilao} está dificultando a vida do {nome_aranha}")
elif fator_sorte_r1 == 2:
    defesa_vilao_r1 = defesa_vilao + defesa_capanga
    if dano_aranha > defesa_vilao_r1:
        pontos_aranha += 1
        print(f"O {nome_aranha} acertou vários golpes no {nome_vilao}")
    else:
        pontos_vilao += 1
        print(f"O {nome_vilao} está dificultando a vida do {nome_aranha}")
elif fator_sorte_r1 == 3:
    dano_aranha_r1 = dano_aranha + dano_aliado
    defesa_vilao_r1 = defesa_vilao + defesa_capanga
    if dano_aranha_r1 >= defesa_vilao_r1:
        pontos_aranha += 1
        print(f"O {nome_aranha} acertou vários golpes no {nome_vilao}")
    else:
        pontos_vilao += 1
        print(f"O {nome_vilao} está dificultando a vida do {nome_aranha}")

#2º Confronto
print("2° confronto:")

if fator_sorte_r2 == 0:
    if defesa_aranha >= dano_vilao:
        pontos_aranha += 1
        print(f"O {nome_aranha} contra-atacou o {nome_vilao}")
    else:
       print(f"O {nome_aranha} não consegue se defender contra o {nome_vilao}")
       pontos_vilao += 1 
elif fator_sorte_r2 == 1:
    dano_vilao_r2 = dano_vilao + dano_capanga
    if defesa_aranha > dano_vilao_r2:
        pontos_aranha += 1
        print(f"O {nome_aranha} contra-atacou o {nome_vilao}")
    else:
        pontos_vilao += 1
        print(f"O {nome_aranha} não consegue se defender contra o {nome_vilao}")
elif fator_sorte_r2 == 2:
    defesa_aranha_r2 = defesa_aranha + defesa_aliado
    if defesa_aranha_r2 >= dano_vilao:
        pontos_aranha += 1
        print(f"O {nome_aranha} contra-atacou o {nome_vilao}")
    else:
        pontos_vilao += 1
        print(f"O {nome_aranha} não consegue se defender contra o {nome_vilao}")
elif fator_sorte_r2 == 3:
    dano_vilao_r2 = dano_vilao + dano_capanga
    defesa_aranha_r2 = defesa_aranha + defesa_aliado
    if defesa_aranha_r2 >= dano_vilao_r2:
        pontos_aranha += 1
        print(f"O {nome_aranha} contra-atacou o {nome_vilao}")
    else:
        pontos_vilao += 1
        print(f"O {nome_aranha} não consegue se defender contra o {nome_vilao}")

#3º Confronto
print("3° confronto:")
if fator_sorte_r3 == 0:
    if dano_aranha >= defesa_vilao:
        pontos_aranha += 1
        print(f"O {nome_aranha} acertou vários golpes no {nome_vilao}")
    else:
        pontos_vilao += 1
        print(f"O {nome_vilao} está dificultando a vida do {nome_aranha}")
elif fator_sorte_r3 == 1:
    dano_aranha_r3 = dano_aranha + dano_aliado
    if dano_aranha_r3 >= defesa_vilao:
        pontos_aranha += 1
        print(f"O {nome_aranha} acertou vários golpes no {nome_vilao}")
    else:
        pontos_vilao += 1
        print(f"O {nome_vilao} está dificultando a vida do {nome_aranha}")
elif fator_sorte_r3 == 2:
    defesa_vilao_r3 = defesa_vilao + defesa_capanga
    if dano_aranha > defesa_vilao_r3:
        pontos_aranha += 1
        print(f"O {nome_aranha} acertou vários golpes no {nome_vilao}")
    else:
        pontos_vilao += 1
        print(f"O {nome_vilao} está dificultando a vida do {nome_aranha}")
elif fator_sorte_r3 == 3:
    defesa_vilao_r3 = defesa_vilao + defesa_capanga
    dano_aranha_r3 = dano_aranha + dano_aliado
    if dano_aranha >= defesa_vilao:
        pontos_aranha += 1
        print(f"O {nome_aranha} acertou vários golpes no {nome_vilao}")
    else:
        pontos_vilao += 1
        print(f"O {nome_vilao} está dificultando a vida do {nome_aranha}")

#Decisão e anúncio do vencedor
if pontos_aranha > pontos_vilao:
    print(f"O {nome_aranha} e {nome_aliado} conseguiram derrotar o {nome_vilao} e recuperar o multiverso!")
else:
    print(f"O {nome_vilao} e {nome_capanga} invadiram Nova York, onde estão os outros aranhas??")