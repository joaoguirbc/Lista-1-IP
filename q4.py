esconderijo_venom = input()
busca1 = input()

if esconderijo_venom.lower() == busca1.lower():
  print("Ahá, te encontrei e é o fim das suas férias!")
else:
  print("Carambolas, ele não está aqui. Ele continua se divertindo!")
  busca2 = input()
  if esconderijo_venom.lower() == busca2.lower():
    print("Ahá, te encontrei e é o fim das suas férias!")
  else:
    print("Carambolas, ele não está aqui. Ele continua se divertindo!")
    busca3 = input()
    if esconderijo_venom.lower() == busca3.lower():
      print("Ahá, te encontrei e é o fim das suas férias!")
    else:
      print("Carambolas, ele não está aqui. Ele continua se divertindo!")
      print("AAAAAAAH, ele escapou de vez!")