# Exercício (1)
# Faça um algoritmo que leia a idade de uma pessoa expressa em anos, meses e dias
# e escreva a idade dessa pessoa expressa apenas em dias. Considerar ano com 365 dias e mês com 30 dias.

anos = int(input('Digite quantos anos você possui -> '))
meses = int(input('Digite quantos meses você possui -> '))
dias = int(input('Digite quantos dias você possui -> '))

diasTotais = (anos * 365) + (meses * 30) + dias

print(f"Parabens meu mano, voce possui {diasTotais} dias de vida!! uhuu vc é incrível cara")
