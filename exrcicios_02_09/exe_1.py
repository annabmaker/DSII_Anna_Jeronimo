# Exercício 1 - Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.


placar = int(input("Quantos pontos o time fez? "))
gols = int(input("Quantos pontos o time sofreu? "))         
if placar > gols:
    print("O time venceu!")
elif placar < gols:
    print("O time perdeu!")
else:
    print("O time empatou!")

""" 
---Correção---

timea = int(input("Informe o número de pontos do time A:"))
timeb = int(input("Informe o número de pontos do time B:"))
if timea > timeb:
    print( f'O time A venceu a partida por {timea} X {timeb} !')
elif timea < timeb:
    print(f'O time B venceu a partida por {timeb} X {timea} !')
else:
    print(f'Terminou empatado o jogo !!!')
    
"""