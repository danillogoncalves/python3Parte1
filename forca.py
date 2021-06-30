import random

def jogar():
    print('*********************************')
    print('***Bem vindo ao jogo de Forca!***')
    print('*********************************')

    # arquivo = open('paravras.txt', 'r')
    # Foi mudado para não termos que usa o .close() no final, da fora abaixo ele fecha o arquivo no final da função.
    # Tive que acrecentar o encoging, pois isso não estava sendo feito como padrão o UTF-8, estava o cp1252.
    with open('palavras.txt', 'r', encoding='UTF-8') as arquivo:
        palavras = []

        for linha in arquivo:
            linha = linha.strip()
            palavras.append(linha)

    numero = random.randrange(0,len(palavras))
    palavra_secreta = palavras[numero].upper()

#   for letra in palavra_secreta:
#       letras_acertadas.append('_')
    letras_acertadas = ['_' for letra in palavra_secreta]

    enforcou = False
    acerto = False
    erros = 0
    print(letras_acertadas)

    while(not enforcou and not acerto):

        chute = input('Qual a letra?')
        chute = chute.strip().upper()

        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute == letra):
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1

        enforcou = erros == 6
        acerto = '_' not in letras_acertadas
        print(letras_acertadas)

    if(acerto):
        print('Você ganhou!!!')
    else:
        print('Você perdeu!!!')

    print('Fim do jogo')

if(__name__ == '__main__'):
    jogar()
