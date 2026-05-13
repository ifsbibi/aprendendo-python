# Atividade de média

frequencia = int(input("Informe quantos dias o aluno compareceu as aulas: "))

if frequencia > 0 :
    nota1 = float(input("digte o primeiro número: ").replace("," , "."))
    nota2 = float(input("digte o primeiro número: ").replace("," , "."))

media = (nota1 + nota2) /2

print("a media é ",media)

if media >=7 : 
    print("aprovado")
elif media >=5 : 
    print("recuperação")
elif media <5 :
    print("reprovado")
else : 
    print("Aluno não foi as aulas")
    
if nota > 3:
    print("aprovado")
if nota > 4:    
    print("nota maior que a média")
if nota == 5: 
    print("nota maxima, parabens!")
else:
    print("aprovado")