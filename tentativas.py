

#from main import jogo
from draw import draw_stage

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

def tentativas(numero_de_caracteres,frase,matriz_mapeamento):
    erros = 0
    casas_letras = ["_"]*numero_de_caracteres
    letras_tentadas = []

    for a in range(len(frase)):
        if frase[a] == " ":
            casas_letras[a] = " "

    while True:
        letra = input()
        valor_ascii = ord(letra.lower())-97

        while valor_ascii > 26 or valor_ascii < 0:
            letra = input()
            valor_ascii = ord(letra.lower())-97

        if matriz_mapeamento[valor_ascii] != "no":
           for i in matriz_mapeamento[valor_ascii]:
               casas_letras[i] = chr(valor_ascii+97)
        else:
            erros += 1
            letras_tentadas.append(chr(valor_ascii+97))
            print(letras_tentadas)

        if erros == 6:
            print("Você perdeu!")
            break

        elif "_" not in casas_letras:
            print("Acertou :D")
            break

        print(casas_letras)
