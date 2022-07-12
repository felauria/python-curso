# Exercício (3)
# Escreva um algoritmo para ler o número total de eleitores de um município, o número de votos brancos, nulos e válidos.
# Calcular e escrever o percentual que cada um representa em relação ao total de eleitores.

numEleitores = int(input("Digite o número de eleitores do município -> "))
numVotosBranco = int(input("Digite o número de votos em branco -> "))
numVotosNulos = int(input("Digite o número de votos nulos -> "))
numVotosValidos = int(input("Digite o número de votos válidos -> "))

print(f"\n Número de eleitores: {numEleitores} \n Percentual de votos em branco: {(numVotosBranco / numEleitores) * 100} % \n Percentual de votos nulos: {(numVotosNulos / numEleitores) * 100} % \n Percentual de votos válidos: {(numVotosValidos  / numEleitores) * 100} %")
