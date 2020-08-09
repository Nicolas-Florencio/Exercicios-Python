"""
-----------------------------------------
	Função: Informa o dia da semana a partir de um número informado
	Autor: Nicolas Florencio Alves.
	Data de criação: 09/08/2020.
	Data de modificação: 09/08/2020.
-------------------------------------------
"""
n = int(input("Informa o número do dia da semana: "))
if n == 1:
    print("\nSegunda-Feira")
elif n == 2:
    print("\nTerça-Feira")
elif n == 3:
    print("\nQuarta-Feira")
elif n == 4:
    print("\nQuinta-Feira")
elif n == 5:
    print("\nSexta-Feira")
elif n == 6:
    print("\nSábado")
elif n == 7:
    print("\nDomingo")
else:
    print("\nDia da semana inválido")