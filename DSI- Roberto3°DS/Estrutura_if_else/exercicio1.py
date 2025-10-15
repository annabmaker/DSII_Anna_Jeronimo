# Exercício 1 - Faça um Programa que peça a nota de um aluno,
# e imprima se ele foi aprovado ou reprovado, considerando 6 como nota de
# aprovação.        
nota1 = float(input("Digite a média do aluno: "))
if nota1 >= 6:
    print(f'A média informada é :{nota1} Aluno foi aprovado!')
else:
    print('A média informada é :', nota1, 'Aluno foi reprovado!')

"""
---Correção--- 

n1 = float(input("Digite a média do aluno: "))
n2 = float(input("Digite a média do aluno: "))
media = (n1 + n2) / 2
if media >= 6:
    print(f'A média informada é :{media} Aluno foi aprovado!')  
else:
    print('A média informada é :', media, 'Aluno foi reprovado!')   
# Exercício 2 - Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

valor = float(input("Digite um valor: "))
"""