def jogar():
    print('*********************************')
    print('***Bem vindo ao jogo de Forca!***')
    print('*********************************')

    palavra_secreta = 'banana'

    enforcou = False
    acerto = False

    #enquanto não enforcou E não acertou - o not negada o valor bool(booleano)
    #enquanto(not False and not False):
    #enquanto(True and True):
    #enquanto(True):
    while(not enforcou and not acerto):

        index = 0
        chute = input('Qual a letra?')
        chute = chute.strip()

        for letra in palavra_secreta:
            if(chute.upper() == letra.upper()):
                print('Encontrei a letra {} na posição {}'.format(chute, index))
            index = index + 1

        print('Jogando...')

    print('Fim do jogo')

if(__name__ == '__main__'):
    jogar()
