c1 = ' '
c2 = ' '
c3 = ' '
c4 = ' '
c5 = ' '
c6 = ' '
c7 = ' '
c8 = ' '
c9 = ' '

casas = [c1, c2, c3, c4, c5, c6, c7, c8, c9]

playerX = 'X'
playerO = 'O'

fim = False

while fim != True:
    for p in (playerX, playerO):
        jogada =  input('Vez do jogador {}: '.format(p))
        if jogada == 'c1' and c1 != playerX and c1 != playerO:
            c1 = p
        elif jogada == 'c2' and c2 != playerX and c2 != playerO:
            c2 = p
        elif jogada == 'c3' and c3 != playerX and c3 != playerO:
            c3 = p
        elif jogada == 'c4' and c4 != playerX and c4 != playerO:
            c4 = p
        elif jogada == 'c5' and c5 != playerX and c5 != playerO:
            c5 = p
        elif jogada == 'c6' and c6 != playerX and c6 != playerO:
            c6 = p
        elif jogada == 'c7' and c7 != playerX and c7 != playerO:
            c7 = p
        elif jogada == 'c8' and c8 != playerX and c8 != playerO:
            c8 = p
        elif jogada == 'c9' and c9 != playerX and c9 != playerO:
            c9 = p
        else:
            print('Jogada inválida')

        
        if (c1 == playerX and c2 == playerX and c3 == playerX) or (c1 == playerO and c2 == playerO and c3 == playerO):
            print('Jogador {} ganhou'.format(c1))
            fim = True
            break
        elif (c4 == playerX and c5 == playerX and c6 == playerX) or (c4 == playerO and c5 == playerO and c6 == playerO):
            print('Jogador {} ganhou'.format(c4))
            fim = True
            break
        elif (c7 == playerX and c8 == playerX and c9 == playerX) or (c7 == playerO and c8 == playerO and c9 == playerO):
            print('Jogador {} ganhou'.format(c7))
            fim = True
            break
        elif (c1 == playerX and c4 == playerX and c7 == playerX) or (c1 == playerO and c4 == playerO and c7 == playerO):
            print('Jogador {} ganhou'.format(c1))
            fim = True
            break
        elif (c2 == playerX and c5 == playerX and c8 == playerX) or (c2 == playerO and c5 == playerO and c8 == playerO):
            print('Jogador {} ganhou'.format(c2))
            fim = True
            break
        elif (c3 == playerX and c6 == playerX and c9 == playerX) or (c3 == playerO and c6 == playerO and c9 == playerO):
            print('Jogador {} ganhou'.format(c3))
            fim = True
            break
        elif (c1 == playerX and c5 == playerX and c9 == playerX) or (c1 == playerO and c5 == playerO and c9 == playerO):
            print('Jogador {} ganhou'.format(c1))
            fim = True
            break
        elif (c3 == playerX and c5 == playerX and c7 == playerX) or (c3 == playerO and c5 == playerO and c7 == playerO):
            print('Jogador {} ganhou'.format(c3))
            fim = True
            break
        elif (c1 == playerX or c1 == playerO) and (c2 == playerX or c2 == playerO) and (c3 == playerX or c3 == playerO) and (c4 == playerX or c4 == playerO) and (c5 == playerX or c5 == playerO) and (c6 == playerX or c6 == playerO) and (c7 == playerX or c7 == playerO) and (c8 == playerX or c8 == playerO) and (c9 == playerX or c9 == playerO):
            print('Fim de Jogo')
            fim = True
            break
        else:
            continue

# inicialização do tabuleiro 
tab = '''
 {} | {} | {}
-----------
 {} | {} | {}
-----------
 {} | {} | {}
'''.format(c1,c2,c3,c4,c5,c6,c7,c8,c9)

print(tab)