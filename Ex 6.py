"""
-----------------------------------------
	Função: Calcular o preço da venda de um terreno retangular,
	recebendo frente e lado e recendo o valor do metro quadrado.
	Autor: Nicolas Florencio Alves.
	Data de criação: 02/08/2020.
	Data de modificação: 02/08/2020.
-------------------------------------------
"""
base = float(input("Informe a base/largura do terreno: "))
altura = float(input("Informe a altura/comprimento do terreno: "))
preco = float(input("Informe o preço do m²(metro quadrado): "))
print("O preço do terreno com medidas %.2f x %.2f, ficará em: %.2f" %(base, altura, (base*altura*preco)))