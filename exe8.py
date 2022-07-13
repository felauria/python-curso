# Exercício (8)
# Use a estrutura de loop for para que o programa retorne todos números pares de 0 até um número especificado por terminal

num  = int(input("Digite um número -> "))

for i in range(0, num + 1):
    if i % 2 == 0:
        print(f"{i} é par")
