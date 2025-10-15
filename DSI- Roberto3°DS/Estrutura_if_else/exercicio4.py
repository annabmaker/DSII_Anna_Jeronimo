# exercicio 4 - Faça um programa que pergunte o ano de nascimento de uma pessoa
# e, com base na resposta, informe se ela é maior de idade em 2025.
anoatual= 2025
anodenascimento=int(input("Digite o ano de nascimento: "))
idade=anoatual-anodenascimento
if idade>=18:
    print(f'Quem nasceu em {anodenascimento} tem {idade} anos em 2025!')


""" 
---Correção---
x= int(input("Digite o ano de nascimento: "))
y= 2025 - x
if y>=18:
    print(f'Quem nasceu em {x} tem {y} anos em 2025!')
    print('Essa pessoa é maior de idade!')   
else:
    print(f'Quem nasceu em {x} tem {y} anos em 2025!')  
    print('Essa pessoa é menor de idade!')
   """