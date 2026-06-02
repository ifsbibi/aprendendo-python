codigo = int(input("Digite o código do produto parar prosseguir com a compra abaixo: "))

match codigo:
    case 100:
        print("Cachorro-Quente - R$ 10,00")
    case 101:
        print("Bauru Simples - R$ 12,00")
    case 102:
        print("X-Salada - R$ 15,00")
    case 103:
        print("Hambúrguer - R$ 13,00")
    case _:
        print("Código inválido")



