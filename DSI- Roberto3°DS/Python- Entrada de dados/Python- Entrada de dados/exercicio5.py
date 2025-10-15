# Área = (base * altura) / 2 
# (P) = a + b + c
## 4. Crie um programa para entrar com a base a altura de -retângulo- e imprimir respectivamente o perímetro e a área correspondente.


##CORREÇÃO:

base =float(input("Informe o valor da Base: "))
altura =float(input("Informe o valor da Altura: "))

p = 2 * (base + altura)
a = base * altura
print('O Perímetro calculado foi:',p,'A Área  calculado foi:',a)


