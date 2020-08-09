"""
-----------------------------------------
	Função: Informa a ordem crescente de 3 números
	Autor: Nicolas Florencio Alves.
	Data de criação: 09/08/2020.
	Data de modificação: 09/08/2020.
-------------------------------------------
"""
n1 = float(input("Informe o primeiro valor: "))
n2 = float(input("Informe o segundo valor: "))
n3 = float(input("Informe o terceiro valor: "))

if n1 <= n2 <= n3:
    print("\nA ordem crescente é: %.2f, %.2f e %.2f" % (n1, n2, n3))

elif n2 <= n1 <= n3:
    print("\nA ordem crescente é: %.2f, %.2f e %.2f" % (n2, n1, n3))

elif n3 <= n1 <= n2:
    print("\nA ordem crescente é: %.2f, %.2f e %.2f" % (n3, n1, n2))

elif n1 <= n3 <= n2:
    print("\nA ordem crescente é: %.2f, %.2f e %.2f" % (n1, n3, n2))

elif n2 <= n3 <= n1:
    print("\nA ordem crescente é: %.2f, %.2f e %.2f" % (n2, n3, n1))

elif n3 <= n2 <= n1:
    print("\nA ordem crescente é: %.2f, %.2f e %.2f" % (n3, n2, n1))