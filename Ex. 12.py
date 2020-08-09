"""
-----------------------------------------
	Função: Informa se o número está entre 5 e 20,
	se estiver entre este intervalo calcula o cubo desse número
	Autor: Nicolas Florencio Alves.
	Data de criação: 09/08/2020.
	Data de modificação: 09/08/2020.
-------------------------------------------
"""
n = int(input("Informe um número: "))
if 5 < n < 20:
    print("O valor de %d ao cubo é: " % n, n**3)

else:
    print("%d não pertence ao intervalo, logo não será exibido seu cubo" % n)