#lista_de_frases = ["bola de bilhar", "orientacao a objetos", "manipulacao dos dados", "projeto final", "spaghetti code", "palavra", "teste", "debug", "correcao"]
from tentativas import tentativas

continuar_jogo = True

def menu():
    print("Bem vindo ao jogo da forca!")
    print("1 - Adicionar palavra ou frase")
    print("2 - Jogar")
    print("3 - Sair")
    escolha = input()
    if escolha == "1":
        return inserirPalavra()
    elif escolha == "2":
        tentativas()
        menu()
        
    else:
        print("Opção inválida!")
        return menu()

def inserirPalavra():
    print("Digite a palavra ou frase que deseja inserir:")
    palavra = input()
    palavra_valida = True
    for caracter_teste in palavra:
        num_00 = ord(caracter_teste.lower()) - 97
        if (num_00 > 25 or num_00 < 0) and caracter_teste != ' ':
            print("Palavra ou frase inválida!")
            palavra_valida = False
            break
        
    if palavra_valida == True:
        lista_de_palavras = open("palavras.txt", "a")
        lista_de_palavras.write(palavra + "\n")
        lista_de_palavras.close()         
        print("Palavra ou frase inserida com sucesso!")

    while True:
        print("Deseja inserir outra palavra ou frase? (s/n)")
        escolha = input()
        if escolha == "s":
            return inserirPalavra()
        elif escolha == "n":
            return menu()
        else:
            print("Opção inválida!")
    return menu()

menu()
