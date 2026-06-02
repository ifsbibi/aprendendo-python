while True:
    letra = input("Digite uma letra ou 0 pra sair: ")

    match letra:
        case "0":
            print("Programa encerrado")
            break
        case "a" | "e" | "i" | "o" | "u":
            print("É uma vogal!")
        case _:
            print("É uma consoante!") 