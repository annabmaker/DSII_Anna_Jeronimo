#Elabore um algoritmo que dada a idade de um nadador classifique-o em uma das seguintes categorias:
#Infantil A = 5 a 7 anos        
#Infantil B = 8 a 10 anos
#Juvenil A = 11 a 13 anos
#Juvenil B = 14 a 17 anos
#Adultos = maiores de 18 anos

idade = int(input("Digite a idade do nadador: "))
if 5 <= idade <= 7:
    print("Categoria: Infantil A")
elif 8 <= idade <= 10:
    print("Categoria: Infantil B")
elif 11 <= idade <= 13:
    print("Categoria: Juvenil A")   
elif 14 <= idade <= 17:
    print("Categoria: Juvenil B")   
elif idade >= 18:
    print("Categoria: Adultos")
else:
    print("Idade inválida para competição.")

"""
---Correção---
idade = int(input("Informe a idade do nadador: "))
if idade >= 5 and idade <= 7:
    print("Pertence à categoria Infantil A")
elif idade >= 8 and idade <= 10:
    print("Pertence à categoria Infantil B")
elif idade >= 11 and idade <= 13:
    print("Pertence à categoria Juvenil A")
elif idade >= 14 and idade <= 17:
    print("Pertence à categoria Juvenil B")
elif idade >= 18:
    print("Pertence à categoria Adultos")
else:
    print("Idade inválida para competição.")
    """