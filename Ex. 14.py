"""
-----------------------------------------
	Função: Recebe três valores e informa qual é maior
	Autor: Nicolas Florencio Alves.
	Data de criação: 09/08/2020.
	Data de modificação: 09/08/2020.
-------------------------------------------
"""
n1 = float(input("Informe o primeiro valor: "))
n2 = float(input("Informe o segundo valor: "))
n3 = float(input("Informe o terceiro valor: "))
if n1 > n2 and n1 > n3:
    print("\nO maior número é: ", n1)

elif n2 > n1 and n2 > n3:
    print("\nO maior número é: ", n2)

elif n3 > n1 and n3 > n2:
    print("\nO maior número é: ", n3)

else:
    print("\nOs valores são iguais!")