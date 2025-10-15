# Exercício 2 - Faça um Programa que peça dois números e imprima o maior deles. 

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))    
if num1 > num2:
    print(f'O número {num1} é maior que o número {num2}')
elif num1 < num2:
    print(f'O número {num2} é maior que o número {num1}')
   

""" 
---Correção---
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
if n1 > n2:
    print(f'O número {n1} é maior que o número {n2}')
else:
    print(f'O número {n2} é maior que o número {n1}')
    """