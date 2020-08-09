"""
-----------------------------------------
	Função: Informa se o número digitado é positivo, negativo ou neutro
	Autor: Nicolas Florencio Alves.
	Data de criação: 09/08/2020.
	Data de modificação: 09/08/2020.
-------------------------------------------
"""
n = float(input("Informe um número: "))
if n > 0:
    print("O número é positivo")

elif n < 0:
    print("O número é negativo")

else:
    print("O número é neutro(zero)")