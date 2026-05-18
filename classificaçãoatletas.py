idade = int(input("Digite a idade do atleta: "))

if idade <=9:
    print("Sua categoria é a mirim")

elif idade <=14:
    print("Sua categoria é a infantil")

elif idade <=19:
    print("Sua categoria é a junior")

elif idade <=25:
    print("Sua categoria é a sênior")
else:
    print("Sua categoria é a master")