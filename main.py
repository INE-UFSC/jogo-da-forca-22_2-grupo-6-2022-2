matriz_mapeamento = ["no"]*26
frase = input()
numero_de_caracteres = len(frase)
for letra_pos in range (numero_de_caracteres):
    valor_ascii = ord(frase[letra_pos].lower()) - 97
    if frase[letra_pos] == " ":
        continue
    elif matriz_mapeamento[valor_ascii] == "no":
        matriz_mapeamento[valor_ascii] = [letra_pos]
    else:
        matriz_mapeamento[valor_ascii] += [letra_pos]