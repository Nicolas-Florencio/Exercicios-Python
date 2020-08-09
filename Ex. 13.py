"""
-----------------------------------------
	Função: Informa qual dois números informados é maior
	Autor: Nicolas Florencio Alves.
	Data de criação: 09/08/2020.
	Data de modificação: 09/08/2020.
-------------------------------------------
"""
n1 = float(input("Informe o primeiro valor: "))
n2 = float(input("Informe o segundo valor: "))

if n1 < n2:
    print("\nO maior valor é: %.2f" % n2)

elif n2 < n1:
    print("\nO maior valor é: %.2f" % n1)

else:
    print("\nOs valores são iguais")
