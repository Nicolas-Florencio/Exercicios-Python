"""
-----------------------------------------
	Função: Informa se o aluno está aprovado ou reprovado
	Autor: Nicolas Florencio Alves.
	Data de criação: 09/08/2020.
	Data de modificação: 09/08/2020.
-------------------------------------------
"""
nome = str(input("Informe o nome do aluno: "))
media = float(input("Informe a média do aluno: "))
if media >= 7:
    print("\nO aluno %s, está aprovado" % nome)

else:
    print("\nO aluno %s, está reprovado" % nome)