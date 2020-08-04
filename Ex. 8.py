"""
-----------------------------------------
	Função: Exibir o quociente e resto da divisão
	Autor: Nicolas Florencio Alves.
	Data de criação: 03/08/2020.
	Data de modificação: 03/08/2020.
-------------------------------------------
"""
dividendo = float(input("Informe o qual número será dividido: "))
divisor = float(input("Informe o divisor (o número de vezes pelo qual você quer dividir): "))
quociente = dividendo/divisor
print("O resultado (quociente) da divisão é: %.3f\nO resto da divisão é: %d" % (quociente, (quociente*divisor)-dividendo))
