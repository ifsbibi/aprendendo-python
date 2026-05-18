salario = float(input("Digite o sálario brutp: R$  "))

parcela = float(input("Digite o valor da parcela: R$  "))

limite = salario * 0.30

if parcela <= limite:
    print("Crédito aprovado!")
else:
    print("Crédito recusado")

