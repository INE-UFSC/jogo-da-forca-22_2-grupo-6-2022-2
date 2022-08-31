continuar_jogo = True
while continuar_jogo:
    matriz_mapeamento = ["no"]*26
    lista_de_frases = ["bola de bilhar", "orientacao a objetos", "manipulacao dos dados", "projeto final", "spaghetti code", "palavra", "teste", "debug", "correcao"]
    opcao = input("digite '1' para adicionar uma frase ou palavra a lista ou '2' para continuar:")
    if opcao == '1':
        continuar = True
        while continuar:
            print("são caracteres aceitos apenas as 26 letras do alfabeto e espaços")
            nova_frase = input("digite a nova frase/palavra:")
            continuar_checagem = input("digite '1' para continuar a adicionar plavras/frases ou '2' para encerrar esse processo")
            if continuar_checagem == '2':
                continuar = False
    frase = input("digite um número entre 0 e %d para selecionar a palavra/frase." % len(lista_de_frases))
    frase = lista_de_frases[int(frase)]
    numero_de_caracteres = len(frase)
    for letra_pos in range (numero_de_caracteres):
        valor_ascii = ord(frase[letra_pos].lower()) - 97
        if frase[letra_pos] == " ":
            continue
        elif matriz_mapeamento[valor_ascii] == "no":
            matriz_mapeamento[valor_ascii] = [letra_pos]
        else:
            matriz_mapeamento[valor_ascii] += [letra_pos]
    continuar_jogo_checagem = input("digite '1' para encerrar o jogo ou '2' para continuar para a próxima rodada:")
    if continuar_jogo_checagem == '1':
        continuar_jogo = False