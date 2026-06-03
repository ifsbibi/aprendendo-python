notasAlunos = [  ["Joao", 8.7, 9.0],
                 ["Maria", 7.3, 9.0],
                 ["José", 8.3, 5.2] ]

mediaAlunos = []

for i in notasAlunos:
    media = (i[1]+i[2])/2

    lista = []
    lista.append(i[0])
    lista.append(media)

    mediaAlunos.append(lista)

print(mediaAlunos)


#global fora do for
#local dentro do for