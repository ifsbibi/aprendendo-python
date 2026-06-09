buscador = [
             [5, 2, 9],
             [1, 8, 3],
             [4, 7, 6]
    ]

busca = int(input("Digite um número que deseja buscar: "))

for i in range(len(buscador)):
    for j in range(len(buscador[i])):
        if buscador [i][j] == busca:
            print(f"O numero que você procura está na linha {i} e na coluna {j+1}")
            achou = True
            break

        if achou:
            break



