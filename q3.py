chance_ataque = int(input())

if chance_ataque <= 50:
    local_recomendado = str(input())
elif chance_ataque > 50:
    nome_heroi = str(input())

if chance_ataque <= 50 and local_recomendado == "Maceió":
    print("Ufa, finalmente posso tirar minhas férias!")
    print("Bem que eu tava com saudade de uma boa praia!")
elif chance_ataque <= 50 and local_recomendado == "Pipa":
    print("Ufa, finalmente posso tirar minhas férias!")
    print("As noites em Pipa parecem muito animadas, to dentro!")
elif chance_ataque <= 50 and local_recomendado == "Caruaru":
    print("Ufa, finalmente posso tirar minhas férias!")
    print("Parece um local muito divertido para aproveitar as festas juninas!")
elif chance_ataque <= 50 and local_recomendado == "Bonito":
    print("Ufa, finalmente posso tirar minhas férias!")
    print("Praticar rapel nas cachoeiras vai ser demais!")
elif chance_ataque <= 50 and local_recomendado != ("Maceió" and "Pipa" and "Caruaru" and "Bonito"):
    print("Ufa, finalmente posso tirar minhas férias!")
    print(f"Nunca ouvi falar sobre {local_recomendado}, mas me parece uma boa ideia!")

if chance_ataque > 50 and nome_heroi == "Homem-Aranha":
    print("Esses heróis nunca desistem, lá vou eu enfrentar mais um!")
    print("O amigo da vizinhança nunca me deixa em paz! Será derrotado!")
elif chance_ataque > 50 and nome_heroi == "Capitão América":
    print("Esses heróis nunca desistem, lá vou eu enfrentar mais um!")
    print("Derrotar o carinha do escudo vai ser moleza!")
elif chance_ataque > 50 and nome_heroi == "Spider Gwen":
    print("Esses heróis nunca desistem, lá vou eu enfrentar mais um!")
    print("A namoradinha do spidey nunca será capaz de me derrotar!")
elif chance_ataque > 50 and nome_heroi == "Hulk":
    print("Esses heróis nunca desistem, lá vou eu enfrentar mais um!")
    print("Esse aí só sabe gritar e quebrar tudo, não será páreo para mim!")
elif chance_ataque > 50 and nome_heroi != ("Homem-Aranha" and "Capitão América" and "Spider Gwen" and "Hulk"):
    print("Esses heróis nunca desistem, lá vou eu enfrentar mais um!")
    print(f"Não conheço esse herói {nome_heroi}. Preciso me preparar para essa batalha!")