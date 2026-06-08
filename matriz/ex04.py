vendas = [
           [1200, 850, 900, 1500],
           [900, 1100, 1000, 1300],
           [1500, 1600, 1400, 1800],
           [700, 600, 800, 900]
                                     ]

print("Total vendido por cada vendedor:")

for i in range(len(vendas)):
    total_vendedor = sum(vendas[i])
    print(f"Vendedor {i + 1}: R$ {total_vendedor}")

print("\nTotal vendido por dia:")

for coluna in range(len(vendas[0])):
    total_dia = 0

    for linha in range(len(vendas)):
        total_dia += vendas[linha][coluna]

    print(f"Dia {coluna + 1}: R$ {total_dia}")