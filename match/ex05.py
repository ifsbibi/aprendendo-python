perfil = input("Digite o perfil: ")

match perfil:
    case "ADMIN":
        print("Acesso total: Criar, Ler, Atualizar e Deletar.")
    case "GERENTE":
        print("Acesso gerencial: Criar, Ler e Atualizar.")
    case "EDITOR":
        print("Acesso de conteúdo: Ler e Atualizar.")
    case "VISITANTE":
        print("Acesso restrito: Apenas Leitura.")
    case _:
        print("Perfil não reconhecido. Acesso bloqueado.")