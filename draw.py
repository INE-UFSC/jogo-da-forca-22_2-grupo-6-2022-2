# Função que pega estado do jogo e printa de acordo com os erros atuais (Implementar)
# Recebe como parâmetro total de erros e printa a cada input do usuário o "bonequinho" do estágio atual (Feito)
import os

'''  Lista de desenhos com índice relativo a quantidade de erros atual do round:
     erros: 0 nada
     erros: 1 cabeça
     erros: 2 corpo
     erros: 3 Perna esq
     erros: 4 Perna dir
     erros: 5 braço esq
     erros: 6 Game Over '''

stage_list = ['''
     _______
     |/      |
     |
     |
     |
     |
     |
    _|___''', '''
    _______
     |/      |
     |      (_)
     |
     |
     |
     |
    _|___''', '''
    _______
     |/      |
     |      (_)
     |       |
     |       |
     |
     |
    _|___''' , '''
    _______
     |/      |
     |      (_)
     |       |
     |       |
     |        \\
     |
    _|___''', '''
    _______
     |/      |
     |      (_)
     |       |
     |       |
     |     // \\
     |
    _|___''', '''
    _______
     |/      |
     |      (_)
     |       |\\
     |       |
     |     // \\
     |
    _|___''', '''
  ______  ____    ____    __  ______   _____  __    _ ______  _____
 |   ___||    \  |    \  /  ||   ___| /     \\  \  //|   ___||     |
 |   |  ||     \ |     \/   ||   ___| |     | \  \// |   ___||    \\
 |______||__|\__\|__/\__/|__||______| \_____/  \__/  |______||__|\__\ ''', '''
__   __  ___   _   _       __      __ ___  _  _   _   
\ \ / / / _ \ | | | |      \ \    / /|_ _|| \| | | |  
 \   / | (_) || |_| |       \ \/\/ /  | | | .  | |_|  
  |_|   \___/  \___/         \_/\_/  |___||_|\_| (_) ''']

def draw_stage(erros):
    os.system('cls')
    print(stage_list[erros], end = "           ")
