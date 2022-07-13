# Exercício (10)
# Crie um jogo RPG por turnos de console

# -O programa deve permitir o usuário à escolher entre dois personagens (mago ou guerreiro)
# Caso o usuário escolha guerreiro o programa deve sortear um valor aleatório entre 5 e 10 que será a barra de poder do guerreiro
# Caso o usuário escolha mago o programa deve sortear um valor aleatório entre 7 e 15 que será a barra de poder do mago

# -Dentro do jogo o usuário terá 4 opções:
# Atacar (sorteia um valor de 3 a 10 de dano caso o usuário tenha escolhido guerreiro ou sorteia um valor entre 0 e 8 caso o usuário tenha escolhido um mago, independente do personagem escolhido o jogador gasta 2 de poder por ataque)
# Defender (cancela 1 ataque do inimigo, caso o usuário seja um mago o jogador gasta 1 de poder de ataque),
# Curar (cura 1 de vida no caso do guerreiro e 2 de vida no caso do mago)
# Descansar (sorteia um valor entre 1 e 5 e usa este valor para recuperar pontos de poder)

# -Monstros
# Os monstros são gerados com 20 de vida
# Para atacar o monstro em seu turno escolhe aleatoriamente entre atacar dando 3 de dano ou se defender
# Quando algum monstro é morto, o usuário tem a opção de sair do jogo ou continuar
# Caso o usuário após matar um monstro queira continuar jogando, toda a sua vida é recuperada e o próximo monstro gerado terá 10 de vida e 3 de ataque a mais que o último e o jogador ganhará mais 3 de probabilidade de ataque e mais 5 de vida

import random

print("-=" * 64)
print("Bem vindo ao ROGER PULOS E GRITOS")
nome = input("Digite seu nome: -> ")


while True:
    classe = input("Escolha sua classe: Mago/Guerreiro -> ")

    if classe == "Mago" or classe == "mago":
        classe = "mago"
        poder = random.randint(7,15)
        break

    elif classe == "Guerreiro" or classe == "guerreiro":
        classe = "guerreiro"
        poder = random.randint(5,10)
        break

    else:
        print("Classe não identificada, por favor preencha novamente.")
        continue


print("Em um reino não tão distante chamado Rogersvania, um jovem oriundo de uma família humilde, vivia a servicos do reino para matar a fome de seus parentes.")
print("Até que um dia...\n")
print("houve o chamado")
print("\n\n O reino do norte após se apoderar do livro sagrado dos Gulls, dominou a magia negra e a utilizou para invadir e devastar os reinos vizinhos")
print("Todos do reino corriam sérios perigos até que um ato heróico acendeu a chama de esperanca")
print(f"O jovem {nome}, que até então apenas ajudava na faxina do palácio, se dipos a entrar escondido na terra inimiga e matar o mal pela raiz.")

print(f"\n\nSe aproximando das fazendas de Eli, o {classe} se depara com uma velha senhora que lhe oferece um chá")

while True:
    res = input("O jovem deve aceitar? sim/nao ->")

    if res == "nao":
        print(f"\n{nome} recusa o convite educadamente e se despede da senhora, porém, ao se virar para ir embora,\na mulher o puxa pelos bracos e comeca a se transformar na frente de seus olhos e se revela um terrível monstro")
        break
    elif res == "sim":
        print(f"\n{nome} aceita o convite e se senta com a senhora na varanda da casa. Após longos 30 minutos de conversa, o jovem diz precisar partir e agradece o café\nA senhora sorri e comeca a gargalhar bem alto, o jovem comeca a se sentir tonto e presencia a senhora se transformando em um terrível mostro na frente de seus olhos")
        break
    else:
        print("Responda corretamente.")
        continue
