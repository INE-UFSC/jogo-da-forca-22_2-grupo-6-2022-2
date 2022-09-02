
#lista_de_frases = ["bola de bilhar", "orientacao a objetos", "manipulacao dos dados", "projeto final", "spaghetti code", "palavra", "teste", "debug", "correcao"]


import random
from random import randint
from tentativas import *

continuar_jogo = True

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
    for caracter_teste in palavra:
        num_00 = ord(caracter_teste) - 97
        if num_00 > 25 or num_00 < 0:
            print("Palavra ou frase inválida!")
        else:
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
