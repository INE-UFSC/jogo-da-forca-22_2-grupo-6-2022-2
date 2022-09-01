def tentativas(numero_de_caracteres,frase,matriz_mapeamento):
    erros = 0
    casas_letras = ["_"]*numero_de_caracteres
    letras_tentadas = set()

    for a in range(len(frase)):
        if frase[a] == " ":
            casas_letras[a] = " "

    while True:
        letras_tentadas = set(letras_tentadas)
        letras_tentadas = list(letras_tentadas)
        #print(forca(erros))
        for i in casas_letras:
            print(i, end = '')
        print('\nLetras tentadas: ', end = '')
        for a in letras_tentadas:
            print(a, end = ' ')
        print()

        letra = input()
        valor_ascii = ord(letra.lower())-97
    
        while valor_ascii > 26 or valor_ascii < 0:
            letra = input()
            valor_ascii = ord(letra.lower())-97
    
        if matriz_mapeamento[valor_ascii] != "no":
           for i in matriz_mapeamento[valor_ascii]:
               casas_letras[i] = chr(valor_ascii+97)
               letras_tentadas.append(chr(valor_ascii+97))
        else:
            erros += 1
            letras_tentadas.append(chr(valor_ascii+97))
        
        if erros == 6:
            #print(forca(erros))
            break
        
        elif "_" not in casas_letras:
            #print(vitoria())
            break