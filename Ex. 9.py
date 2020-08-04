"""
-----------------------------------------
	Função: Calcula se o número é maior ou menor que 100
	se for maior que 100 ele recebe 150
	Autor: Nicolas Florencio Alves.
	Data de criação: 03/08/2020.
	Data de modificação: 03/08/2020.
-------------------------------------------
"""
print("Se o número informado for maior que 100 ele será acrescido a 150")
print("Caso contrário, nada ocorrerá")
n = int(input("Informe o número: "))

if n > 100:
    print("O número é maior que 100,então,ele recebe 150, logo se torna: ", n + 150)

elif n < 100:
    print("O número %d é menor que 100 então não receberá 150" %(n))
else:
    print("O número %d é igual a 100 então não receberá 150" % (n))
