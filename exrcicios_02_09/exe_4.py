#Faça um algoritmo que solicite dois números ao usuário(com decimais) Em seguida solicite que o usuário informe o resultado das quatro operações matemáticas (subtração, multiplicação e divisão) 

num1 = float(input("Digite o primeiro número: "))   
num2 = float(input("Digite o segundo número: "))
soma = float(input("Qual o resultado da soma entre os dois números? "))
subtracao = float(input("Qual o resultado da subtração entre os dois números?"))
multiplicacao = float(input("Qual o resultado da multiplicação entre os dois números? "))   
divisao = float(input("Qual o resultado da divisão entre os dois números? "))
if soma == num1 + num2:
    print("Resultado da soma correto!")
else:
    print("Resultado da soma incorreto!")
if subtracao == num1 - num2:
    print("Resultado da subtração correto!")
else:
    print("Resultado da subtração incorreto!")
if multiplicacao == num1 * num2:
    print("Resultado da multiplicação correto!")
else:
    print("Resultado da multiplicação incorreto!")
if num2 != 0:
    if divisao == num1 / num2:
        print("Resultado da divisão correto!")
        

""""
---Correção---
n1 = int(input("Informe um número: "))
n2 = int(input("Informe um número: "))
s = n1 + n2
sub = n1 - n2
mult= n1 * n2
div = n1 / n2
print(f'A soma entre {n1} e {n2} é: {s}')
print(f'A subtração entre {n1} e {n2} é: {sub}')
print(f'A multiplicação entre {n1} e {n2} é: {mult}')
print(f'A divisão entre {n1} e {n2} é: {div}') 

"""