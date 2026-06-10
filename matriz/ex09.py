matriz = [
                    [15,42,7],
                    [23,91,12],
                    [34,8,55]
                                ]

matriz_V = [sum(n) for n in matriz]

matriz_S = [n for conjunto in matriz for n in conjunto]

maior = max (matriz_S)
menor = min(matriz_S)

matriz_S.index(maior)
matriz_S.index(menor) 