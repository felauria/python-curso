# Exercício (6)
# Crie um programa que peça ao usuário um número, e retorne todos os múltiplos do número escolhido pelo usuário de 1 a 10

num = int(input("Digite um número -> "))
i = 1

print("----------------TABUADA--HAHA----------------")

while True:
    res = i*num
    print(f"{i} x {num} = {res} \n")

    if i == 10:
        print("----------------------------------------------")
        break

    i += 1
