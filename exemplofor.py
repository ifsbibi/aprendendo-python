 # SIMULAÇÃO DE CHAMADA

alunos = ["Jaqueline", "Débora" , "Evilyn", "Arthur", "João Gabriel", "Izaac", "Iago", "Luã", "Rafael Mendes", "Rafael Lisboa"]

alunos.sort()

print(f"Quantos alunos tem na sala:  {len(alunos)}")

print("--- Iniciando a chamada! ---")
for i in alunos:
    print(f"Aluno(a) {i} está presente!")
print("--- Fim da chamada!")
