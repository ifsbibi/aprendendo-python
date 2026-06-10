dados_pessoais = {

    "nome" : "Joao",
    "idade" : 21,
    "nascimento" : "20-05-2005",
    "sexo" : "M",
    "altura" : 1.70,
    "temCNH" : True,

    }

continuar = "s"
while continuar == "s":


        dados = input("Digite o que você que encontrar: ")

        print(dados_pessoais.get(dados, "Valor não encontrado! "))

        continuar = input("Quer continuar? (s/n):")[0].lower()
        