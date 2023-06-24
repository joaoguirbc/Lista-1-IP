vida_venom = int(input())
ataque_venom = int(input())
pocao_venom = int(input())

vida_creeper = int(input())
ataque_creeper = ataque_venom

vida_druida = int(input())
ataque_druida = int(input())

#1º confronto
print("SENHORAS E SENHORES! AGORA O VENOM ENFRENTARÁ O CREEPER!")
if ataque_venom >= vida_creeper and vida_venom > ataque_creeper:
    print("O creeper não tankou e foi de base...")
    print("Isso aí! Ele é todo esquentadinho, mas no final deu tudo certo!")
    vencedor_r1 = "Venom"
    vida_atual_venom = vida_venom - ataque_creeper
elif ataque_creeper >= vida_venom and vida_creeper > ataque_venom:
    print("O venom não tankou e foi de base...")
    print("AH NÃO! O VENOM PEGOU EM BOMBA!")
    vencedor_r1 = "Creeper"
elif ataque_creeper >= vida_venom and ataque_venom >= vida_creeper:
    print("O venom não tankou e foi de base...")
    print("O creeper não tankou e foi de base...")
    print("AH NÃO! O VENOM PEGOU EM BOMBA!")
    vencedor_r1 = "Creeper"
else:
    vida_atual_venom = vida_venom - ataque_creeper
    vida_atual_creeper = vida_creeper - ataque_venom
    if vida_atual_venom > vida_atual_creeper:
        vencedor_r1 = "Venom"
        print(f"Vida atual do Venom: {vida_atual_venom}")
        print(f"Dano sofrido pelo Venom: {ataque_creeper}")
        print(f"Vida atual do creeper: {vida_atual_creeper}")
        print(f"Dano sofrido pelo creeper: {ataque_venom}")
        print("Isso aí! Ele é todo esquentadinho, mas no final deu tudo certo!")
    else:
        vida_atual_venom = vida_venom - ataque_creeper
        vida_atual_creeper = vida_creeper - ataque_venom
        vencedor_r1 = "Creeper"
        print(f"Vida atual do Venom: {vida_atual_venom}")
        print(f"Dano sofrido pelo Venom: {ataque_creeper}")
        print(f"Vida atual do creeper: {vida_atual_creeper}")
        print(f"Dano sofrido pelo creeper: {ataque_venom}")
        print("AH NÃO! O VENOM PEGOU EM BOMBA!")

#Tentativa de poção
if vencedor_r1 == "Venom":
    if vida_atual_venom + pocao_venom <= vida_venom:
        vida_atual_venom += pocao_venom
        print("Ah! Essa poção é da boa!")

#Poção forçada pelo druida
if vencedor_r1 == "Venom":
    if vida_atual_venom + pocao_venom < vida_venom:
        vida_atual_venom += pocao_venom
    elif vida_atual_venom + pocao_venom == vida_venom:
        vida_atual_venom = vida_venom
    elif vida_atual_venom + pocao_venom > vida_venom:
        ataque_druida += (vida_atual_venom + pocao_venom - vida_venom)
        vida_atual_venom = vida_venom

#2º confronto
if vencedor_r1 == "Venom":
    print("SENHORAS E SENHORES! AGORA O VENOM ENFRENTARÁ O DRUIDA!")
    if ataque_venom >= vida_druida and vida_atual_venom > ataque_druida:
        print("O druida não tankou e foi de base...")
        print("Quase me dei mal, nunca mais aceito nada de estranho...")
        vencedor_r2 = "Venom"
        vida_atual_venom = vida_venom - ataque_druida
    elif ataque_druida >= vida_atual_venom and vida_druida > ataque_venom:
        print("O venom não tankou e foi de base...")
        print("Pelo visto a poção tava fora do prazo de validade :(")
        vencedor_r2 = "Druida"
    elif ataque_druida >= vida_atual_venom and ataque_venom >= vida_druida:
        print("O venom não tankou e foi de base...")
        print("O druida não tankou e foi de base...")
        print("Pelo visto a poção tava fora do prazo de validade :(")
        vencedor_r2 = "Druida"
    else:
        vida_atual_venom_r2 = vida_atual_venom - ataque_druida
        vida_atual_druida = vida_druida - ataque_venom
        if ataque_venom > ataque_druida:
            vencedor_r2 = "Venom"
            print(f"Vida atual do Venom: {vida_atual_venom_r2}")
            print(f"Dano sofrido pelo Venom: {ataque_druida}")
            print(f"Vida atual do druida: {vida_atual_druida}")
            print(f"Dano sofrido pelo druida: {ataque_venom}")
            print("Quase me dei mal, nunca mais aceito nada de estranho...")
        elif ataque_druida > ataque_venom:
            vencedor_r2 = "Druida"
            print(f"Vida atual do Venom: {vida_atual_venom_r2}")
            print(f"Dano sofrido pelo Venom: {ataque_druida}")
            print(f"Vida atual do druida: {vida_atual_druida}")
            print(f"Dano sofrido pelo druida: {ataque_venom}")
            print("Pelo visto a poção tava fora do prazo de validade :(")
        elif vida_atual_venom_r2 > vida_atual_druida:
            vencedor_r2 = "Venom"
            print(f"Vida atual do Venom: {vida_atual_venom_r2}")
            print(f"Dano sofrido pelo Venom: {ataque_druida}")
            print(f"Vida atual do druida: {vida_atual_druida}")
            print(f"Dano sofrido pelo druida: {ataque_venom}")
            print("Quase me dei mal, nunca mais aceito nada de estranho...")
        else:
            vida_atual_venom_r2 = vida_atual_venom - ataque_druida
            vida_atual_druida = vida_druida - ataque_venom
            vencedor_r2 = "Druida"
            print(f"Vida atual do Venom: {vida_atual_venom_r2}")
            print(f"Dano sofrido pelo Venom: {ataque_druida}")
            print(f"Vida atual do druida: {vida_atual_druida}")
            print(f"Dano sofrido pelo druida: {ataque_venom}")
            print("Pelo visto a poção tava fora do prazo de validade :(")

#Print final
if vencedor_r1 == "Venom" and vencedor_r2 == "Venom":
    print("Essa aventura foi epicamente épica, meu amigo! Boa viagem aí! * Começa a tocar saxofone *")
else:
    print("Pelo visto as aventuras do Miles terminaram por aqui...")