import random
from random import randint
from draw import *

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

def tentativas():
    lista_de_palavras = open('palavras.txt', 'r')
    lista_de_palavras = lista_de_palavras.read().splitlines()
    frase = random.choice(lista_de_palavras)
    numero_de_caracteres = len(frase)
    matriz_mapeamento = formadormatriz(frase, numero_de_caracteres)
    erros = 0
    casas_letras = ["_"]*numero_de_caracteres
    letras_tentadas = []
    
    for a in range(len(frase)):
        if frase[a] == " ":
            casas_letras[a] = " "

    while True:
        letras_tentadas = list(set(letras_tentadas))
        letras_tentadas.sort()
        draw_stage(erros)

        for i in casas_letras:
            print(i, end = '')

        print('\nLetras tentadas: ', end = '')

        for a in letras_tentadas:
                print(a, end = ' ')
        print()

        letra = input("Digite uma letra:")
        valor_ascii = ord(letra.lower())-97

        while valor_ascii > 26 or valor_ascii < 0:
            letra = input("Digite novamente (apenas letras do alfabeto): ")
            valor_ascii = ord(letra.lower())-97

        if matriz_mapeamento[valor_ascii] != "no":
           for i in matriz_mapeamento[valor_ascii]:
               casas_letras[i] = chr(valor_ascii+97)
               letras_tentadas.append(chr(valor_ascii+97))
        
        elif letra in letras_tentadas:
            continue

        else:
            erros += 1
            letras_tentadas.append(chr(valor_ascii+97))
        
        if erros == 6:
            draw_stage(erros)
            break
        
        elif "_" not in casas_letras:
            draw_stage(7)
            print('\n\n')
            break