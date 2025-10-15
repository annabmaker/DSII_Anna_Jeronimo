# Exercício 3 - Faça um Programa que peça um número e informe se o número é par ou ímpar.

impar= float(input("Digite um número: "))
if impar % 2 == 0:
    print(f'O número {impar} é par')
else:
    print(f'O número {impar} é ímpar')  
      

"""
---Correção---
n1 = int(input("Digite um número: "))
if n1 % 2 == 0:
    print(f'O número {n1} é par')
else:
    print(f'O número {n1} é ímpar')
"""