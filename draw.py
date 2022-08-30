# Função que pega estado do jogo e printa de acordo com os erros atuais
# Recebe como parâmetro total de erros e printa a cada input do usuário o "bonequinho" do estágio atual
# Se o usuário não errou a letra, continua no mesmo estágio

def stage(errors):

    # errors: 0 Inteiro

    # errors: 1 Cabeça

    # errors: 2 Braço Esq

    # - errors: 3  Braço Dir

    # - errors: 4 Perna Esq 

    # - errors: 5  Perna Dir

    # errors: 6 Game Over

#return current_stage