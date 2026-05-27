valor = float(input("Digite o valor do saque: R$ "))
cedulas = [50, 20, 10, 5, 2]
notas = 0
while valor > 0:

    for n in cedulas:
