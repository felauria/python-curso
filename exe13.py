# (13) Criar uma funcionalidade que retorna a ultima index de um elemento dentro de uma tupla usando for

luva = ("O","melhor","de","todos","gracas","a","Deus","pai.","Obrigado","meu","Deus","!")

for index, elemento in enumerate(luva):
    if luva.count(elemento) > 1:
        posicao = index

print(f"O index do ultimo elemento repetido é {posicao}")
