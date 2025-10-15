# Exercício 5 - Faça um Programa que leia dois números e mostre o maior deles,
# assim como a diferença entre eles.

a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
if a > b:
    print(f'O primeiro valor é maior')
elif b > a:
    print(f'O segundo valor é maior')
else:
    print(f'Não existe valor maior, os dois são iguais')
    

""" 
---Correção--- 26-08-2025
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))    
if n1 == n2:
    print(f'Não existe valor maior, os dois são iguais {n1}')
elif n1 > n2:
    diferenca = n1 - n2
    print(f'O número {n1} é maior que o número {n2} e a diferença entre eles é {diferenca}')
else:
    diferenca = n2 - n1
    print(f'O número {n2} é maior que o número {n1} e a diferença entre eles é {diferenca}')    
"""