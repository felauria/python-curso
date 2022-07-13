# Exercício (12)
# Crie um script que receba 6 números e retorne quais são os números pares e quais são os ímpares

numeros = []
i = 1

for l in range(0,6):
    numeros.append(int(input(f"Digite o {i}º número ->")))
    i += 1

for num in numeros:
    if num % 2 == 0:
        print(f"{num} é par")
    else:
        print(f"{num} é impar")
