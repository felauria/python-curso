# Exercício (5)
# Escreva um programa que leia os catetos oposto e adjacente de um triângulo e calcule a hipotenusa


catOposto = int(input("Digite o valor do cateto oposto -> "))
catAdjacente = int(input("Digite o valor do cateto adjacente -> "))

hipotenusa = (catOposto ** 2 + catAdjacente ** 2) ** 0.5

print(f"O valor da hipotenusa é {hipotenusa}")
