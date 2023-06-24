caracteristica1 = str(input())
caracteristica2 = str(input())

paixao = str(input())

habilidade = str(input())

nota1 = int(input())
nota2 = int(input())
nota3 = int(input())

if caracteristica1 == "Humildade" and caracteristica2 == "Bondade":
    if paixao == "Mary" or paixao == "Ninguem":
        if habilidade == "Dancar" or habilidade == "Lancar":
            if ((nota1 + nota2 + nota3) / 3) >= 7:
                print("Siga em frente, olhe para o lado. Bem-vindo ao aranhaverso, Miranha Furacao!")

if caracteristica1 != "Humildade" or caracteristica2 != "Bondade":
    print("Ops, parece que não foi dessa vez, Miranha. Você terá que continuar na Carreta Furacao mesmo!")
    print("Infelizmente você não possui as característica necessárias!")
elif paixao != "Mary" and paixao != "Ninguem":
    print("Ops, parece que não foi dessa vez, Miranha. Você terá que continuar na Carreta Furacao mesmo!")
    print("Infelizmente você não está apaixonado pela pessoa certa!")
elif habilidade != "Dancar" and habilidade != "Lancar":
    print("Ops, parece que não foi dessa vez, Miranha. Você terá que continuar na Carreta Furacao mesmo!")
    print("Infelizmente você não possui as habilidades necessárias!")
elif ((nota1 + nota2 + nota3) / 3) < 7:
    print("Ops, parece que não foi dessa vez, Miranha. Você terá que continuar na Carreta Furacao mesmo!")
    print("Infelizmente você não obteve um bom desempenho escolar!")