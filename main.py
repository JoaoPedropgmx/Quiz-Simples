Questoes = {
    "Questão1": {
        "Questão": "Qual foi o jogador mais jovem a ganhar a copa do mundo?",
        "Resposta": "Pelé"
    },
    "Questão2": {
        "Questão": "Qual foi o primeiro ano da copa?",
        "Resposta": "1930"
    },
    "Questão3": {
        "Questão": "Onde foi realizada a copa de 1998?",
        "Resposta": "França"
    },
    "Questão4": {
        "Questão": "Quem ganhou a copa de 2002?",
        "Resposta": "Brasil"
    },
    "Questão5": {
        "Questão": "Qual o nome do mascote da copa de 2014?",
        "Resposta": "Fuleco"
    },
    "Questão6": {
        "Questão": "Quem ganhou a copa de 1930?",
        "Resposta": "Uruguai"
    },
    "Questão7": {
        "Questão": "Qual o nome do mascote da copa de 1990?",
        "Resposta": "Ciao"
    }
}



def quiz():
    Score = 0
    for chave, valor in Questoes.items():

        print (valor['Questão'])
        resposta = input('Digite sua Resposta: ')

        if resposta.lower() == valor['Resposta'].lower():
            print('Parabens Você Acertou!')
            Score += 1
            print('Score: '+str(Score))
        else:
            print('Você Errou!')
            print('A Resposta Correta é: ' + valor['Resposta'])
            print('Score: '+str(Score))
    if Score == 7:
        print("Parabens Você Acertou todas as Perguntas")

    else:
        retry = input('Gostaria de tentar Novamente? Y/N')
        if retry == 'Y':
            quiz()
        elif retry == 'N':
            print('Obrigado por Participar!')


quiz()
