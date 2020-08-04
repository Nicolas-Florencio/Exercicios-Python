"""
-----------------------------------------
	Função: troca os números de variáveis
	se for maior que 100 ele recebe 150
	Autor: Nicolas Florencio Alves.
	Data de criação: 03/08/2020.
	Data de modificação: 03/08/2020.
-------------------------------------------
"""
a = int(input("Informe um número para ser trocado: "))
b = int(input("Informe outro número para ser trocado: "))

b = a + b
a = b - a
b = b - a

print("Os valores trocados ficam da seguinte maneira: %d e %d" % (a, b))