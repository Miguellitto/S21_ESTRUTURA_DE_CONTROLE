idade = int(input("Digite sua idade: "))
"""
    Este programa mostra a faixa etaria
"""

if idade < 18: # Esta é a primeira condição
    print("Menor de idade") # Menor idade
elif 18 <= idade < 60: # Está é a segunda condição.
    print("Adulto") # Já é considerado adulto.
else: # Maior que essa idade.
    print("Idoso") # Já é considerado idoso.