conceito = input("Digite o conceito (A, B, C, D ou F): ")

match conceito:
    case "A":
        print("Excelente trabalho!")
    case "B":
        print("Bom desempenho.")
    case "C":
        print("Satisfatório.")
    case "D":
        print("Abaixo da média (Atenção).")
    case "F":
        print("Reprovado.")
    case _:
        print("Conceito desconhecido.")
        