#Faça um algoritmo que receba um valor sw uma compra e receba o numero de prestações, apresente o valor das prestações sem juros.

valor = float(input("Digite o valor da compra: "))
prestacoes = int(input("Digite o número de prestações: "))
if prestacoes > 0:
    valor_prestacao = valor / prestacoes
    print(f'O valor de cada prestação é: R$ {valor_prestacao:.2f}')
else:
    print("O número de prestações deve ser maior que zero.")

"""
---Correção---
valortotal = float(input("Digite o valor da compra total: "))
n1 = int(input("Digite o número de prestações: "))
prestacao = valortotal / n1
print(f'O valor de cada prestação é: R$ {prestacao}')

"""