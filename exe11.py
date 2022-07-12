# Exercício (11)
# Simule uma tentativa de criar uma conta em uma plataforma digital
# -O programa deve conferir se a conta do usuário que está sendo criado possui no mínimo 12 caracteres
# e tenha uma senha que possua de no mínimo 8 caracteres e caracteres numéricos
# -O programa também deve barrar a entrada de caracteres especiais na criação do nome de usuário
# -O programa só deve criar a conta caso todas as condições tenham sido concluídas, se não o programa deve reiniciar voltando para o primeiro processo
# -Quando a conta for criada o programa deve printar a frase: "conta criada!"

from curses.ascii import isalpha


while True:
    print("\n\n\nTELA DE CADASTRO EDUDUCKERS")
    login = input("Insira seu login -> ")
    senha = input("Insira sua senha -> ")

    if login == '' or senha == '':
        print("\nATENCAO! O campo de login/senha está em branco")
        continue

    elif len(login) < 12 or not login.isalpha():
        print("\nATENCAO! O campo de login deve conter no mínimo 12 caracteres e nao deve conter nenhum caractere especial")
        continue

    elif len(senha) < 8 or not any(chr.isdigit() for chr in senha):
        print("\nATENCAO! O campo de senha deve conter no mínimo 8 caracteres e deve conter pelo menos um número")
        continue

    else:
        print("\nCadastro realizado com sucesso!")
        break
