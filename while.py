listaIdades =[]
continuar = "s"

while continuar == "s":
    idade = int(input("Digite sua idade:"))
    listaIdades.append(idade)
    continuar = input("Quer continuar? (s/n)").upper()[0]

    print(listaIdades)