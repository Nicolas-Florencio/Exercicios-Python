"""
-----------------------------------------
	Função: Informa a classificação do grupo a partir da idade
	Autor: Nicolas Florencio Alves.
	Data de criação: 09/08/2020.
	Data de modificação: 09/08/2020.
-------------------------------------------
"""
idade = int(input("Informe a idade: "))
if 5 <= idade <= 11:
    print("\nPertence a classe Infantil!")

elif 12 <= idade <= 17:
    print("\nPertence a classe Juvenil!")

elif idade >= 18:
    print("Pertence a classe Adulto!")

else:
    print("\nIdade inválida ou não pertence a uma classe!")