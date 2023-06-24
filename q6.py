nome = str(input())
numero_pessoas = int(input())
coeficiente = float(input())

if numero_pessoas % 2 == 0:
    formula = float(((coeficiente * (numero_pessoas - 1)) + 1))
else:
    formula = float(((coeficiente * (numero_pessoas - 1)) / 2))

fumantes = int(formula + 0.5)

proporcao_ciclo = int((fumantes/numero_pessoas) * 100)

print(f"Vamos verificar se {nome} vai fumar singaro!")
print(f"{proporcao_ciclo}% dos seus amigos fumam singaro")

if proporcao_ciclo < 25:
    print("Você tem poucas chances de fumar singaro, fuma não pow, cuide da sua saúde")
elif 25 < proporcao_ciclo < 50:
    print("Cuidado pra não fumar ein, fuma não pow, cuide da sua saúde")
elif proporcao_ciclo > 50:
    print("TIRA ESSE SINGARO DA BOCA. FUMA NÃO POW, CUIDE DA SUA SAÚDE!")