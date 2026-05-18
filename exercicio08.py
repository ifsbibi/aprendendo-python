valorTotalCompras = float(input("Digite o total das compras: "))

if valorTotalCompras <= 100:
    print(f"Você não teve desconto. O valor total da sua compra é de R$ {valorTotalCompras:.2f}")
elif valorTotalCompras > 100 and valorTotalCompras <= 300:
     valorDesconto = valorTotalCompras * 0.05
     valorComdesconto = valorTotalCompras - valorDesconto
     print(f"Você teve o desconto de 5% . O valor total da sua compra é de R$ {valorTotalCompras:.2f}")

elif valorTotalCompras > 300 and valorTotalCompras < 500:
    print(f"Você teve o desconto de 10%. O valor total da sua compra é de {valorTotalCompras*0.9:.2f}")