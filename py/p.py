print('$$$$$$$$$$$$$$$$$$$$')
print('jogo de adivinhação!')
print('$$$$$$$$$$$$$$$$$$$$\n')


print('[1] facil\n')
print('[2] medio\n')
print('[3] dificil\n')
dificuldade_str = input('escolha a dificuldade:')
dificuldade = int(dificuldade_str)

if (dificuldade == 1):
    tentativas = 8
if(dificuldade == 2):
    tentativas = 5
if(dificuldade == 3):
    tentativas = 3

    
print('dificuldade escolhida: {}\n' .format(dificuldade))
if(dificuldade == 4):
    print('CHANCE UNICA - BOA SORTE\n')
    tentativas = 1
    
if(dificuldade < 1 or dificuldade > 4):
    tentativas = 0
    print('DIFICULDADE INVALIDA!')
    
    
from random import randint
numero_secreto = randint(1, 100)
rodada = 1

for rodada in range(1, tentativas + 1):
    print( 'Rodada: {} de {}' .format(rodada, tentativas))
    chute_str = input('digite um numero entre 1 e 100:')
    print('voce digitou:', chute_str, '\n')
    chute = int(chute_str)
    
    if (chute < 1 or chute > 100 ):
        print('o numero deve estar entre 1 e 100!')

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if (acertou):
        print('RESPOSTA CERTA!\n')
        break
    else:
        if (menor):
            print('muito baixo\n')
        elif (maior):
                print('muito alto\n')

    if(rodada == tentativas - 1):
        print('ULTIMA CHANCE')


print('Fim de jogo')
print('O numero era: {}' .format(numero_secreto))
