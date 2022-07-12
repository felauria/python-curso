# Exercício (9)
# Simule um radar de rodovia
# Onde a velocidade máxima permitida na rodovia é 90 Km/h e a mínima 30 Km/h
# -O programa deve capturar a velocidade do usuário por terminal, caso a resposta esteja em branco o programa deve indicar que a velocidade não foi fornecida
# -Caso o usuário esteja abaixo da velocidade o programa deve retornar que o carro está muito lento e que o usuário deve mudar de mão
# -Caso o usuário esteja acima da velocidade o programa deve computar uma multa para o usuário, sendo o valor dessa multa o excesso de velocidade * 7
# -Caso a velocidade não seja fornecida pelo usuário o programa deve sortear um numero entre 1 e 120 e aplicar a mecânica acima com o numero sorteado

from random import randint as aleatorio

vel = input("Insira a velocidade do veículo -> ")

if int(vel) <= 90 and int(vel) >= 30:
    print("Velocidade permitida!")
elif int(vel) > 90:
    excesso = int(vel) - 90
    multa = excesso * 7
    print(f"Velocidade acima do permitido! \n A multa será de R$ {multa}")
elif int(vel) < 30:
    print("O carro está muito lento. Por favor mude de mão")
elif int(vel) == '':
    num = aleatorio(1,120)
    multa = 7 * num
    print(f"Velocidade não informada! Valor da multa: R$ {multa}")
