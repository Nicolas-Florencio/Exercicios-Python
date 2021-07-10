"""
-----------------------------------------
	Função: Nome e preço de pedido de acordo com a opção escolhida
	Autor: Nicolas Florencio Alves.
	Data de criação: 10/07/2021.
	Data de modificação: 10/07/2021.
-------------------------------------------
"""

option = int(input("As opções são: \nCachorro quente (1)\nX-salada (2)\nX-burguer (7)\nX-tudo (15)\nQual seu pedido? "))

if option == 1:
    print("\nO pedido é: Cachorro quente , que custa R$3,50 a unidade")

elif option == 2:
    print("\nO pedido é: X-salada , que custa R$5,00 a unidade")

elif option == 7:
    print("\nO pedido é: X-burguer , que custa R$8,90 a unidade")

elif option == 15:
    print("\nO pedido é: X-tudo , que custa R$12,70 a unidade")

else:
    print("Opção inválida")