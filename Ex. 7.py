"""
-----------------------------------------
	Função: Valor de uma prestação em atraso USANDO: PRESTAÇAO= VALOR + (VALOR * (TAXA/100) * TEMPO)
	diremos qual o valor da prestação que está com pendencia de pagamento
	Autor: Nicolas Florencio Alves.
	Data de criação: 03/08/2020.
	Data de modificação: 03/08/2020.
-------------------------------------------
"""
taxa = float(input("Informe o valor da taxa "))
tempo = int(input("Informe o tempo da prestação(dias, meses e anos): "))
valor = float(input("Informe o valor da prestação: "))
print("O valor da prestação com atraso de pagamento é: %.2f" %(valor + (valor * (taxa/100) * tempo)))
