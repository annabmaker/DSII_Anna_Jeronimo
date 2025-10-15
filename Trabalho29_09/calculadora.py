#Exercicio para entrega 23.09.2025
#Elaborar um algoritmo "calculadora" utilizando todos os recursos e comandos vistos em sala de aula.
#Aparecendo o nome do aluno ao executar o programa.

listacal = [" Desenvolvido por Anna Beatriz Campos 3°DS Noturno"]
print(listacal[0])

print("Escolha a operação desejada:")
print("1 - Adição")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")
print("5 - Exponiciação")
print("6 - Resto da Divisão")
operacao = input("Digite o número da operação (1/2/3/4/5/6): ")
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

if operacao == '1':
    resultado = num1 + num2
    print(f"O resultado da adição é: {resultado}")
elif operacao == '2':
    resultado = num1 - num2
    print(f"O resultado da subtração é: {resultado}")
elif operacao == '3':
    resultado = num1 * num2
    print(f"O resultado da multiplicação é: {resultado}")
elif operacao == '4':
    if num2 != 0: # Verifica se o divisor não é zero
        resultado = num1 / num2
        print(f"O resultado da divisão é: {resultado}")
    else:
        print("Erro: Divisão por zero não é permitida.")
elif operacao == '5':
    resultado = num1 ** num2
    
    print(f"O resultado da exponenciação é: {resultado}")
elif operacao == '6':
    resultado = num1 % num2
    print(f"O resultado do resto da operação é: {resultado}")
else:
    print("Operação inválida. Por favor, escolha uma operação entre 1 e 6.")

listacal = ["3°DS", "Beatriz"]
listacal[1] = "Anna Beatriz"
print(listacal)

listacal = ["Anna", "Beatriz", "3°DS"]
listacal.append("Atividade dada pelo professor Roberto Itai")
print(listacal)

listacal = ["Atividade", "Avaliativa", "Professor Roberto Itai"]
for x in listacal:
  print(x)

listacal = ["Anna", "Beatriz", "Campos"]
i = 0
while i < len(listacal):
  print(listacal[i])
  i = i + 1