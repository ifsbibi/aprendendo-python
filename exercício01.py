n1 = int(input("digte o primeiro número: "))
n2 = int(input("digte o segundo número: "))

resultado = n1 // n2
resultado2 = n1 % n2
resultado3 = n1 ** n2

print("o resultado é ",resultado)
print("o resultado2 é ",resultado2)
print("o resultado3 é ",resultado3)


print("--------------------------------------------------------------------------")
print("   OPERADORES RELACIONAIS"      )
print("--------------------------------------------------------------------------")


relacao1 = n1 > n2
relacao2 = n1 < n2
relacao3 = n1 >= n2
relacao4 = n1 <= n2
relacao5 = n1 == n2
relacao6 = n1 != n2

print("Os resultados das relacao estarao abaixo: \n{} \n{} \n{} \n{} \n{} \n{}".format(relacao1, relacao2, relacao3, relacao4, relacao5, relacao6))