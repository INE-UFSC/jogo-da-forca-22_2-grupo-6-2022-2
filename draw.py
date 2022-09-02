# Função que pega estado do jogo e printa de acordo com os erros atuais (Implementar)
# Recebe como parâmetro total de erros e printa a cada input do usuário o "bonequinho" do estágio atual (Feito)

'''  Lista de desenhos com índice relativo a quantidade de erros atual do round:
     erros: 0 Inteiro
     erros: 1 Braço Esq
     erros: 2 Braço Dir
     erros: 3 Perna Esq 
     erros: 4 Perna Dir
     erros: 5 Corpo
     erros: 6 Game Over '''

stage_list = ['''
     _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / \\
     |
    _|___''', '''
    _______
     |/      |
     |      (_)
     |       |/
     |       |
     |      / \\
     |
    _|___''', '''
    _______
     |/      |
     |      (_)
     |       |
     |       |
     |      / \\
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
     |       
     |
    _|___''' , '''
    _______
     |/      |
     |      (_)
     |       
     |       
     |      
     |
    _|___''', '''                                                                      
  ______  ____    ____    __  ______   _____  __    _ ______  _____   
 |   ___||    \  |    \  /  ||   ___| /     \\\\  \  //|   ___||     |  
 |   |  ||     \ |     \/   ||   ___| |     | \  \// |   ___||     \  
 |______||__|\__\|__/\__/|__||______| \_____/  \__/  |______||__|\__\                                                                      
                                                                      
''', '''ganho uhuu''']

def draw_stage(erros):
    print(stage_list[erros])