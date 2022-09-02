
#lista_de_frases = ["bola de bilhar", "orientacao a objetos", "manipulacao dos dados", "projeto final", "spaghetti code", "palavra", "teste", "debug", "correcao"]


import random
from random import randint
from draw import draw_stage

continuar_jogo = True

def jogo():
    lista_de_palavras = open("palavras.txt", "r")
    lista_de_palavras = lista_de_palavras.read().splitlines()
    frase = random.choice(lista_de_palavras)
    numero_de_caracteres = len(frase)
    matriz_mapeamento = formadormatriz(frase, numero_de_caracteres)
    erros = 0
    casas_letras = ["_"] * numero_de_caracteres
    letras_tentadas = []
           
    while True:
        print(casas_letras)
        print("Digite uma letra:")
        print(matriz_mapeamento)
        letra = input()
        valor_ascii = ord(letra.lower())-97
        while valor_ascii > 26 or valor_ascii < 0:
            letra = input()
            valor_ascii = ord(letra.lower())-97

        for letra in range(len(frase)):
            if letra in matriz_mapeamento[valor_ascii]:
                casas_letras[letra] = chr(valor_ascii+97)
            else:
                pass

        if matriz_mapeamento[valor_ascii] != "no":
            for i in matriz_mapeamento[valor_ascii]:
                print(chr(valor_ascii+97), end = " ")
                draw_stage(erros)
        else:
            erros += 1
            if erros <= 5:
                print("Letra errada!")
                draw_stage(erros)
        if erros == 6:
            print("Você perdeu!")
            draw_stage(6)
            menu()
            break
        elif "_" not in casas_letras:
            print("Acertou :D")
            draw_stage(7)
            menu()
            break

def formadormatriz(frase, numero_de_caracteres):
    matriz_mapeamento = ["no"]*26
    for letra_pos in range (numero_de_caracteres):
        valor_ascii = ord(frase[letra_pos].lower()) - 97
        if frase[letra_pos] == " ":
            continue
        elif matriz_mapeamento[valor_ascii] == "no":
            matriz_mapeamento[valor_ascii] = [letra_pos]
        else:
            matriz_mapeamento[valor_ascii] += [letra_pos]
    return matriz_mapeamento

def menu():
    print("Bem vindo ao jogo da forca!")
    print("1 - Adicionar palavra ou frase")
    print("2 - Jogar")
    print("3 - Sair")
    escolha = input()
    if escolha == "1":
        return inserirPalavra()
    elif escolha == "2":
        return jogo()
    else:
        print("Opção inválida!")
        return menu()

def inserirPalavra():
    print("Digite a palavra ou frase que deseja inserir:")
    palavra = input()
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

inserirPalavra()
